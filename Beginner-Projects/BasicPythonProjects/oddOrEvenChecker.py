import tkinter as tk
from tkinter import messagebox

def check_odd_even():
    try:
        num = int(entry.get())
        if num % 2 == 0:
            messagebox.showinfo("Result", "It's an even number.")
        else:
            messagebox.showinfo("Result", "It's an odd number.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create GUI window
root = tk.Tk()
root.title("Odd or Even Checker")
root.geometry("300x150")

# Input field
tk.Label(root, text="Enter a number:").pack()
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Check Button
tk.Button(root, text="Check", command=check_odd_even).pack(pady=5)

root.mainloop()