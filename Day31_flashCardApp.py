from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
data_dict = {}

try:
    data = pd.read_csv('Files/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('Files/french_words.csv')
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def change_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = choice(data_dict)
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(word, text=f"{current_word['French']}", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=f"{current_word['English']}", fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)


def known_words():
    data_dict.remove(current_word)
    new_data = pd.DataFrame(data_dict)
    new_data.to_csv("Files/words_to_learn.csv", index=False)

    change_word()


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.tk.call('source', 'Files/azure.tcl')
window.tk.call('set_theme', 'light')

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file='Files/card_front.png')
card_back_image = PhotoImage(file='Files/card_back.png')
right_image = PhotoImage(file='Files/right.png')
wrong_image = PhotoImage(file='Files/wrong.png')
canvas_image = canvas.create_image(400, 263, image=card_front_image)
lang = canvas.create_text(400, 200, text="", font=("Poppins", 25))
word = canvas.create_text(400, 300, text="", font=("Poppins", 76, "bold"))
canvas.grid(row=1, column=1, columnspan=3)

right_btn = Button(image=right_image, border=0, bg=BACKGROUND_COLOR, cursor='hand2',
                   command=known_words, activebackground=BACKGROUND_COLOR)
right_btn.grid(row=2, column=3)

wrong_btn = Button(image=wrong_image, bg=BACKGROUND_COLOR, border=0, cursor='hand2',
                   command=change_word, activebackground=BACKGROUND_COLOR)
wrong_btn.grid(row=2, column=1)

change_word()

window.mainloop()
