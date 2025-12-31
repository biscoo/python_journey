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
mark = ""
timer = None
timer_running = False   # <<< NEW FLAG

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer_running, mark
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f'{WORK_MIN}:00')
    check.config(text="  ")
    reps = 0
    mark = ""
    timer_running = False   # <<< RESET FLAG

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, timer_running

    # <<< PREVENT MULTIPLE TIMERS
    if timer_running:
        return
    timer_running = True

    reps += 1
    if reps in [2, 4, 6]:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)

    elif reps in [1, 3, 5, 7]:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

    elif reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN ------------------------------- #
def count_down(count):
    global timer, mark, reps, timer_running

    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps < 8:
            if reps % 2 == 0:
                mark += "✔"
                check.config(text=mark)
            start_timer()
        else:
            mark += "✔"
            check.config(text=mark)
            timer_label.config(text="Pomodoro")
            timer_running = False   # <<< ALLOW START AGAIN

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=300, height=300)
window.config(pady=20, padx=20, background='#FFDEB9')

canvas = Canvas(width=250, height=250, bg='#FFDEB9', highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(125, 125, image=image)
timer_text = canvas.create_text(125, 145, text=f'{WORK_MIN}:00', font=(FONT_NAME, 35, 'bold'), fill='white')
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg='#FFDEB9')
timer_label.grid(column=1, row=0)

start = Button(text='Start', font=(FONT_NAME, 9, 'bold'), command=start_timer)
start.grid(column=0, row=2)

reset = Button(text='Reset', font=(FONT_NAME, 9, 'bold'), command=reset_timer)
reset.grid(column=2, row=2)

check = Label(text="  ", fg=GREEN, bg='#FFDEB9', font=(FONT_NAME, 15, 'normal'))
check.grid(column=1, row=3)

window.mainloop()
