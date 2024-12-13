import tkinter as tk
from tkinter import messagebox
from service.login_service import LoginService

class LoginWindow(tk.Toplevel):
    def __init__(self, main_controller):
        super().__init__()
        self.main_controller = main_controller
        self.login_service = LoginService()
        self.id_entry = None
        self.password_entry = None

    def open_login_window(self):
        self.title("로그인")

        tk.Label(self, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="비밀번호:").grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        login_button = tk.Button(self, text="로그인", command=self.get_student_identification)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def get_student_identification(self):
        student = self.main_controller.identify_login_student(self.id_entry.get(), self.password_entry.get())

        if student:
            messagebox.showinfo("로그인 성공", "[SUCCESS] 로그인 성공.")
            self.destroy()
        else:
            messagebox.showerror("로그인 실패", "아이디 또는 비밀번호를 확인하세요.")