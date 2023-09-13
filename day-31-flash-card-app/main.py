from tkinter import *
import random
import csv

# -------------------- START CONFIG -------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Helvetica', 36, 'italic')
WORD_FONT = ('Helvetica', 48, 'bold')
window = Tk()
window.title("Flash card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ------------------- MECHANICS ------------------- #
db = None
with open('data/french_words.csv', 'r') as db_file:
    db = db_file.readlines()
timer = None
chosen_example = None


def next_card():
    global timer, db, chosen_example
    if timer:
        window.after_cancel(timer)

    draw_pool = []
    for card_entry in db[1:]:
        card_list = card_entry.split(',')
        if int(card_list[3]) == 0:
            temp = 2
        else:
            temp = int((int(card_list[2]) / int(card_list[3]) - 1) * 10)
        for i in range(temp//2):
            draw_pool.append(card_list)



    chosen_example = random.choice(draw_pool)
    main_canvas.itemconfig(displayed_word, text=chosen_example[0], fill=BACKGROUND_COLOR)
    main_canvas.itemconfig(displayed_language, text='Francais', fill=BACKGROUND_COLOR)
    timer = window.after(3000, flip_card)
    main_canvas.itemconfig(card, image=card_front)


def flip_card():
    translated_word = chosen_example[1]
    main_canvas.itemconfig(displayed_language, text='English', fill='white')
    main_canvas.itemconfig(displayed_word, text=translated_word, fill='white')
    main_canvas.itemconfig(card, image=card_back)


def guessed_right():
    if not main_canvas.itemcget(displayed_word, 'text') == 'FlashCard App':
        chosen_example[2] = str(int(chosen_example[2]) + 1)
        chosen_example[3] = str(int(chosen_example[3]) + 1)+'\n'
        update_data()
    next_card()


def guessed_wrong():
    if not main_canvas.itemcget(displayed_word, 'text') == 'FlashCard App':
        chosen_example[2] = str(int(chosen_example[2]) + 1)
        update_data()
    next_card()


def update_data():
    for index, line in enumerate(db):
        if db[index].split(',')[0] == chosen_example[0]:
            db[index] = ','.join(chosen_example)

    with open('data/french_words.csv', 'w') as db_file:
        db_file.writelines(db)

# ------------------- UI SETUP -------------------- #
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
main_canvas = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=530)
card = main_canvas.create_image(400, 265, image=card_front)
displayed_language = main_canvas.create_text(400, 200, text='welcome to', font=LANGUAGE_FONT)
displayed_word = main_canvas.create_text(400, 250, text='FlashCard App', font=WORD_FONT)
main_canvas.grid(column=0, row=0, columnspan=5)

correct_img = PhotoImage(file='./images/right.png')
correct_button = Button(image=correct_img, highlightthickness=0, command=guessed_right)
correct_button.grid(column=3, row=1)

wrong_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=guessed_wrong)
wrong_button.grid(column=1, row=1)

window.mainloop()
