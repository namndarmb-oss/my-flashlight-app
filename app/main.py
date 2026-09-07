:torchlight/app/main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from plyer import flashlight
from kivy.properties import BooleanProperty

# بارگذاری فایل KV
Builder.load_file('torchlight/app/torchlight.kv')

class TorchLayout(BoxLayout):
    # وضعیت فعلی چراغ قوه (True = روشن)
    is_on = BooleanProperty(False)

    def toggle_flashlight(self):
        """روشن/خاموش کردن چراغ قوه"""
        if self.is_on:
            flashlight.off()
            self.is_on = False
        else:
            flashlight.on()
            self.is_on = True

class TorchApp(App):
    def build(self):
        return TorchLayout()

if __name__ == '__main__':
    TorchApp().run()
