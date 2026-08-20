from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex
from plyer import flash

class LuxuryTorch(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_on = False
        self.md_bg_color = get_color_from_hex("#0F0F12")

        # عنوان
        self.add_widget(MDLabel(
            text="L U X E  T O R C H",
            halign="center",
            pos_hint={"center_y": 0.85},
            font_style="H5",
            theme_text_color="Custom",
            text_color=get_color_from_hex("#D4AF37")
        ))

        # دکمه
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
                flash.on()
                self.is_on = True
                self.btn.icon_color = get_color_from_hex("#D4AF37")
                self.btn.md_bg_color = get_color_from_hex("#25252B")
            else:
                flash.off()
                self.is_on = False
                self.btn.icon_color = get_color_from_hex("#444444")
                self.btn.md_bg_color = get_color_from_hex("#1A1A1F")
        except Exception as e:
            print(f"Error: {e}")

class TorchApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        return LuxuryTorch()

if __name__ == "__main__":
    TorchApp().run()
