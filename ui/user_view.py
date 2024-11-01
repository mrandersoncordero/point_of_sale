import customtkinter as ctk
from tkinter import ttk
from controllers.user_controller import UserController

class UserView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = UserController()
        self.window_users_list()

    def window_users_list(self):
        self.lbl_frame_button_list_user = ctk.CTkLabel(self)
        self.lbl_frame_button_list_user.grid(row=0, column=0, padx=10, pady=10, sticky='sw')

        btn_user_new = ctk.CTkButton(self.lbl_frame_button_list_user, text='Nuevo',
                                     fg_color="#1b5e20",
                                     hover_color="#2e7d32")
        btn_user_new.grid(row=0, column=0, padx=5, pady=5)
        btn_user_edit = ctk.CTkButton(self.lbl_frame_button_list_user, text='Modificar')
        btn_user_edit.grid(row=0, column=1, padx=5, pady=5)
        btn_user_delete = ctk.CTkButton(self.lbl_frame_button_list_user, text='Eliminar',
                                        fg_color="#b71c1c",
                                        hover_color="#c62828")
        btn_user_delete.grid(row=0, column=2, padx=5, pady=5)

        self.lbl_frame_search_list_user = ctk.CTkFrame(self)
        self.lbl_frame_search_list_user.grid(row=1, column=0, pady=(0,10), padx=10)

        search_user_entry = ctk.CTkEntry(self.lbl_frame_search_list_user, width=700)
        search_user_entry.grid(row=0, column=0, padx=5, pady=5)

        # ===== Treeview con Scrollbar =====
        self.label_tree_list_user = ctk.CTkLabel(self)
        self.label_tree_list_user.grid(row=2, column=0, sticky='nsew')

        columnas = ("codigo", "nombre", "clave", "rol")
        self.tree_user_list = ttk.Treeview(self.label_tree_list_user, columns=columnas, height=17, show="headings")
        self.tree_user_list.grid(row=0, column=0, sticky="nsew")

        self.tree_user_list.heading("codigo", text="Codigo")
        self.tree_user_list.heading("nombre", text="Nombre")
        self.tree_user_list.heading("clave", text="Clave")
        self.tree_user_list.heading("rol", text="Rol")
        self.tree_user_list['displaycolumns'] = ("codigo", "nombre", "rol")

        self.listar_usuarios()

        # CTkScrollbar para el Treeview
        scrollbar = ctk.CTkScrollbar(self.label_tree_list_user, orientation="vertical", command=self.tree_user_list.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree_user_list.configure(yscrollcommand=scrollbar.set)

    def listar_usuarios(self):
        usuarios = self.controller.listar_usuarios()
        for user in usuarios:
            self.tree_user_list.insert(parent='', index='end',
                                       values=(user.codigo, user.nombre, user.contrasena, user.rol))
