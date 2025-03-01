import tkinter as tk
from tkinter import scrolledtext

def count_words():
    text = text_area.get("1.0", tk.END)  # Get text from textbox
    words = text.split()
    word_count_label.config(text=f"Word Count: {len(words)}")  # Update label

# Create GUI window
root = tk.Tk()
root.title("Word Counter")
root.geometry("400x300")

# Text Area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(pady=10)

# Count Button
count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack()

# Word Count Label
word_count_label = tk.Label(root, text="Word Count: 0", font=("Arial", 14))
word_count_label.pack(pady=10)

root.mainloop()
