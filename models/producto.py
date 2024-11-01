class Producto:
    def __init__(self, nombre, cantidad, precio, id=None):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio