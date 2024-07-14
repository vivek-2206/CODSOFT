import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.bg_color = "black" 
        self.fg_color = "white"  
        self.button_bg_color = "white"  
        self.button_fg_color = "black"  
        self.entry_bg_color = "white"  
        self.entry_fg_color = "black"  
        self.listbox_bg_color = "white"  
        self.listbox_fg_color = "black"  
        self.root.configure(bg=self.bg_color)

        # Label and Entry box to add new tasks
        self.label = tk.Label(root, text="Enter the Task:", bg=self.bg_color, fg=self.fg_color, font=("Helvetica", 10, "bold"))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.task_entry = tk.Entry(root, width=40, bg=self.entry_bg_color, fg=self.entry_fg_color)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, width=50, height=10, bg=self.listbox_bg_color, fg=self.listbox_fg_color)
        self.task_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Buttons to add, update, and delete tasks
        button_font = ("Helvetica", 10, "bold")

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg=self.button_bg_color, fg=self.button_fg_color, width=20, font=button_font)
        self.add_button.grid(row=1, column=0, padx=(10, 5), pady=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task, bg=self.button_bg_color, fg=self.button_fg_color, width=20, font=button_font)
        self.update_button.grid(row=1, column=1, padx=5, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg=self.button_bg_color, fg=self.button_fg_color, width=20, font=button_font)
        self.delete_button.grid(row=1, column=2, padx=(5, 10), pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_task_index)
            new_task = simpledialog.askstring("Update Task", "Update the task:", initialvalue=selected_task)
            if new_task:
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, new_task)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()