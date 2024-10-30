from tkinter.constants import CENTER

import customtkinter as ct

class Sale(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Ventas")
        self.geometry("400x300")
        self.resizable(False, False)
        self.styles()
        self.create_label_frame()

    def styles(self):
        pass

    def create_label_frame(self):
        # Crear el marco principal
        label_frame = ct.CTkFrame(self, corner_radius=10)
        label_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Agregar un título al "LabelFrame"
        label_title = ct.CTkLabel(label_frame, text="Inicio de Sesion",
                                  font=("Arial", 16, "bold"))
        label_title.pack(pady=(10, 0))

        # Agregar widgets dentro del label_frame usando pack
        txt_user = ct.CTkEntry(label_frame, placeholder_text="Usuario", width=400)
        txt_user.pack(pady=10, padx=20)

        txt_password = ct.CTkEntry(label_frame, placeholder_text="Contraseña", show="*",
                                   width=400)
        txt_password.pack(pady=10, padx=20)

        btn_login = ct.CTkButton(label_frame, text="Iniciar Sesión", corner_radius=10,
                                 width=320,
                                 border_color='#345683',
                                 border_width=2)
        btn_login.pack(pady=10)

def main():
    ct.set_appearance_mode("dark")  # Opciones: "dark", "light", "system"
    ct.set_default_color_theme("blue")  # Opciones: "blue", "green", "dark-blue"
    app = Sale()
    app.mainloop()

if __name__ == "__main__":

    main()
