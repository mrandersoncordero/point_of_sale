from dao.base_dao import BaseDAO
from models.producto import Producto

class ProductoDAO(BaseDAO):
    def agregar_producto(self, producto):
        query = "INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)"
        self.execute(query, (producto.nombre, producto.cantidad, producto.precio))

    def obtener_productos(self):
        query = "SELECT id, nombre, cantidad, precio FROM productos"
        productos_data = self.execute(query).fetchall()
        return [Producto(*data) for data in productos_data]