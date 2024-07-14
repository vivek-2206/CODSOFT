import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(entry_length.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        label_password.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer for the length")

root = tk.Tk()
root.title("Password Generator")

label_length = tk.Label(root, text="Enter length of password:")
label_length.grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

label_password = tk.Label(root, text="Generated Password: ")
label_password.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()