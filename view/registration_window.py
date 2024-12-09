import threading
import tkinter as tk
from tkinter import ttk, messagebox
from service.lecture_management import LectureManagementService
from service.registration_management import RegistrationService

class RegistrationWindow:
    def __init__(self, root, auto_thread, user_logged_in):
        self.root = root
        self.auto_thread = auto_thread
        self.student = user_logged_in
        self.lecture_management = LectureManagementService()
        self.registration = RegistrationService()
        self.lecture_code = None

    def open_registration_window(self):
        if self.auto_thread is None:
            self.auto_thread = threading.Thread(target=self.lecture_management.auto_increment_subscriptions, daemon=True)
            self.auto_thread.start()

        registration_window = tk.Toplevel(self.root)
        registration_window.title("수강신청")
        tk.Label(registration_window, text="강의 코드:").grid(row=0, column=0, padx=5, pady=5)
        lecture_code_entry = tk.Entry(registration_window)
        self.lecture_code = lecture_code_entry.get()
        lecture_code_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(registration_window, text="수강신청하기", command=self.start_registration).grid(row=1, column=0, columnspan=2,pady=10)

    def start_registration(self,):
        lecture_code = self.lecture_code
        lecture = self.lecture_management.find_lecture_with_code(lecture_code)
        if not lecture:
            messagebox.showerror("오류", f"[ERROR] {lecture_code}: 강의 코드를 찾을 수 없습니다.")
            return

        course_credits = lecture.credit
        current_total_credits = self.student.total_credits

        if current_total_credits + course_credits > 18:
            messagebox.showerror("오류", "수강가능학점을 초과했습니다")
            return

        success, msg = self.lecture_management.add_subscription(lecture_code)
        if not success:
            messagebox.showerror("오류", msg)
            return

        success_sg, msg_sg = self.registration.register_lecture_to_student(self.student, lecture_code)
        if success_sg:
            self.student.total_credits += course_credits
            messagebox.showinfo("성공", msg_sg)
        else:
            self.lecture_management.cancel_subscription(lecture_code)
            messagebox.showerror("오류", msg_sg)

