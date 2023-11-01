import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])  

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30)
entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

root.mainloop()
