from tkinter import *
clicks = 0

def click_button():
    global clicks
    clicks += 1
    button.config(text="Нажатий {}".format(clicks))

root = Tk()
root.geometry("300x100")

button = Button(text="Нажатий 0", bg="#555", fg="#ccc", font=16, command=click_button)
button.place(relx=.5, rely=.5, anchor="c")
root.mainloop()
