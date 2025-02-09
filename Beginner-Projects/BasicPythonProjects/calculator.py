import tkinter as tk

def add_numbers():
    num1 = float(entry1.get().strip())
    num2 = float(entry2.get().strip())
    result = num1 + num2
    result_label.config(text="Result: " + str(result))

def subtract_numbers():
    num1 = float(entry1.get().strip())
    num2 = float(entry2.get().strip())
    result = num1 - num2
    result_label.config(text="Result: " + str(result))

def multiply_numbers():
    num1 = float(entry1.get().strip())
    num2 = float(entry2.get().strip())
    result = num1 * num2
    result_label.config(text="Result: " + str(result))

def divide_numbers():
    num1 = float(entry1.get().strip())
    num2 = float(entry2.get().strip())
    result = num1 / num2
    result_label.config(text="Result: " + str(result))

def power_numbers():
    num1 = float(entry1.get().strip())
    power = float(entry3.get().strip())
    result = num1 ** power
    result_label.config(text="Result: " + str(result))

def clear_entries():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Calculator")

entry1__label = tk.Label(root, text="Enter the first number:")
entry1__label.grid(row=0, column=0)
entry1 = tk.Entry(root, width=20)
entry1.grid(row=0, column=1)

entry2__label = tk.Label(root, text="Enter the second number:")
entry2__label.grid(row=1, column=0)
entry2 = tk.Entry(root, width=20)
entry2.grid(row=1, column=1)

entry3__label = tk.Label(root, text="Enter the power:")
entry3__label.grid(row=2, column=0)
entry3 = tk.Entry(root, width=20)
entry3.grid(row=2, column=1)

add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.grid(row=3, column=0)

subtract_button = tk.Button(root, text="Subtract", command=subtract_numbers)
subtract_button.grid(row=3, column=1)

multiply_button = tk.Button(root, text="Multiply", command=multiply_numbers)
multiply_button.grid(row=4, column=0)

divide_button = tk.Button(root, text="Divide", command=divide_numbers)
divide_button.grid(row=4, column=1)

power_button = tk.Button(root, text="Power", command=power_numbers)
power_button.grid(row=5, column=0)

clear_button = tk.Button(root, text="Clear", command=clear_entries)
clear_button.grid(row=5, column=1)


result_label = tk.Label(root, text="", border=2, padx=10, pady=10)
result_label.grid(row=6, column=0, columnspan=2)



root.mainloop()