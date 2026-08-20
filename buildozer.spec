[app]
title = Luxury Torch
package.name = luxytorch
package.domain = org.mqm.luxe
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,kivymd,plyer

# مجوزهای الزامی
android.permissions = CAMERA, WAKE_LOCK
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
orientation = portrait
fullscreen = 1

# برای جلوگیری از خطاهای احتمالی در بیلد
p4a.branch = master
