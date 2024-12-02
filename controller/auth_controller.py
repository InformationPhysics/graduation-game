from service.authentication import *
from view.input_view import InputView

class AuthController:
    auth_service = AuthenticationService()

    def sign_up(self):
        student = InputView.print_sign_up()
