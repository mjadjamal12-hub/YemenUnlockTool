from kivy.app import App
from kivy.uix.button import Button
class YemenTool(App):
    def build(self):
        # هذا هو نص الزر الذي سيظهر في تطبيقك
        return Button(text='Yemen Unlock Tool\nVersion 1.0\nReady', font_size=30)
if __name__ == "__main__":
    YemenTool().run()
