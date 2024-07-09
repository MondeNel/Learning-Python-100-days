from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
# Define color constants for UI elements
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Define font and timer intervals (in minutes)
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 5  # Setting both short and long breaks to 5 minutes

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """
    Resets the timer, stopping any ongoing countdown, resetting the timer display to 00:00, 
    updating the timer label, and clearing the check marks.
    """
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    window.config(bg=YELLOW)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Starts the timer for either a work session or break based on the number of repetitions completed.
    Updates the timer label accordingly.
    """
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        window.title("Break Time!")
        window.config(bg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
        window.title("Break Time!")
        window.config(bg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        window.title("Work Time!")
        window.config(bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """
    Handles the countdown mechanism. Updates the timer text on the canvas every second.
    Calls itself recursively until the countdown reaches zero, then starts the next timer phase.
    """
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# Set up the main window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create and place the timer label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

# Create and place the canvas with the tomato image and timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Create and place the Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Create and place the Reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Create and place the check marks label
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# Initialize global variables
reps = 0
timer = None

# Keep the window open and start the Tkinter event loop
window.mainloop()
