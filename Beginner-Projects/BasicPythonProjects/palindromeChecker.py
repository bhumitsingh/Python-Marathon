import tkinter as tk
from tkinter import messagebox

def check_palindrome():
    text = entry.get()  # Get user input
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())  # Remove spaces & punctuation
    if cleaned_text == cleaned_text[::-1]:
        messagebox.showinfo("Result", "It's a palindrome! 🎉")
    else:
        messagebox.showinfo("Result", "Not a palindrome. ❌")

# Create GUI window
root = tk.Tk()
root.title("Palindrome Checker")
root.geometry("300x150")

# Input field
tk.Label(root, text="Enter text:").pack()
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Check Button
check_button = tk.Button(root, text="Check", command=check_palindrome)
check_button.pack(pady=10)

root.mainloop()
