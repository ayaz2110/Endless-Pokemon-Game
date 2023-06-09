from tkinter import * 
from PIL import ImageTk, Image
root = Tk()

root.title("Endeless Dice Game")
root.geometry("600x400")

root.configure(background = "yellow2")

img = ImageTk.PhotoImage(Image.open("data:image/jpeg;base64,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"))

player1 = Label(root, text = "Player 1", bg = "royal blue", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "royal blue", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score_label = Label(root, bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root, bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_dice_label = Label(root, bg = "chocolate1", fg = "white")
random_dice_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()

