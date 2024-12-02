from model.student import Student

class AuthenticationService:
    file_name = "resource/student_information.md"
    students = {}

    def __init__(self):
        self.logged_in_user = None

    def load_student_information(self):
        reader = open(self.file_name, "rt")
        line = reader.readline()
        while True:
            if not line:
                break



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
