import customtkinter as ct
from views.dashboard_view import  DashBoardView

class LoginView(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title('Login - Sistema de Ventas')
        self.geometry("400x300")
        self.create_interface()

    def create_interface(self):
        # Crear el marco principal
        self.frame_login = ct.CTkFrame(self, corner_radius=10)
        self.frame_login.pack(padx=20, pady=20, fill="both", expand=True)

        # Agregar un título al "LabelFrame"
        label_title = ct.CTkLabel(self.frame_login, text="Inicio de Sesion",
                                  font=("Arial", 16, "bold"))
        label_title.pack(pady=(10, 0))

        # Agregar widgets dentro del label_frame usando pack
        txt_user = ct.CTkEntry(self.frame_login, placeholder_text="Usuario", width=400)
        txt_user.pack(pady=10, padx=20)

        txt_password = ct.CTkEntry(self.frame_login, placeholder_text="Contraseña", show="*",
                                   width=400)
        txt_password.pack(pady=10, padx=20)

        btn_login = ct.CTkButton(self.frame_login, text="Iniciar Sesión", command=self.login,
                                 corner_radius=10,
                                 width=320,
                                 border_color='#345683',
                                 border_width=2)
        btn_login.pack(pady=10)

    def login(self):
        self.after(1000, self.destroy()) # Aqui ocultamos la ventana login
        DashBoardView().window_menu()

if __name__ == "__main__":
    app = LoginView()
    app.mainloop()