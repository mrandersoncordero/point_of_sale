from services.login_service import LoginService

class LoginController:
    def __init__(self):
        self.login_service = LoginService()

    def autenticar(self, username, password):
        """Llama al servicio de autenticación y retorna el resultado."""
        return self.login_service.autenticar_usuario(username, password)