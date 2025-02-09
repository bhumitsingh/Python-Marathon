import random
import tkinter as tk
from tkinter import messagebox

number = random.randint(1, 100)

def guess_number():
    guess = int(entry.get().strip())
    if guess == number:
        messagebox.showinfo("Congratulations", "You guessed the number!")
    elif guess < number:
        messagebox.showinfo("Too low", "Your guess is too low.")
    else:
        messagebox.showinfo("Too high", "Your guess is too high.")


root = tk.Tk()
root.title("Guess the Number")

label = tk.Label(root, text="Enter a number between 1 and 100:")
label.pack()

entry = tk.Entry(root, width=20)
entry.pack()

button = tk.Button(root, text="Guess", command=guess_number)
button.pack()

root.mainloop()