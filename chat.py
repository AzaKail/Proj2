from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from supabase import create_client, Client

# Настройки Supabase
url = "https://olzyhnpnhadusvrryawv.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9senlobnBuaGFkdXN2cnJ5YXd2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzA2NjAwNzAsImV4cCI6MjA0NjIzNjA3MH0.pXJHX1HXljvAV2X1Q2cHNNfC7b6M7mtu9XuH4Tga_bg"  # Замените на ваш ключ
supabase: Client = create_client(url, key)

class ChatScreen(Screen):
    search_input = ObjectProperty(None)
    user_list = ObjectProperty(None)

    def on_pre_enter(self, *args):
        """Инициализация экрана перед его отображением."""
        app = MDApp.get_running_app()
        user_email = app.root.current_user
        self.ids.welcome_label.text = f"Вы вошли как: {user_email}"

    def search_users(self):
        """Поиск пользователей по email."""
        search_query = self.search_input.text.strip()
        self.user_list.clear_widgets()

        if not search_query:
            self.user_list.add_widget(OneLineListItem(text="Введите email для поиска."))
            return

        try:
            response = supabase.from_("profiles").select("email").ilike("email", f"%{search_query}%").execute()
            if response.data:
                for user in response.data:
                    item = OneLineListItem(
                        text=user["email"],
                        on_release=lambda x=user: self.start_chat(x["email"])
                    )
                    self.user_list.add_widget(item)
            else:
                self.user_list.add_widget(OneLineListItem(text="Пользователи не найдены."))
        except Exception as e:
            self.user_list.add_widget(OneLineListItem(text=f"Ошибка поиска: {str(e)}"))

    def start_chat(self, email):
        """Начало чата с выбранным пользователем."""
        print(f"Начало чата с {email}")
