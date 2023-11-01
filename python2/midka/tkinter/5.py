import tkinter as tk

def open_new_window():
    def submit_data():
        data = entry.get()
        new_window_label.config(text="Data submitted: " + data)

    new_window = tk.Toplevel(root)
    new_window.title("New Window")

    entry_label = tk.Label(new_window, text="Enter data:")
    entry_label.pack()

    entry = tk.Entry(new_window)
    entry.pack()

    submit_button = tk.Button(new_window, text="Submit", command=submit_data)
    submit_button.pack()

    new_window_label = tk.Label(new_window, text="")
    new_window_label.pack()

root = tk.Tk()
root.title("Main Window")

open_window_button = tk.Button(root, text="Open New Window", command=open_new_window)
open_window_button.pack()

root.mainloop()
