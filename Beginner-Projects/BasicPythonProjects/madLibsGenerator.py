import tkinter as tk
from tkinter import messagebox

def generate_mad_libs():
    noun = nounEntry.get().strip()
    verb = verbEntry.get().strip()
    adjective = adjectiveEntry.get().strip()
    adverb = adverbEntry.get().strip()

    mad_libs = f"The {adjective} {noun} {verb} {adverb}"
    messagebox.showinfo("Mad Libs", mad_libs)

root = tk.Tk()
root.title("Mad Libs Generator")

nounLabel = tk.Label(root, text="Enter a noun:")
nounLabel.pack()
nounEntry = tk.Entry(root, width=50)
nounEntry.pack()

verbLabel = tk.Label(root, text="Enter a verb:")
verbLabel.pack()
verbEntry = tk.Entry(root, width=50)
verbEntry.pack()

adjectiveLabel = tk.Label(root, text="Enter an adjective:")
adjectiveLabel.pack()
adjectiveEntry = tk.Entry(root, width=50)
adjectiveEntry.pack()

adverbLabel = tk.Label(root, text="Enter an adverb:")
adverbLabel.pack()
adverbEntry = tk.Entry(root, width=50)
adverbEntry.pack()

generateButton = tk.Button(root, text="Generate Mad Libs", command=generate_mad_libs)
generateButton.pack()

root.mainloop()