from tkinter import *
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_indices = listbox.curselection()
    if selected_task_indices:
        selected_task_index = selected_task_indices[0]
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")


root = Tk()
root.title("To-Do List")

frame = Frame(root)
frame.pack(padx=10, pady=10)

task_entry = Entry(frame, width=40)
task_entry.grid(row=0, column=0, padx=5, pady=5)

add_button = Button(frame, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)

remove_button = Button(frame, text="Remove Task", width=12, command=remove_task)
remove_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

listbox = Listbox(frame, width=50)
listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
