# Mihon's keep-alive progress notification for batch update checks

Research note, checked 23 Nov 2026 against the current Mihon source on GitHub (mihonapp/mihon, the community fork that continues Tachiyomi; the package paths still read eu.kanade.tachiyomi). Prompted by Unggun: a batch of update checks runs silently, and when several apps sit queued behind a rate limit the phone shows nothing. The request: a keep-alive notification with progress bar updates, and Mihon is the reference because its library update solves exactly this shape of problem - hundreds of metadata checks in a background worker, with the user wanting to see it moving.

## What Mihon actually does

Two files: LibraryUpdateWorker.kt and LibraryUpdateNotifier.kt in app/src/main/java/eu/kanade/tachiyomi/data/library/ (source: https://github.com/mihonapp/mihon/tree/main/app/src/main/java/eu/kanade/tachiyomi/data/library).

1. **The worker promotes itself to a foreground service.** At the start of work it calls setForeground, and getForegroundInfo() returns a ForegroundInfo built from the progress notification with FOREGROUND_SERVICE_TYPE_DATA_SYNC (Android 10+). This is the keep-alive half of the trick: while the notification is attached as foreground, Android treats the process as user-visible work, so a long batch is not killed mid-run and the notification cannot be swiped away.
2. **One ongoing notification, updated in place.** The builder is created once and cached: dedicated low-importance progress channel, setOngoing(true), setOnlyAlertOnce(true) so updates never re-buzz, and a Cancel action whose pending intent broadcasts to a receiver that cancels the work. Every update calls setProgress(total, current, false) for a determinate bar, sets the title to a formatted percentage, and uses BigTextStyle to list the items currently being fetched (each title chopped to 40 chars). There is a preference to hide the item list for privacy.
3. **Updates are throttled, not per-item.** showProgressNotification skips updates arriving faster than NOTIF_PROGRESS_INTERVAL_MS = 500ms (except the final one), because several fetch coroutines call it at once and the system would drop most of them anyway. The notifier is @Synchronized around the shared builder.
4. **Progress is reported before and after each item.** A wrapper adds the item to a "currently updating" list, posts the notification, runs the check, then removes it, increments the completed counter, and posts again. The bar therefore moves even when individual checks are slow or stalled.
5. **The notification is always canceled in a finally block**, so a finished, failed or canceled batch never leaves a stale ongoing notification behind.

## What transfers to Unggun

Unggun's background update task has the same shape: N apps checked with bounded concurrency, errors aggregated at the end, and today only a transient "checking updates" notification that carries no progress. The 0.1.6 change (rate-limited apps queued for automatic recheck) makes the silence more visible, because a queued recheck can sit pending for up to an hour.

Directly applicable:

- A single ongoing progress notification per batch, updated in place with setProgress(total, current, false) and onlyAlertOnce, listing the apps currently being checked, throttled to about 500ms.
- Post before and after each app so slow checks still move the bar.
- Cancel action that cancels the remaining batch.
- Cancel the notification in finally, unconditionally.

The caveat: Unggun's checks run through the Flutter workmanager plugin, which does not expose WorkManager's setForeground/expedited API. The true keep-alive (foreground-service promotion, FOREGROUND_SERVICE_TYPE_DATA_SYNC) needs either native glue or accepting that the notification is informational while the worker is an ordinary background worker subject to normal quotas. The progress-notification half is achievable from Dart today with the notification stack Unggun already uses; the progress count already exists for the UI (completed/total behind refreshProgress) and would need to be forwarded to the notification layer inside the background isolate.

## Takeaway

Mihon's design is worth copying almost literally: foreground-promoted worker plus one cached, throttled, cancelable ongoing notification whose bar moves per item. For Unggun the notification half is a straightforward change; the foreground-service half is the part that needs a platform decision first.

Sources: LibraryUpdateWorker.kt and LibraryUpdateNotifier.kt, mihonapp/mihon main branch, retrieved 2026-11-23.
