from view.login_window import LoginWindow
from service.login_service import LoginService

class MainController:
    def __init__(self, main_view):
        self.main_view = main_view
        self.login_window = None

        self.login_service = LoginService()
        self.current_user = None

    def login(self):
        if not self.login_window or not self.login_window.winfo_exists(): #tk메서드: 존재 1 반환
            self.login_window = LoginWindow(self)
            self.login_window.open_login_window()
        else:
            self.login_window.lift() # 창 있으면 최상위로 띄우기

    def identify_login_student(self, student_id, password):
        student = self.login_service.login(student_id, password)
        if student:
            self.current_user = student
            return student
        return None

    def register(self):
        pass

    def show_class_list(self):
        pass

    def exit(self):
        pass
