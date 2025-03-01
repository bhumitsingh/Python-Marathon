import tkinter as tk
from PIL import Image, ImageTk
import random
import time
import os

# Create main window
root = tk.Tk()
root.title("Rolling Dice Animation")

# Load dice images
assets_path = os.path.join(os.path.dirname(__file__), "assets")
dice_faces = [ImageTk.PhotoImage(Image.open(os.path.join(assets_path, f"dice{i}.png")).resize((100, 100))) for i in range(1, 7)]

# Label to display dice
dice_label = tk.Label(root, image=dice_faces[0])
dice_label.pack(pady=20)

# Function to animate dice roll
def roll_dice_animation(rolls=10, delay=100):
    if rolls > 0:
        random_face = random.choice(dice_faces)  # Pick a random dice face
        dice_label.config(image=random_face)
        root.after(delay, roll_dice_animation, rolls - 1)  # Call itself with reduced rolls
    else:
        final_face = dice_faces[random.randint(0, 5)]  # Final roll result
        dice_label.config(image=final_face)

# Button to start rolling animation
roll_button = tk.Button(root, text="Roll Dice", command=lambda: roll_dice_animation())
roll_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
