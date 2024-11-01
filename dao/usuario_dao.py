from dao.base_dao import BaseDAO
from models.usuario import Usuario

class UsuarioDAO(BaseDAO):

    def agregar_usuario(self, usuario):
        query = "INSERT INTO usuarios (codigo, nombre, contrasena, rol) VALUES(?,?,?,?)"
        self.execute(query, (usuario.codigo, usuario.nombre, usuario.contrasena, usuario.rol))

    def obtener_usuarios(self):
        query = "SELECT codigo, nombre, contrasena, rol, id FROM usuarios"
        usuarios_data = self.execute(query).fetchall()
        return [Usuario(*data) for data in usuarios_data]

    def obtener_usuario_por_nombre_y_contrasena(self, nombre, contrasena):
        query = "SELECT * FROM usuarios WHERE nombre=? AND contrasena=?"
        usuarios_data = self.execute(query, (nombre, contrasena)).fetchone()
        return [Usuario(*data) for data in usuarios_data]