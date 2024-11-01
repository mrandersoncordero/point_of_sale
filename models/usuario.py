class Usuario:
    def __init__(self, codigo, nombre, contrasena, rol, id=None):
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.contrasena = contrasena
        self.rol = rol

    def __str__(self):
        return f'Usuario => id: {self.id}, codigo: {self.codigo}, nombre: {self.nombre}, rol: {self.rol}'
