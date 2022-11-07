from email.mime import image
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
random_word = None

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#----------------------Acessing Data--------------------#
try:
    french_word_data = pandas.read_csv("data/words_to_learn.csv")
    french_dict = french_word_data.to_dict(orient="records")
except FileNotFoundError:
    french_word_data = pandas.read_csv("data/french_words.csv")
    french_dict = french_word_data.to_dict(orient="records")


def nextcard():
    global random_word
    flash_card.itemconfig(flash_img, image=front_img)
    random_word = random.choice(french_dict)
    flash_card.itemconfig(lang_text, text="French")
    flash_card.itemconfig(word_text, text=random_word["French"])
    global timer
    timer = window.after(3000, show_answer)


def nextcard_correct():

    french_dict.remove(random_word)
    new_data = pandas.DataFrame(french_dict)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    nextcard()

def nextcard_wrong():
    nextcard()

#anser
def show_answer():
    global timer
    global random_word
    flash_card.itemconfig(flash_img, image=back_img)
    flash_card.itemconfig(lang_text, text="English")
    flash_card.itemconfig(word_text, text=random_word["English"])
    window.after_cancel(timer)


#----------------------UI DESIGN--------------------#

#canvas
flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
flash_img = flash_card.create_image(400, 254, image=front_img)
lang_text = flash_card.create_text(400, 150, text="Language", fill="black", font=("Ariel", 40, "italic"))
word_text = flash_card.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))

back_img = PhotoImage(file="images/card_back.png")
# flash_card.create_image(400, 254, image=back_img)


flash_card.grid(column=0, row=0, columnspan=2, rowspan=2)


#button
img_wro = PhotoImage(file="images/wrong.png")
but_wrong = Button(image=img_wro, highlightthickness=0, command=nextcard_wrong)
but_wrong.grid(column=0, row=2)

img_rig = PhotoImage(file="images/right.png")
but_right = Button(image=img_rig, highlightthickness=0, command=nextcard_correct)
but_right.grid(column=1, row=2)

nextcard()

window.mainloop()

