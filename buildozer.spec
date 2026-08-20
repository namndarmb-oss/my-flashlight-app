[app]
title = Luxury Torch
package.name = luxetorch
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,ttf
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,plyer==2.1.0
orientation = portrait
fullscreen = 0
android.permissions = CAMERA, FLASHLIGHT
android.features = android.hardware.camera, android.hardware.camera.flash
android.archs = arm64-v8a, armeabi-v7a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.private_storage = True
android.accept_sdk_license = True
android.entrypoint = main
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1
