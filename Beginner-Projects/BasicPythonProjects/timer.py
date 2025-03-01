import tkinter as tk
from tkinter import messagebox
import time

def start_timer():
    try:
        total_seconds = int(entry_min.get()) * 60 + int(entry_sec.get())
        if total_seconds <= 0:
            messagebox.showerror("Invalid Time", "Please enter a positive time.")
            return
        countdown(total_seconds)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for minutes and seconds.")

def countdown(seconds):
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        timer_label.after(1000, countdown, seconds - 1)
    else:
        timer_label.config(text="Time's up!⏰")
        messagebox.showinfo("Countdown Finished", "Time's up!")

# Create main window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x200")

# Label and entry for minutes
label_min = tk.Label(root, text="Minutes:").pack()
entry_min = tk.Entry(root)
entry_min.pack()

# Label and entry for seconds
label_sec = tk.Label(root, text="Seconds:").pack()
entry_sec = tk.Entry(root)
entry_sec.pack()

# Button to start timer
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=20)

# Label to display timer
timer_label = tk.Label(root, text="00:00", font=("Arial", 24))
timer_label.pack()

root.mainloop()
