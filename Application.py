import tkinter as tk
from controller.main_controller import MainController
from view.main_view import MainView

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("수강신청 시스템")

        main_view = MainView(self)
        main_controller = MainController(main_view)
        main_view.set_controller(main_controller)

if __name__ == "__main__":
    App().mainloop()
