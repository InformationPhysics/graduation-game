import tkinter as tk
from tkinter import messagebox

class RegistrationView(tk.Toplevel):
    def __init__(self, main_controller):
        super().__init__()
        self.main_controller = main_controller
        self.lecture_code_entry = None

    def open_registration_window(self):
        self.title("수강 신청")
        self.geometry("400x200")

        tk.Label(self, text="강의 코드:").grid(row=0, column=0, padx=5, pady=5)
        self.lecture_code_entry = tk.Entry(self)
        self.lecture_code_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self, text="수강 신청하기", command=self.on_register_click).grid(row=1, column=0, columnspan=2, pady=10)

    def on_register_click(self):
        lecture_code = self.lecture_code_entry.get()
        success, message = self.main_controller.start_registration(lecture_code)

        if success:
            messagebox.showinfo("성공", message)
        else:
            messagebox.showerror("오류", message)
