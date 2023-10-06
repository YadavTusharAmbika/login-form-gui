import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x200")
root.title("Login Form")

def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "user" and password == "pass":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

label_username = tk.Label(root, text="Username:")
label_username.pack(pady=10)
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

button_login = tk.Button(root, text="Login", command=validate_login)
button_login.pack(pady=20)

root.mainloop()
