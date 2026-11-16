# Android home-screen widgets: which views are allowed, and how taps work in lists

Status: Android developer documentation read 2026-11-16. Documentation summary only; nothing was run.

## Allowed views
The `RemoteViews` reference says it "is limited to support for the following layouts": AdapterViewFlipper, FrameLayout, GridLayout, GridView, LinearLayout, ListView, RelativeLayout, StackView, ViewFlipper. And the following widgets: AnalogClock, Button, Chronometer, ImageButton, ImageView, ProgressBar, TextClock, TextView. As of API 31, CheckBox, RadioButton, RadioGroup and Switch may also be used. "Descendants of these classes are not supported."
https://developer.android.com/reference/android/widget/RemoteViews

Implication (reasoning, not a source claim): a plain `android.view.View`, for example an empty spacer, is not on that list, so a widget layout using one should not be assumed to work. How the platform enforces the list was not checked here.

## Taps inside a list widget
The collections guide says `setOnClickPendingIntent()` "is not allowed for child views in an individual collection item". Instead: "to add click behavior to individual items in a collection, use `setOnClickFillInIntent()`", with a pending-intent template set on the collection view and a fill-in intent set per item in the `RemoteViewsFactory`.
https://developer.android.com/develop/ui/views/appwidgets/collections

The same guide permits `setOnClickPendingIntent()` for a global element outside the collection items. Whether every pixel of a widget can be made tappable was not established from documentation.

## Not established
Swipe or pull-to-refresh on widgets: the pages read did not state either way, so no claim is made here.
