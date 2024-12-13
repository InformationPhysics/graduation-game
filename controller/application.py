import threading
import tkinter as tk
from tkinter import ttk, messagebox
from constants.constant import ErrorMessage

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("수강신청 시스템")
        self.is_logged_in = False
        self.auto_thread = None

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.login_button = tk.Button(self.frame, text="로그인", command=self.open_login_window)
        self.registration_button = tk.Button(self.frame, text="수강신청", command=self.open_registration_window)
        self.class_catalog_button = tk.Button(self.frame, text="강의목록 조회", command=self.show_class_list)
        self.exit_button = tk.Button(self.frame, text="종료", command=self.on_exit)

        self.login_button.grid(row=0, column=0, padx=10, pady=10)
        self.registration_button.grid(row=0, column=1, padx=10, pady=10)
        self.class_catalog_button.grid(row=0, column=2, padx=10, pady=10)
        self.exit_button.grid(row=0, column=3, padx=10, pady=10)


        self.root.quit()
