from dao.producto_dao import ProductoDAO
from models.producto import Producto

class InventarioService:
    def __init__(self):
        self.producto_dao = ProductoDAO()

    def agregar_producto(self, nombre, cantidad, precio):
        """Agregar un producto al inventario."""
        producto = Producto(nombre, cantidad, precio)
        self.producto_dao.agregar_producto(producto)

    def obtener_inventario(self):
        """Obtiene todos los productos del inventario."""
        return  self.producto_dao.obtener_productos()