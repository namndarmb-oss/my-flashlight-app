from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

# safe import for flash (so running on desktop or during some build steps won't crash)
try:
    from plyer import flash
except Exception:
    flash = None

class LuxuryTorch(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_on = False
        self.md_bg_color = get_color_from_hex("#0F0F12") # مشکی فوق‌العاده تیره

        # عنوان لوکس
        self.add_widget(MDLabel(
            text="L U X E  T O R C H",
            halign="center",
            pos_hint={"center_y": 0.85},
            font_style="H5",
            theme_text_color="Custom",
            text_color=get_color_from_hex("#D4AF37") # رنگ طلایی کلاسیک
        ))

        # دکمه اصلی با سایه و استایل
        self.btn = MDIconButton(
            icon="power",
            icon_size="100sp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            md_bg_color=get_color_from_hex("#1A1A1F"),
            theme_icon_color="Custom",
            icon_color=get_color_from_hex("#444444")
        )
        self.btn.bind(on_release=self.toggle_flash)
        self.add_widget(self.btn)

    def toggle_flash(self, instance):
        try:
            if not self.is_on:
                if flash:
                    flash.on()
                else:
                    print("Flash API not available on this platform")
                self.is_on = True
                self.btn.icon_color = get_color_from_hex("#D4AF37") # روشن شدن به رنگ طلایی
                self.btn.md_bg_color = get_color_from_hex("#25252B")
            else:
                if flash:
                    flash.off()
                else:
                    print("Flash API not available on this platform")
                self.is_on = False
                self.btn.icon_color = get_color_from_hex("#444444")
                self.md_bg_color = get_color_from_hex("#0F0F12")
        except Exception as e:
            print(f"Error: {e}")

class TorchApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return LuxuryTorch()

if __name__ == "__main__":
    TorchApp().run()
