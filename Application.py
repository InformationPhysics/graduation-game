import tkinter as tk
from controller.main_controller import MainController
from view.main_view import MainView

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("졸업게임 2024")

        main_view = MainView(self)
        main_controller = MainController(main_view)
        main_view.set_controller(main_controller)
        main_controller.first_scenario()

if __name__ == "__main__":
    App().mainloop()

