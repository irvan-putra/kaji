# Changing an Android app's application ID: what the official docs say

Status: read 2026-11-16 from Android's own pages. Where the docs are silent, this note says so; nothing was tested on a device.

## What the docs say
- The application ID uniquely identifies the app on the device and in Google Play. Once an app is published, Android's guide says never to change it: Play treats an upload with a different ID as a completely different app, and a new version of an existing app must use the same application ID and signing certificate. https://developer.android.com/build/configure-app-module
- Google Play's help states that package names are unique and permanent. https://support.google.com/googleplay/android-developer/answer/113469
- The namespace used in code can be changed separately from the application ID, per the same Android page, so a code rename does not by itself change the installed identity.

## What follows (reasoning, not tested)
- Because the ID identifies the app on the device, an app with a new ID would be a separate app. A phone that has the old app may be able to keep it installed next to the new one; this note did not test that, and it does not say the old app stops working.
- The old app keeps receiving updates only if updates for it continue to be published under the old ID and certificate.
- The new app needs its own update path (a store listing or download source), and data in the old app is not moved by Android automatically; any handoff (export and import, or a bridge release) has to be built.

## Checks before changing an ID
Whether the old ID has been published or distributed, who updates it, which signing key each ID uses, and how users move their data.
