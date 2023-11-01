import tkinter as tk

def authenticate():
    username = username_entry.get()
    password = password_entry.get()

    if username == "user" and password == "password":
        login_status.config(text="Login Successful", fg="green")
    else:
        login_status.config(text="Login Failed. Try again.", fg="red")

root = tk.Tk()
root.title("Try")

username_label = tk.Label(root, text = "username")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text = "password")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

login_button = tk.Button(root, text="Login", command=authenticate)
login_button.pack()

login_status = tk.Label(root, text="", fg="black")
login_status.pack()

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()

