import customtkinter as ct
from views.login_view import LoginView

def main():
    app = LoginView()
    app.mainloop()

if __name__ == '__main__':
    ct.set_appearance_mode("dark")  # Opciones: "dark", "light", "system"
    ct.set_default_color_theme("blue")  # Opciones: "blue", "green", "dark-blue"
    main()