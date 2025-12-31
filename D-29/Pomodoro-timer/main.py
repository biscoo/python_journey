from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
marks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, marks

    window.after_cancel(timer)
    reps = 0
    marks = ""

    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"{WORK_MIN}:00")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM --------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps in [1, 3, 5, 7]:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN, 0)

    elif reps in [2, 4, 6]:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN, 0)

    elif reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN, 0)


# ---------------------------- COUNTDOWN MECHANISM ----------------------- #
def count_down(minutes, seconds):
    global timer, marks

    time_string = f"{minutes}:{seconds:02}"
    canvas.itemconfig(timer_text, text=time_string)

    if minutes == 0 and seconds == 0:
        if reps < 8:
            if reps % 2 == 0:
                marks += "✔"
                check_label.config(text=marks)
            start_timer()
        else:
            timer_label.config(text="Pomodoro")
        return

    if seconds > 0:
        seconds -= 1
    else:
        minutes -= 1
        seconds = 59

    timer = window.after(1000, count_down, minutes, seconds)


# ---------------------------- UI SETUP ---------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=20, pady=20, bg="#FFDEB9")

canvas = Canvas(width=250, height=250, bg="#FFDEB9", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image=tomato_img)
timer_text = canvas.create_text(
    125, 145, text=f"{WORK_MIN}:00", fill="white",
    font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

timer_label = Label(
    text="Timer", fg=GREEN, bg="#FFDEB9",
    font=(FONT_NAME, 40, "bold")
)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 9, "bold"),
                      command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 9, "bold"),
                      command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(text="", fg=GREEN, bg="#FFDEB9",
                    font=(FONT_NAME, 15))
check_label.grid(column=1, row=3)

window.mainloop()
