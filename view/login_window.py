import tkinter as tk
from tkinter import messagebox
from service.log_inout_service import Log_inout
from constant.constant import ErrorMessage

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.log_service = Log_inout()
        self.user_logged_in = None

    def open_login_window(self):
        login_window = tk.Toplevel(self.root)
        login_window.title("로그인")
        tk.Label(login_window, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(login_window, text="비밀번호:").grid(row=1, column=0, padx=5, pady=5)

        id_entry = tk.Entry(login_window)
        password_entry = tk.Entry(login_window, show="*")
        id_entry.grid(row=0, column=1, padx=5, pady=5)
        password_entry.grid(row=1, column=1, padx=5, pady=5)

        def do_login():
            student = self.log_service.log_in(id_entry.get(), password_entry.get())
            self.user_logged_in = student
            if student:
                self.is_logged_in = True
                messagebox.showinfo("로그인 성공", "[SUCCESS] 로그인 성공.")
                login_window.destroy()
            elif student == ErrorMessage.LOGIN_ID_ERROR:
                messagebox.showerror("오류", ErrorMessage.LOGIN_ID_ERROR)
            elif student == ErrorMessage.LOGIN_PASSWORD_ERROR:
                messagebox.showerror("오류", ErrorMessage.LOGIN_PASSWORD_ERROR)

        login_button = tk.Button(login_window, text="로그인", command=do_login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        return