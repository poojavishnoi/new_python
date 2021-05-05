from tkinter import *
import math
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    label.config(text="TIMER")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="break", bg=YELLOW, fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="break", bg=YELLOW, fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="work", bg=YELLOW, fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks = f"{work_sessions} Session completed"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=205, height=225, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
timer_txt = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME,  30, "bold"))


label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label.grid(row=1, column=2)

button1 = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
button1.grid(row=3, column=1)

button2 = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
button2.grid(row=3, column=3)

check_marks = Label(text="" ,bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=2)

canvas.grid(row=2, column=2)


window.mainloop()