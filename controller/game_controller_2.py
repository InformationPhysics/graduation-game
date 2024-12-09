import threading
import tkinter as tk
from view.input_view import InputView
from view.output_view import OutputView
from service.log_inout_service import Log_inout
from service.lecture_management import LectureManagementService
from constant.constant import Choice

class GameController:
    def __init__(self):
        self.root = tk.Tk()
        self.view_controller = ViewController(root=self.root)
        self.auth_service = Log_inout()
        self.lecture_service = LectureManagementService()
        self.auto_thread = threading.Thread(target=self.lecture_service.auto_increment_subscriptions, daemon=True)
        self.auto_thread.start()

    def start(self):
        self.root.mainloop()

        while True:
            choice = InputView.get_choice()

            if choice == Choice.LOGIN:
                student_id, password = InputView.get_login_info()
                student = self.auth_service.log_in(student_id, password)
                if student:
                    OutputView.print_login_success(student.name)
                else:
                    OutputView.print_login_failure()

            elif choice == Choice.ADD_LECTURE:
                if not self.auth_service.user_logged_in:
                    OutputView.print_login_failure()
                    continue
                lecture_code = InputView.get_course_code()
                lecture = self.lecture_service.add_subscription(lecture_code)
                if lecture:
                    OutputView.print_registration_success(lecture)
                else:
                    OutputView.print_registration_failure(lecture_code)

            elif choice == Choice.SHOW_LECTURES:
                OutputView.print_lecture_catalog(self.lecture_service.lectures_dict)

            elif choice == Choice.EXIT:
                OutputView.print_exit_message()
                break

            else:
                print("[ERROR] 유효한 선택이 아닙니다.")
