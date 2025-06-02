from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard

def fix_arabic(text):
    # تحويل النص العربي للعرض الصحيح (عكس + اتصال حروف)
    return ''.join(reversed(text))

club_names = {
    "برشلونة": "ﻰﻧﻮﻠﺳﺭﺎﺑ",
    "الهلال": "ﻝﺍﻟﻻﻫ",
    "النصر": "ﺭﺻﻧﻻﺍ",
    "الاتحاد": "ﺪﺣﺘﻟﺍ",
    "ريال مدريد": "ﺪﻳﺭﺪﻣ ﻝﺎﻳﺭ",
    "أتلتيكو مدريد": "ﺪﻳﺭﺪﻣ ﻮﻜﺘﻟﺗﺍ"
}

class ArabicConverter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        self.input = TextInput(hint_text='أدخل النص العربي هنا', multiline=True, font_size=20)
        self.add_widget(self.input)
        
        self.output = TextInput(hint_text='النص المعالج', readonly=True, font_size=20)
        self.add_widget(self.output)

        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        btn_layout.add_widget(Button(text='تحويل', on_press=self.convert))
        btn_layout.add_widget(Button(text='نسخ', on_press=self.copy_output))
        btn_layout.add_widget(Button(text='مسح', on_press=self.clear_all))
        self.add_widget(btn_layout)

        self.add_widget(Button(text='تحويل اسم نادي تلقائيًا', size_hint_y=None, height=50, on_press=self.convert_club))

    def convert(self, instance):
        self.output.text = fix_arabic(self.input.text)

    def copy_output(self, instance):
        Clipboard.copy(self.output.text)

    def clear_all(self, instance):
        self.input.text = ""
        self.output.text = ""

    def convert_club(self, instance):
        text = self.input.text.strip()
        self.output.text = club_names.get(text, fix_arabic(text))

class ArabicConverterApp(App):
    def build(self):
        return ArabicConverter()

if __name__ == '__main__':
    ArabicConverterApp().run()