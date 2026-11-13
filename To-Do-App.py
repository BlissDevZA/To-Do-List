
import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

tasks = []

def load_tasks():
    global tasks

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                tasks = json.load(file)
        except (json.JSONDecodeError, OSError):
            tasks = []

def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def refresh_tasks():
    task_list.delete(0, tk.END)

    for task in tasks:
        status = "✓" if task["completed"] else "○"
        task_list.insert(
            tk.END,
            f"{status}  {task['name']}"
        )

def add_task():
    task_name = task_entry.get().strip()

    if not task_name:
        messagebox.showwarning(
            "Empty Task",
            "Please enter a task first."
        )
        return

    tasks.append({
        "name": task_name,
        "completed": False
    })

    save_tasks()
    refresh_tasks()
    task_entry.delete(0, tk.END)

def complete_task():
    selection = task_list.curselection()

    if not selection:
        messagebox.showwarning(
            "No Selection",
            "Please select a task."
        )
        return

    index = selection[0]
    tasks[index]["completed"] = not tasks[index]["completed"]

    save_tasks()
    refresh_tasks()

def delete_task():
    selection = task_list.curselection()

    if not selection:
        messagebox.showwarning(
            "No Selection",
            "Please select a task to delete."
        )
        return

    index = selection[0]
    del tasks[index]

    save_tasks()
    refresh_tasks()

# Create main window
root = tk.Tk()
root.title("My To-Do List")
root.geometry("450x500")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

# Heading
heading = tk.Label(
    root,
    text="MY TO-DO LIST",
    font=("Arial", 20, "bold"),
    bg="#f2f2f2",
    fg="#222222"
)
heading.pack(pady=20)

# Task input
task_entry = tk.Entry(
    root,
    font=("Arial", 13),
    width=30
)
task_entry.pack(pady=10)

# Add button
add_button = tk.Button(
    root,
    text="Add Task",
    font=("Arial", 11, "bold"),
    bg="#2196F3",
    fg="white",
    width=20,
    command=add_task
)
add_button.pack(pady=5)

# Task list
task_list = tk.Listbox(
    root,
    font=("Arial", 12),
    width=38,
    height=12,
    selectmode=tk.SINGLE
)
task_list.pack(pady=15)

# Complete button
complete_button = tk.Button(
    root,
    text="Complete / Undo Task",
    font=("Arial", 10, "bold"),
    bg="#4CAF50",
    fg="white",
    width=25,
    command=complete_task
)
complete_button.pack(pady=5)

# Delete button
delete_button = tk.Button(
    root,
    text="Delete Selected Task",
    font=("Arial", 10, "bold"),
    bg="#f44336",
    fg="white",
    width=25,
    command=delete_task
)
delete_button.pack(pady=5)

# Load saved tasks
load_tasks()
refresh_tasks()

# Run application
root.mainloop()