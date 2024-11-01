from ui.login_view import LoginView
import customtkinter as ctk

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    login_app = LoginView()
    login_app.mainloop()