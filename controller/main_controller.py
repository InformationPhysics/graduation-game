from view.login_view import LoginView
from view.registration_view import RegistrationView
from view.lecture_table_view import LectureTableView
from view.exit_view import ExitView
from service.login_service import LoginService
from controller.registration_controller import RegistrationController
from model.student import Student
class MainController:
    def __init__(self, main_view):
        self.main_view = main_view

        self.login_window = None
        self.login_service = LoginService()
        self.current_user = None

        self.registration_view = None
        self.registration_controller = RegistrationController()

        self.lecture_table_view = None
        self.exit_view = None

    # 로그인
    def open_login_window(self):
        if not self.login_window or not self.login_window.winfo_exists(): #tk메서드: 존재 1 반환
            self.login_window = LoginView(self)
            self.login_window.open_login_window()
        else:
            self.login_window.lift() # 창 있으면 최상위로 띄우기

    def identify_login_student(self, student_id, password):
        student = self.login_service.login(student_id, password)
        if student:
            self.current_user = student
            return student
        return None

    # 수강신청
    def open_registration_window(self):
        if not self.registration_view or not self.registration_view.winfo_exists():
            self.registration_view = RegistrationView(self)
            self.registration_view.open_registration_window()

        self.registration_controller.start_auto_increment()

    def start_registration(self, lecture_code):
        return self.registration_controller.register_lecture(self.current_user, lecture_code)

    def get_all_lectures(self):
        return self.registration_controller.get_all_lectures()

    # 강의 조회
    def open_class_catalog(self):
        if not self.lecture_table_view or not self.lecture_table_view.winfo_exists():
            self.lecture_table_view = LectureTableView(self)
    # 종료
    def open_exit_window(self):
        if not self.exit_view or not self.exit_view.winfo_exists():
            self.exit_view = ExitView(self)
        else:
            self.exit_view.lift()

    def handle_exit(self):
        self.main_view.quit()
