import customtkinter as ctk
from controllers.login_controller import LoginController
from ui.dashboard_view import DashBoardView
from tkinter import messagebox

class LoginView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Sistema de Ventas")
        self.geometry("400x300")

        # Controlador de login
        self.controller = LoginController()

        self.init_interface()

    def init_interface(self):
        # Crear el marco principal
        self.frame_login = ctk.CTkFrame(self, corner_radius=10)
        self.frame_login.pack(padx=20, pady=20, fill="both", expand=True)

        # Interfaz de Login
        label_title = ctk.CTkLabel(self.frame_login, text="Inicio de Sesion", font=("Arial", 16, "bold"))

        self.username_entry = ctk.CTkEntry(self.frame_login, placeholder_text="Usuario", width=400)
        self.password_entry = ctk.CTkEntry(self.frame_login, placeholder_text="Contraseña", show="*", width=400)
        login_button = ctk.CTkButton(self.frame_login, text="Ingresar", command=self.verificar_credenciales,
                                  corner_radius=10,
                                  width=320,
                                  border_color='#345683',
                                  border_width=2)
        # Layout
        label_title.pack(pady=(10, 0))
        self.username_entry.pack(pady=10, padx=20)
        self.password_entry.pack(pady=10, padx=20)
        login_button.pack(pady=10)

    def verificar_credenciales(self):
        """Verifica el usuario y la contraseña."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.controller.autenticar(username, password):
            messagebox.showinfo("Éxito", "¡Login correcto!")
            self.destroy()  # Cierra la ventana de login
            dashboard_app = DashBoardView()  # Abre la ventana de inventario
            dashboard_app.mainloop()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")