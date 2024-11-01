import customtkinter as ctk
from controllers.inventario_controller import InventarioController
from tkinter import  messagebox

class InventarioView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Inventario - Punto de Venta")
        self.geometry("400x300")

        # Configuración de Controlador
        self.controller = InventarioController()

        # Elementos de la Interfaz
        self.nombre_entry = ctk.CTkEntry(self, placeholder_text="Nombre del producto")
        self.cantidad_entry = ctk.CTkEntry(self, placeholder_text="Cantidad")
        self.precio_entry = ctk.CTkEntry(self, placeholder_text="Precio")

        self.agregar_btn = ctk.CTkButton(self, text="Agregar Producto", command=self.agregar_producto)
        self.lista_productos_btn = ctk.CTkButton(self, text="Listar Productos", command=self.listar_productos)
        self.result_label = ctk.CTkLabel(self, text="Productos en inventario: ")

        # Layout
        self.nombre_entry.pack(pady=5)
        self.cantidad_entry.pack(pady=5)
        self.precio_entry.pack(pady=5)
        self.agregar_btn.pack(pady=5)
        self.lista_productos_btn.pack(pady=5)
        self.result_label.pack(pady=5)

    def agregar_producto(self):
        """Método para agregar un producto al inventario"""
        nombre = self.nombre_entry.get()
        cantidad = self.cantidad_entry.get()
        precio = self.precio_entry.get()

        try:
            self.controller.agregar_producto(nombre, int(cantidad), float(precio))
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
            self.nombre_entry.delete(0, 'end')
            self.cantidad_entry.delete(0, 'end')
            self.precio_entry.delete(0, 'end')
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos para cantidad y precio.")

    def listar_productos(self):
        """Lista los productos en inventario."""
        print('listar')
        productos = self.controller.listar_productos()
        texto = "\n".join([f"{p.nombre}: {p.cantidad} unidades, ${p.precio}" for p in productos])
        self.result_label.configure(text=f"Productos en inventario: \n{texto}")