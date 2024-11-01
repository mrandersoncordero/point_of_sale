from services.usuario_service import UsuarioService

class UserController:
    def __init__(self):
        self.usuario_service = UsuarioService()

    def agregar_producto(self, codigo, nombre, contrasena, rol):
        self.usuario_service.agregar_producto(codigo, nombre, contrasena, rol)

    def listar_usuarios(self):
        return self.usuario_service.obtener_usuarios()

    def login(self):
        return self.usuario_service.obtener_usuario_por_nombre_y_contrasena()
