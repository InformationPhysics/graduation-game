import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.pack(padx=20, pady=20)

        self.login_button = tk.Button(self, text="로그인", command=self.open_login_window)
        self.registration_button = tk.Button(self, text="수강신청", command=self.open_registration_window)
        self.class_catalog_button = tk.Button(self, text="강의목록 조회", command=self.show_class_list)
        self.exit_button = tk.Button(self, text="종료", command=self.on_exit)

        self.login_button.grid(row=0, column=0, padx=10, pady=10)
        self.registration_button.grid(row=0, column=1, padx=10, pady=10)
        self.class_catalog_button.grid(row=0, column=2, padx=10, pady=10)
        self.exit_button.grid(row=0, column=3, padx=10, pady=10)

        self.main_controller = None

    def set_controller(self, controller):
        self.main_controller = controller

    def open_login_window(self):
        if self.main_controller:
            self.main_controller.login()

    def open_registration_window(self):
        if self.main_controller:
            self.main_controller.register()

    def show_class_list(self):
        if self.main_controller:
            self.main_controller.show_class_list()

    def on_exit(self):
        if self.main_controller:
            self.main_controller.exit()
