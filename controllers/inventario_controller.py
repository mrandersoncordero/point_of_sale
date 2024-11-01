from services.inventario_service import InventarioService

class InventarioController:
    def __init__(self):
        self.inventario_service = InventarioService()

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un producto usando el servicio de inventario."""
        self.inventario_service.agregar_producto(nombre, cantidad, precio)

    def listar_productos(self):
        """Obtiene el inventario actual."""
        return self.inventario_service.obtener_inventario()