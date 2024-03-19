import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_word = None

def choose_new_word():
    global current_word
    global flip_timer

    window.after_cancel(flip_timer)

    new_word = random.choice(word_translation_dict)
    new_word_french = new_word["French"]
    card_canvas.itemconfig(word_text, text=new_word_french, fill="black")
    card_canvas.itemconfig(language_text, text="French", fill="black")

    current_word = new_word

    flip_timer = window.after(3000, display_english)
    card_canvas.itemconfig(card_canvas_image, image=card_front_image)

def display_english():
    card_canvas.itemconfig(word_text, text=current_word["English"], fill="white")
    card_canvas.itemconfig(language_text, text="English", fill="white")

    card_canvas.itemconfig(card_canvas_image, image=card_back_image)



# --------- UI SETUP ------------ #
window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_canvas = tkinter.Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.grid(row=0, column=0, columnspan=2)
card_front_image = tkinter.PhotoImage(file="images/card_front.png")
card_back_image = tkinter.PhotoImage(file="images/card_back.png")
card_canvas_image = card_canvas.create_image(0,0, anchor="nw", image=card_front_image)

language_text = card_canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = card_canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

right_button_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_button_image, bd=0, highlightthickness=0, command=choose_new_word)
right_button.grid(row=1, column=0)
wrong_button_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_button_image, bd=0, highlightthickness=0, command=display_english)
wrong_button.grid(row=1, column=1)

# --------- Reading word data ---------- #
data = pandas.read_csv("data/french_words.csv")
# Orient just determines how the dictionary is interpreted from the DataFrame.
word_translation_dict = data.to_dict(orient="records")

# Initial Setup #
flip_timer = window.after(3000, display_english)
choose_new_word()

window.mainloop()
