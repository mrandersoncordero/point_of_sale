import customtkinter as ct

class DashBoardView(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title('Dashboard - Sistema de Ventas')
        self.resizable(False, False)
        # self.create_interface()

    def window_menu(self):
        self.frame_left = ct.CTkFrame(self, width=200, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky='nsew')
        self.frame_center = ct.CTkFrame(self, corner_radius=0)
        self.frame_center.grid(row=0, column=1, sticky='nsew')
        self.frame_right = ct.CTkFrame(self, width=400, corner_radius=0)
        self.frame_right.grid(row=0, column=2, sticky='nsew')

        btn_products = ct.CTkButton(self.frame_left, text='Productos')
        btn_products.grid(row=0, column=0, padx=10, pady=(10,0))
        btn_sales = ct.CTkButton(self.frame_left, text='Ventas')
        btn_sales.grid(row=1, column=0, padx=10, pady=(10,0))
        btn_clients = ct.CTkButton(self.frame_left, text='Clientes')
        btn_clients.grid(row=2, column=0, padx=10, pady=(10,0))
        btn_purchases = ct.CTkButton(self.frame_left, text='Compras')
        btn_purchases.grid(row=3, column=0, padx=10, pady=(10,0))
        btn_users = ct.CTkButton(self.frame_left, text='Usuarios',
                                 command=self.window_users_list)
        btn_users.grid(row=4, column=0, padx=10, pady=(10,0))
        btn_reports = ct.CTkButton(self.frame_left, text='Reportes')
        btn_reports.grid(row=5, column=0, padx=10, pady=(10,0))
        btn_backup = ct.CTkButton(self.frame_left, text='Backup')
        btn_backup.grid(row=6, column=0, padx=10, pady=(10,0))
        btn_restore_bd = ct.CTkButton(self.frame_left, text='Restaurar BD')
        btn_restore_bd.grid(row=7, column=0, padx=10, pady=10)

        lbl2 = ct.CTkLabel(self.frame_center, text='Aqui pondremos las ventanas del menu')
        lbl2.grid(row=0, column=0, padx=10, pady=10)

        lbl3 = ct.CTkLabel(self.frame_right, text='Aqui pondremos las busquedas para la venta')
        lbl3.grid(row=0, column=0, padx=10, pady=10)

    def window_users_list(self):
        self.frame_user_list = ct.CTkFrame(self.frame_center)
        self.frame_user_list.grid(row=0, column=0,
                                  columnspan=2,
                                  sticky='nsew')
        self.lbl_frame_button_list_user = ct.CTkLabel(self.frame_user_list)
        self.lbl_frame_button_list_user.grid(row=0, column=0, sticky='nsew')

        btn_user_new = ct.CTkButton(self.lbl_frame_button_list_user, text='Nuevo')
        btn_user_new.grid(row=0, column=0, padx=5, pady=5)
        btn_user_edit = ct.CTkButton(self.lbl_frame_button_list_user, text='Modificar')
        btn_user_edit.grid(row=0, column=1, padx=5, pady=5)
        btn_user_delete = ct.CTkButton(self.lbl_frame_button_list_user, text='Eliminar')
        btn_user_delete.grid(row=0, column=2, padx=5, pady=5)

        self.lbl_frame_search_list_user = ct.CTkFrame(self.frame_user_list)
        self.lbl_frame_search_list_user.grid(row=1, column=0, sticky='nsew')

        txt_search_users = ct.CTkEntry(self.lbl_frame_search_list_user) # width=450 puede ser
        txt_search_users.grid(row=0, column=0, padx=5, pady=5)


if __name__ == '__main__':
    ct.set_appearance_mode("dark")  # Opciones: "dark", "light", "system"
    ct.set_default_color_theme("blue")  # Opciones: "blue", "green", "dark-blue"
    app = DashBoardView()
    app.attributes("-zoomed", True)
    app.window_menu()
    app.mainloop()