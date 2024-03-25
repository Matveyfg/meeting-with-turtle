import tkinter as tk

class ClickerGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Clicker Game")

        self.label_player1 = tk.Label(self.master, text="Игрок 1: 0")
        self.label_player1.pack()

        self.label_player2 = tk.Label(self.master, text="Игрок 2: 0")
        self.label_player2.pack()

        self.master.bind("<Button-1>", self.click_player1)
        self.master.bind("<KeyPress-s>", self.click_player2)

        self.count_player1 = 0
        self.count_player2 = 0

    def click_player1(self, event):
        self.count_player1 += 1
        self.label_player1.config(text="Игрок 1: " + str(self.count_player1))

    def click_player2(self, event):
        self.count_player2 += 1
        self.label_player2.config(text="Игрок 2: " + str(self.count_player2))

root = tk.Tk()
game = ClickerGame(root)
root.mainloop()
