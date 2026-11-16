# Shizuku as an option for app updates (supplement)

Read from the project's README on 2026-11-16: https://github.com/RikkaApps/Shizuku
- Shizuku has the user start a server once, through root or ADB, and then lets other apps call Android system APIs with that higher permission through it, instead of running slow shell commands.
- Developer docs: https://github.com/RikkaApps/Shizuku-API

For an app that wants smoother self-updates outside a store, Shizuku can be started with root or with ADB, so a phone without root can use it only if the user can set up a supported ADB start. That setup is extra work for the user and its steps were not checked here. Whether it fits a given update flow was not tested; compare it with the plain installer prompt, F-Droid and Obtainium notes.
