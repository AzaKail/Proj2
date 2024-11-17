from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp
from reg import LoginScreen
from chat import ChatScreen

sm = ScreenManager()
class MainApp(MDApp):
    def build(self):
        # Создаем ScreenManager с переходами
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.current_user = None  # Данные авторизованного пользователя

        # Добавляем экраны
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(ChatScreen(name='chat'))

        return self.sm

    def set_current_user(self, user_data):
        """Сохраняет текущего пользователя и переходит на экран чата"""
        self.sm.current_user = user_data
        self.sm.current = 'chat'

if __name__ == '__main__':
    MainApp().run()
