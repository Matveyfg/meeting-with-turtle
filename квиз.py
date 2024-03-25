import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Простая викторина")

def show_result():
    messagebox.showinfo("Результат", "Правильных ответов: 1 из 1")


def check_answer_two():
    selected_answer = var.get()
    if selected_answer == "Перун":
        messagebox.showinfo("Правильно", "Верно!")
    else:
        messagebox.showinfo("Неверно", "Попробуйте еще раз.")

question_label = tk.Label(root, text="Главный бог славян был?")
question_label.pack()

var = tk.StringVar(value="Велес")
radio_btn1 = tk.Radiobutton(root, text="Перун", variable=var, value="Перун")
radio_btn1.pack()

radio_btn2 = tk.Radiobutton(root, text="Велес", variable=var, value="Велес")
radio_btn2.pack()
check_button = tk.Button(root, text="Проверить", command=check_answer_two)
check_button.pack()

result_button = tk.Button(root, text="Показать результат", command=show_result)
result_button.pack()

root.mainloop()