import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Operation Error", "Please select an operation")
            return
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

operation_var = tk.StringVar()
operation_var.set(None)

frame_operations = tk.LabelFrame(root, text="Choose an operation")
frame_operations.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

radio_add = tk.Radiobutton(frame_operations, text="Add", variable=operation_var, value='add')
radio_add.grid(row=0, column=0, padx=10, pady=5)

radio_subtract = tk.Radiobutton(frame_operations, text="Subtract", variable=operation_var, value='subtract')
radio_subtract.grid(row=0, column=1, padx=10, pady=5)

radio_multiply = tk.Radiobutton(frame_operations, text="Multiply", variable=operation_var, value='multiply')
radio_multiply.grid(row=1, column=0, padx=10, pady=5)

radio_divide = tk.Radiobutton(frame_operations, text="Divide", variable=operation_var, value='divide')
radio_divide.grid(row=1, column=1, padx=10, pady=5)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()