class LoginService:
    def autenticar_usuario(self, username, password):
        """Verifica si el usuario y la contraseña son correctos."""
        return username == "admin" and password == "root"