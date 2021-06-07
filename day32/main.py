from tkinter import *
import pandas
import random

current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_back, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_back, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashyy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_back = canvas.create_image(400,263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Gothic", 40, "italic"))
card_word = canvas.create_text(400, 300, text="Word", font=("Gothic", 60, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
button_no = Button(image=cross_image, highlightthickness=0, command=next_card)
button_no.grid(row=1, column=0)

right_image = PhotoImage(file='images/right.png')
button_yes = Button(image=right_image, highlightthickness=0, command=is_known)
button_yes.grid(row=1, column=1)

next_card()

window.mainloop()
