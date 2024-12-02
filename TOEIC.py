import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def main():
    image_path = '/Users/kim-shineui/Downloads/TOEIC.jpeg'
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print("Image not found at path:", image_path)
        return

    root = tk.Tk()
    root.title("OMR Viewer")

    # 이미지 프레임 생성
    image_frame = tk.Frame(root)
    image_frame.pack(side='left')

    photo = ImageTk.PhotoImage(image)

    canvas = tk.Canvas(image_frame, width=photo.width(), height=photo.height())
    canvas.pack()
    canvas.create_image(0, 0, anchor='nw', image=photo)

    # OMR 입력 프레임 생성
    omr_frame = tk.Frame(root)
    omr_frame.pack(side='right', padx=20)

    questions = [101, 102, 103, 104]
    options = ['A', 'B', 'C', 'D']
    correct_answers = ['D', 'A', 'B', 'C']
    user_answers = {}

    tk.Label(omr_frame, text="정답을 선택하세요").grid(row=0, column=0, columnspan=5, pady=10)

    for i, question in enumerate(questions):
        tk.Label(omr_frame, text=f"{question}번").grid(row=i + 1, column=0, padx=10, pady=5)
        user_answers[question] = tk.StringVar(value='')  # 기본값을 빈 문자열로 설정

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

        root.destroy()

    submit_button = tk.Button(omr_frame, text="제출", command=submit_answers)
    submit_button.grid(row=len(questions) + 1, column=0, columnspan=5, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
