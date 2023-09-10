from tkinter import *
from functools import partial
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#C51605"
GREEN = "#CECE5A"
YELLOW = "#FFE17B"
ORANGE = "#FD8D14"
FONT_NAME = "Andale Mono"
MY_FONT = (FONT_NAME, 35, "bold")
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
count_down_timer = 0
reps = 0
checkmarks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global timer, reps, checkmarks
    window.after_cancel(timer)
    reps = 0
    checkmarks = ""
    canvas.itemconfig(timer_text, text="00:00")
    cm_label.config(text=checkmarks)
    tim_label.config(text="Timer")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps, checkmarks
    reps += 1
    if reps == 1:
        checkmarks = ""
        cm_label.config(text=checkmarks)
    if reps % 2:
        count_down(WORK_MIN)
        tim_label.config(text="Work hard", fg=RED)
    else:
        # break -> add a checkmark and start appropriate timer
        if reps % 8 == 0:
            reps = 0
            count_down(LONG_BREAK_MIN )
            tim_label.config(text="Have a break", fg=GREEN)
        else:
            count_down(SHORT_BREAK_MIN )
            tim_label.config(text="Have a break", fg=ORANGE)

        if checkmarks == "":
            checkmarks = "✓"
        else:
            checkmarks += " ✓"
        cm_label.config(text=checkmarks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(num):
    global timer
    mins, secs = num // 60, num % 60
    global reps
    canvas.itemconfig(timer_text, text=f'{mins:0>2}:{secs:0>2}')
    if num > 0:
        timer = window.after(1000, count_down, num-1)

    else:
        window.after(1000, start_timer)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro App')
window.config(padx=100, pady=50, bg=YELLOW)

# checkmarks
cm_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
cm_label.grid(row=0, column=1)

# canvas
canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 115, image=image)
timer_text = canvas.create_text(100, 140, text='00:00', fill=GREEN, font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# timer label
tim_label = Label(text='Timer', fg=RED, bg=YELLOW, font=(FONT_NAME, 35, "bold"), width=12)
tim_label.grid(row=2, column=1)

# start button
st_button = Button(text="Start", fg=YELLOW, bg=RED, font=(FONT_NAME, 20, 'normal'),
                   borderwidth=0, highlightthickness=0, command=start_timer)
st_button.grid(row=2, column=0)

# restart button
rst_button = Button(text="Reset", fg=YELLOW, bg=RED, font=(FONT_NAME, 20, 'normal'),
                    borderwidth=0, highlightthickness=0, command=reset_timer)
rst_button.grid(row=2, column=2)

window.mainloop()