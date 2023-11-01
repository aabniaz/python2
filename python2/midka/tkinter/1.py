import tkinter as tk

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val, col_val = 1, 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, command=calculate).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(root, text=button, command=lambda: entry.delete(0, tk.END)).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
