[app]

# (str) عنوان برنامه
title = Torch Light

# (str) نام بسته (package)
package.name = torchlight

# (str) دامنهٔ معکوس (برای شناسهٔ یکتا)
package.domain = org.example

# (str) مسیر اصلی برنامه
source.dir = app

# (list) پسوندهای فایل‌های منبع که باید در بسته گنجانده شوند
source.include_exts = py,kv

# (list) فایل‌های استاتیک (آیکون و ...). در این مثال فقط یک آیکون ساده استفاده می‌کنیم.
icon.filename = %(source.dir)s/icon.png

# (str) نسخهٔ برنامه
version = 1.0

# (list) مجوزهای مورد نیاز اندروید
android.permissions = FLASHLIGHT

# (list) کتابخانه‌های پایتون که باید در APK گنجانده شوند
requirements = python3,kivy,plyer

# (str) حداقل نسخهٔ SDK اندروید
android.minapi = 21

# (str) هدف SDK اندروید
android.target = 33

# (bool) فعال‌سازی پشتیبانی از 64‑bit (برای Play Store الزامی است)
android.arch = arm64-v8a

# (bool) استفاده از Java 8
android.api = 33

# (bool) فعال‌سازی حالت debug (برای تست)
debug = 1

# (bool) فعال‌سازی حالت release (بعد از تست)
# release = 1   # وقتی آماده انتشار شد، این خط را فعال کنید.

# (str) مسیر خروجی APK (در پوشه bin)
# خروجی به‌صورت torchlight-1.0-debug.apk خواهد بود.
