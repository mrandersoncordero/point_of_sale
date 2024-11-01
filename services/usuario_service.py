from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

class UsuarioService:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()

    def agregar_producto(self, codigo, nombre, contrasena, rol):
        """Agregar un usuario a la bd."""
        usuario = Usuario(codigo, nombre, contrasena, rol)
        self.usuario_dao.agregar_usuario(usuario)

    def obtener_usuarios(self):
        """Obtienen todos los usuarios de la bd."""
        return  self.usuario_dao.obtener_usuarios()

    def obtener_usuario_por_nombre_y_contrasena(self, nombre, contrasena):
        """Obtener Usuario por nombre y contrasena."""
        return self.usuario_dao.obtener_usuario_por_nombre_y_contrasena(nombre, contrasena)
