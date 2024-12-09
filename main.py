from controller.game_controller_2 import GameController
import tkinter as tk

def app():
    game = GameController()
    game.start()

if __name__ == "__main__":
    app()

# TODO 1: 1 회원가입 선택 만들기
# TODO 2: 비회원일때 수강신청 누르면 로그인실패라고 뜬다. 로그인해달라고 바꾸기
# TODO 3: 로그인 - 비밀번호 안보이게 하기