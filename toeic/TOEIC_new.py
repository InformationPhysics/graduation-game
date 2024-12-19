import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import base64
from io import BytesIO

class TOEIC:
    def __init__(self):
        # Base64로 인코딩된 이미지 데이터
        from toeic.image_texted import encoded_image
        image_data = encoded_image

        # Base64 문자열을 이미지로 디코딩
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))

        self.root = tk.Tk()
        self.root.title("OMR Viewer")

        # 이미지 프레임 생성
        image_frame = tk.Frame(self.root)
        image_frame.pack(side='left')

        photo = ImageTk.PhotoImage(image)

        canvas = tk.Canvas(image_frame, width=photo.width(), height=photo.height())
        canvas.pack()
        canvas.create_image(0, 0, anchor='nw', image=photo)

        # 이하 코드는 원본과 동일
        omr_frame = tk.Frame(self.root)
        omr_frame.pack(side='right', padx=20)

        questions = [101, 102, 103, 104]
        options = ['A', 'B', 'C', 'D']
        correct_answers = ['D', 'A', 'B', 'C']
        user_answers = {}

        tk.Label(omr_frame, text="정답을 선택하세요").grid(row=0, column=0, columnspan=5, pady=10)

        for i, question in enumerate(questions):
            tk.Label(omr_frame, text=f"{question}번").grid(row=i + 1, column=0, padx=10, pady=5)
            user_answers[question] = tk.StringVar(value='')

            for j, option in enumerate(options):
                tk.Radiobutton(
                    omr_frame, text=option, variable=user_answers[question], value=option
                ).grid(row=i + 1, column=j + 1, padx=5)

        def submit_answers():
            correct_count = 0
            for q_index, question in enumerate(questions):
                user_answer = user_answers[question].get()
                if user_answer == correct_answers[q_index]:
                    correct_count += 1

            if correct_count >= 3:
                T_state = 0
                with open('state.txt', 'w') as f:
                    f.write(f'state=={T_state}')
                messagebox.showinfo("Result", "정답입니다!")
            else:
                T_state = 1
                with open('state.txt', 'w') as f:
                    f.write(f'state=={T_state}')
                messagebox.showinfo("Result", "실패하셨습니다.")

            self.root.destroy()

        submit_button = tk.Button(omr_frame, text="제출", command=submit_answers)
        submit_button.grid(row=len(questions) + 1, column=0, columnspan=5, pady=10)

        self.root.mainloop()