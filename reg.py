from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from supabase import create_client, Client

# Настройки Supabase
url = "https://olzyhnpnhadusvrryawv.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9senlobnBuaGFkdXN2cnJ5YXd2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzA2NjAwNzAsImV4cCI6MjA0NjIzNjA3MH0.pXJHX1HXljvAV2X1Q2cHNNfC7b6M7mtu9XuH4Tga_bg"  # Замените на ваш ключ
supabase: Client = create_client(url, key)

# Загрузка интерфейса из KV-файла
Builder.load_file("reg.kv")


class LoginScreen(Screen):
    def logger(self):
        """Обработчик входа пользователя"""
        email = self.ids.user.text
        password = self.ids.password.text

        try:
            response = supabase.auth.sign_in_with_password({"email": email, "password": password})
            if response:
                # Сохраняем пользователя и переходим на экран чата
                MDApp.get_running_app().set_current_user({"email": email})
            else:
                self.ids.welcome_label.text = "Ошибка входа. Проверьте почту и пароль."
        except Exception as e:
            self.ids.welcome_label.text = f"Ошибка: {e}"

    def register_user(self):
        email = self.ids.user.text
        password = self.ids.password.text
        try:
            response = supabase.auth.sign_up({"email": email, "password": password})
            if response.user:
                self.ids.welcome_label.text = "Регистрация успешна! Проверьте почту для подтверждения."
                supabase.from_("profiles").insert({"email": email}).execute()

                # После успешной регистрации сразу переводим на экран чата
                # MDApp.get_running_app().root.current = 'chat'
            else:
                self.ids.welcome_label.text = "Не удалось зарегистрироваться."
        except Exception as e:
            self.ids.welcome_label.text = f"Ошибка: {e}"
