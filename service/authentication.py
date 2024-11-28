from model.student import Student


class AuthenticationService:
    def __init__(self):
        self.logged_in_user = None
        self.users = {
            "admin": Student(0000, 0000, "admin", "admin"),
        }

    def login(self, student_number, password):

        user = self.users.get()
        if user and user["password"] == password:
            self.logged_in_user =
            return user["name"]
        return None

    def logout(self):
        self.logged_in_user = None

    def is_logged_in(self):
        return self.logged_in_user is not None
