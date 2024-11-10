from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('login.kv')

    def logger(self):
        self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'

    def register(self):
        # Обработчик для кнопки "Регистрация"
        self.root.ids.welcome_label.text = "Регистрация нажата"

MainApp().run()
