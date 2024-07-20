import tkinter as tk
from tkinter import messagebox

def perform_operation(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            result = 'Invalid operation'
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widgets for the numbers
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create buttons for each operation
button_add = tk.Button(root, text="+", command=lambda: perform_operation('+'))
button_add.pack(side=tk.LEFT, padx=5, pady=5)

button_subtract = tk.Button(root, text="-", command=lambda: perform_operation('-'))
button_subtract.pack(side=tk.LEFT, padx=5, pady=5)

button_multiply = tk.Button(root, text="*", command=lambda: perform_operation('*'))
button_multiply.pack(side=tk.LEFT, padx=5, pady=5)

button_divide = tk.Button(root, text="/", command=lambda: perform_operation('/'))
button_divide.pack(side=tk.LEFT, padx=5, pady=5)

# Create a label to display the result
label_result = tk.Label(root, text="Result: ")
label_result.pack()

# Start the GUI event loop
root.mainloop()









