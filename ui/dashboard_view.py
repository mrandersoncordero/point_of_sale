import customtkinter as ctk
from tkinter import ttk

from ui.user_view import UserView

class DashBoardView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Dashboard - Sistema de Ventas')
        self.resizable(False, False)
        self.styles()
        self.window_menu()
        self.user_view = None  # Declaración de la instancia de UserView

    def styles(self):
        # ===== Estilos de la Tabla =====
        self.style = ttk.Style()
        self.style.theme_use("alt")  # Seleccionar tema base para personalizar

        # Estilo de celdas de datos
        self.style.configure("Treeview",
                        background="#333333",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#333333")
        self.style.map("Treeview", background=[("selected", "#1f538d")])

        # Estilo para las cabeceras de la tabla
        self.style.configure("Treeview.Heading",
                        background="#444444",
                        foreground="white",
                        font=("Arial", 12, "bold"))
        self.style.map("Treeview.Heading",
                  background=[("active", "#555555")])  # Cambiar el fondo al pasar el cursor

    def window_menu(self):
        # Interfaz
        self.frame_left = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky='nsew')
        self.frame_center = ctk.CTkFrame(self, corner_radius=0)
        self.frame_center.grid(row=0, column=1, sticky='nsew')
        self.frame_right = ctk.CTkFrame(self, width=400, corner_radius=0)
        self.frame_right.grid(row=0, column=2, sticky='nsew')

        # Interfaz - Left
        btn_products = ctk.CTkButton(self.frame_left, text='Productos')
        btn_sales = ctk.CTkButton(self.frame_left, text='Ventas')
        btn_clients = ctk.CTkButton(self.frame_left, text='Clientes')
        btn_purchases = ctk.CTkButton(self.frame_left, text='Compras')
        btn_users = ctk.CTkButton(self.frame_left, text='Usuarios',
                                 command=self.show_user_view)
        btn_reports = ctk.CTkButton(self.frame_left, text='Reportes')
        btn_backup = ctk.CTkButton(self.frame_left, text='Backup')
        btn_restore_bd = ctk.CTkButton(self.frame_left, text='Restaurar BD')

        btn_products.grid(row=0, column=0, padx=10, pady=(10,0))
        btn_sales.grid(row=1, column=0, padx=10, pady=(10,0))
        btn_clients.grid(row=2, column=0, padx=10, pady=(10,0))
        btn_purchases.grid(row=3, column=0, padx=10, pady=(10,0))
        btn_users.grid(row=4, column=0, padx=10, pady=(10,0))
        btn_reports.grid(row=5, column=0, padx=10, pady=(10,0))
        btn_backup.grid(row=6, column=0, padx=10, pady=(10,0))
        btn_restore_bd.grid(row=7, column=0, padx=10, pady=10)

        # Interfaz - Center
        lbl2 = ctk.CTkLabel(self.frame_center, text='Aqui pondremos las ventanas del menu')
        lbl2.grid(row=0, column=0, padx=10, pady=10)

        # Interfaz - Right
        lbl3 = ctk.CTkLabel(self.frame_right, text='Aqui pondremos las busquedas para la venta')
        lbl3.grid(row=0, column=0, padx=10, pady=10)

    def show_user_view(self):
        if self.user_view is not None:
            self.user_view.grid_forget()  # Elimina la vista de usuario actual si ya existe
        self.user_view = UserView(self.frame_center)
        self.user_view.grid(row=0, column=0, sticky="nsew")

if __name__ == '__main__':
    ctk.set_appearance_mode("dark")  # Opciones: "dark", "light", "system"
    ctk.set_default_color_theme("blue")  # Opciones: "blue", "green", "dark-blue"
    app = DashBoardView()
    app.attributes("-zoomed", True)
    app.window_menu()
    app.mainloop()