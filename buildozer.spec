[app]

# (str) Title of your application
title = Cable Color Converter

# (str) Package name
package.name = cablecolorconverter

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

[android]

# (int) Target Android API, should be as high as possible.
api = 31

# (int) Minimum API your APK / AAB will support.
minapi = 21

# (str) Android NDK version to use (match what's available)
ndk = 27.2.12479018

# (bool) Use --private data storage (True) or --dir public storage (False)
private_storage = True

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
accept_sdk_license = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# Build for single arch to avoid conflicts
archs = arm64-v8a

# (str) python-for-android branch to use
p4a.branch = master

# (str) python-for-android git clone directory
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
# Run `buildozer android list` to see available bootstraps.
bootstrap = sdl2

[buildozer:global]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
