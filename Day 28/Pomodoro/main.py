from cgitb import text
from email.mime import image
from tkinter import *
from urllib import response
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
    canvas.itemconfig(canvas_text, text="00:00")
    time_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    #long reak
    if reps%8 == 0:
        time_label.config(text="Long Break", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    #short break
    elif reps%2 == 0:
        time_label.config(text="Short Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    #work time
    else:
        time_label.config(text="Work Time", fg=GREEN)
        countdown(WORK_MIN * 60)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    

    min = int(count/60)
    sec = count % 60
    if sec == 0 or sec < 10:
        sec = "0"+ str(sec)

    canvas.itemconfig(canvas_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        checks = ""
        for i in range(int(reps/2)):
            checks += "✔"
        check_label.config(text=checks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



#label
time_label = Label(text="Timer")
time_label.config(pady=15 ,font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
time_label.grid(column=1, row=0)

#start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

#reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

#checkmark label
check_label = Label(text="")
check_label.config(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)



window.mainloop()