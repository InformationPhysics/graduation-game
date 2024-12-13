import tkinter as tk
from tkinter import messagebox

class ExitView(tk.Toplevel):
    def __init__(self, main_controller):
        super().__init__()
        self.main_controller = main_controller
        self.title("종료 확인")
        self.geometry("300x150")
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="프로그램을 종료하시겠습니까?", font=("Arial", 12))
        label.pack(pady=20)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        exit_button = tk.Button(button_frame, text="종료", command=self.on_exit)
        exit_button.pack(side=tk.LEFT, padx=10)

        cancel_button = tk.Button(button_frame, text="취소", command=self.on_cancel)
        cancel_button.pack(side=tk.RIGHT, padx=10)

    def on_exit(self):
        self.main_controller.handle_exit()
        self.destroy()

    def on_cancel(self):
        self.destroy()
