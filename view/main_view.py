import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.pack(padx=20, pady=20)
        self.login_button = tk.Button(self, text="로그인", command=self.login)
        self.registration_button = tk.Button(self, text="수강신청", command=self.registration)
        self.class_catalog_button = tk.Button(self, text="강의목록 조회", command=self.class_catalog)
        self.exit_button = tk.Button(self, text="종료", command=self.exit)

        self.login_button.grid(row=0, column=0, padx=10, pady=10)
        self.registration_button.grid(row=0, column=1, padx=10, pady=10)
        self.class_catalog_button.grid(row=0, column=2, padx=10, pady=10)
        self.exit_button.grid(row=0, column=3, padx=10, pady=10)

        self.main_controller = None

    def set_controller(self, controller):
        self.main_controller = controller

    def login(self):
        if self.main_controller:
            self.main_controller.open_login_window()

    def registration(self):
        if self.main_controller:
            self.main_controller.open_registration_window()

    def class_catalog(self):
        if self.main_controller:
            self.main_controller.open_class_catalog()

    def exit(self):
        if self.main_controller:
            self.main_controller.open_exit_window()
