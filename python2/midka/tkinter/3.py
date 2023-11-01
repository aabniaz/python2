import tkinter as tk

def func():
    username = username_entry.get()
    password = password_entry.get()

    if username == "user" and password == "password":
        login_status.config(text="Login Successful", fg="green")
    else:
        login_status.config(text="Login Failed. Try again.", fg="red")

root = tk.Tk()
root.title("Login System")

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # 'show' will mask the password
password_entry.pack()

login_button = tk.Button(root, text="Login", command=func)
login_button.pack()

login_status = tk.Label(root, text="", fg="black")
login_status.pack()

root.mainloop()
