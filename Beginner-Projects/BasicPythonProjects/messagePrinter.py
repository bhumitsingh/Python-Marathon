{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Printing input from user in GUI window"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# importing necessary libararies\n",
    "import tkinter as tk\n",
    "from tkinter import messagebox\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function to print the message\n",
    "def printMessage():\n",
    "    message = messageEntry.get().strip()\n",
    "    print(message)\n",
    "    messageEntry.delete(0, tk.END)\n",
    "    messagebox.showinfo(\"Message Printed\", f\"Message: {message}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is Bhumit\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception in Tkinter callback\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\bhumi\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\tkinter\\__init__.py\", line 2068, in __call__\n",
      "    return self.func(*args)\n",
      "           ~~~~~~~~~^^^^^^^\n",
      "  File \"C:\\Users\\bhumi\\AppData\\Local\\Temp\\ipykernel_11588\\4174782256.py\", line 6, in printMessage\n",
      "    messagebox.showinfo(\"Message Printed\", f\"Message: {message}\")\n",
      "    ^^^^^^^^^^\n",
      "NameError: name 'messagebox' is not defined. Did you mean: 'message'?\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception in Tkinter callback\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\bhumi\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\tkinter\\__init__.py\", line 2068, in __call__\n",
      "    return self.func(*args)\n",
      "           ~~~~~~~~~^^^^^^^\n",
      "  File \"C:\\Users\\bhumi\\AppData\\Local\\Temp\\ipykernel_11588\\4174782256.py\", line 6, in printMessage\n",
      "    messagebox.showinfo(\"Message Printed\", f\"Message: {message}\")\n",
      "    ^^^^^^^^^^\n",
      "NameError: name 'messagebox' is not defined. Did you mean: 'message'?\n"
     ]
    }
   ],
   "source": [
    "# creating the main window\n",
    "root = tk.Tk()\n",
    "root.title(\"Message Printer\")\n",
    "\n",
    "# Message Input\n",
    "messageLabel = tk.Label(root, text=\"Enter a message:\")\n",
    "messageLabel.pack()\n",
    "messageEntry = tk.Entry(root, width=50)\n",
    "messageEntry.pack()\n",
    "\n",
    "# Print Button\n",
    "printButton = tk.Button(root, text=\"Print\", command=printMessage)\n",
    "printButton.pack()\n",
    "\n",
    "root.mainloop()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "newenv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
