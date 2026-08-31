from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class OqyolTaxiApp(MDApp):
    def build(self):
        return MDLabel(text="OQYOL TAXI", halign="center")

if __name__ == '__main__':
    OqyolTaxiApp().run()
