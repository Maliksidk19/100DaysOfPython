from tkinter import *
import math

reps = 0
clock = ""

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#f7f5dd")


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global clock
        clock = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔️"
        label_tick.config(text=marks)


label = Label(text="Timer", bg="#f7f5dd", font=("Courier", 30, "bold"), fg="#9bdeac")
label.grid(row=1, column=2)

canvas = Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
image = PhotoImage(file="Files/tomato.png")
canvas.create_image(100, 112, image=image)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=("Courier", 35, "bold"))
canvas.grid(column=2, row=2)


def start_timer():
    global reps
    reps += 1

    work_sec = 1 * 60
    short_break = 1 * 60
    long_break = 20 * 60

    if reps % 8 == 0:
        count_down(long_break)
        label.config(text="Break", fg="#e7305b")
    elif reps % 2 == 0:
        count_down(short_break)
        label.config(text="Break", fg="#e2979c")
    else:
        count_down(work_sec)
        label.config(text="Work", fg="#9bdeac")


def reset_timer():
    window.after_cancel(clock)
    label_tick.config(text="")
    canvas.itemconfig(timer, text="00:00")
    label.config(text="Timer", fg="#9bdeac")
    global reps
    reps = 0


start_button = Button(text="Start", command=start_timer, font=("Poppins", 10), bg="#068FFF", fg="White", padx=5,
                      border=0, cursor="hand2")
start_button.grid(row=3, column=1)
reset_button = Button(text="Reset", command=reset_timer, font=("Poppins", 10), bg="#068FFF", fg="White", padx=5,
                      border=0, cursor="hand2")
reset_button.grid(row=3, column=3)

label_tick = Label(fg="#9bdeac", font=("Poppins", 20, "bold"), bg="#f7f5dd")
label_tick.grid(column=2, row=4)

window.mainloop()
