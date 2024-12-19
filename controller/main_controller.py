from pyexpat.errors import messages

from view.login_view import LoginView
from view.registration_view import RegistrationView
from view.lecture_table_view import LectureTableView
from view.exit_view import ExitView
from view.test_view import TestView
from view.talking_view import *
from service.login_service import LoginService
from service.lecture_management import LectureManagementService
from service.test_management import TestManagementService
from controller.registration_controller import RegistrationController
from controller.test_controller import TestController

class MainController:
    def __init__(self, main_view):
        self.main_view = main_view

        self.login_window = None
        self.login_service = LoginService()
        self.current_user = None

        self.registration_view = None
        self.lecture_management = LectureManagementService()
        self.registration_controller = RegistrationController(self.lecture_management, self)

        self.lecture_table_view = None
        self.exit_view = None

        self.test_view = None
        self.test_management = TestManagementService(self.lecture_management)
        self.test_controller = None

    # 시나리오
    def first_scenario(self):
        Talk1()

    def second_scenario(self):
        Talk2()

    def third_scenario(self):
        Talk3()

    def fourth_scenario(self):
        Talk4()

    # 로그인
    def open_login_window(self):
        if not self.login_window or not self.login_window.winfo_exists(): #tk메서드: 존재 1 반환
            self.login_window = LoginView(self)
            self.login_window.open_login_window()
        else:
            self.login_window.lift() # 창 있으면 최상위로 띄우기

    def identify_login_student(self, student_id, password):
        self.current_user = self.login_service.get_login_student(student_id, password)
        return self.current_user

    # 수강 신청
    def open_registration_window(self):
        if not self.registration_view or not self.registration_view.winfo_exists():
            self.registration_view = RegistrationView(self)
            self.registration_view.open_registration_window()
            self.registration_controller.start_auto_increment() # 수강인원 자동 증가
            self.main_view.enable_test_button() # 테스트 버튼 활성화

    def start_registration(self, lecture_code):
        return self.registration_controller.register_lecture_with_user(self.current_user, lecture_code)

    # 강의 조회
    def open_class_catalog(self):
        if not self.lecture_table_view or not self.lecture_table_view.winfo_exists():
            self.lecture_table_view = LectureTableView(self)

    def get_all_lectures(self):
        return self.lecture_management.get_all_lectures()

    # 종료
    def open_exit_window(self):
        if not self.exit_view or not self.exit_view.winfo_exists():
            self.exit_view = ExitView(self)
        else:
            self.exit_view.lift()

    def handle_exit(self):
        self.main_view.quit()

    # 시험
    def open_test_window(self):
        self.test_view = TestView(self.main_view.master, self)
        self.test_view.pack()
        self.test_controller = TestController(self, self.test_management)
        self.main_view.pack_forget()  # MainView를 숨김

    def get_lecture_test(self):
        return self.test_controller.get_registered_exams()

    def submit_answer(self, user_answer):
        valid, message = self.test_controller.submit_answer(user_answer)
        return valid, message

    def get_exam_result(self):
        return self.test_controller.finalize_exam()

    # 유저 정보 갱신
    def update_user_info(self, updated_user):
        self.current_user = updated_user
