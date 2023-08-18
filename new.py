import tkinter as tk
import re

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        tasks.append(task)
        task_entry.delete(0, tk.END)

def mark_done():
    selected_index = tasks_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        tasks[index] = tasks[index] + " (Done)"
        tasks_listbox.delete(index)
        tasks_listbox.insert(index, tasks[index])


def remove_item():
    selected_index = tasks_listbox.curselection()
    if selected_index:
     index = selected_index[0]
     tasks_listbox.delete(index)
     

def remove_done():
    selected_index = tasks_listbox.curselection()
    if selected_index:
     index = selected_index[0]
     teststr = ""
     teststr = tasks[index]
     teststr = teststr.replace(" (Done)", "")
     tasks[index] = teststr
     tasks_listbox.delete(index)
     tasks_listbox.insert(index, tasks[index])

def save_to_file():
    with open("items.txt", "w") as file:
        items = tasks_listbox.get(0, tk.END)
        for item in items:
            file.write(item + "\n")

def load_from_file():
    tasks_listbox.delete(0, tk.END)  # Clear existing items
    try:
        with open("items.txt", "r") as file:
            items = file.read().splitlines()
            for item in items:
                tasks_listbox.insert(tk.END, item)
    except FileNotFoundError:
        pass  # If the file doesn't exist, do nothing


# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("600x900")

# Create widgets
task_label = tk.Label(root, text="Enter Task:")
task_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Task", command=add_task)
mark_done_button = tk.Button(root, text="Mark Done", command=mark_done)
remove_done_button = tk.Button(root, text="Remove Done", command=remove_done)
remove_item_button = tk.Button(root, text="Remove Item", command=remove_item)

save_button = tk.Button(root, text="Save to File", command=save_to_file)
load_button = tk.Button(root, text="Load from File", command=load_from_file)

tasks_listbox = tk.Listbox(root)

# Pack widgets
task_label.pack(fill=tk.X)
task_entry.pack(fill=tk.X)
add_button.pack(fill=tk.X)
mark_done_button.pack(fill=tk.X)
remove_item_button.pack(fill=tk.X)
remove_done_button.pack(fill=tk.X)
tasks_listbox.pack(fill=tk.BOTH, expand=True)



save_button.pack()
load_button.pack()

# load list
load_from_file()

# Initialize task list
tasks = []

# Start GUI event loop
root.mainloop()
