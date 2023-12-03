import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Final")
window.geometry("500x500")



def login():
    username = tk.Label(text = 'Enter username: ', font=("Roboto 11"))
    password = tk.Label(text = 'Enter password: ', font=("Roboto 11"))
    usernameEntry = tk.Entry(font=("Roboto 11"))
    passwordEntry = tk.Entry(font=("Roboto 11"))
    login_button = tk.Button(text = "Login", command = _login_btn_clicked)
    username.grid(column = 0, row = 1)
    password.grid(column = 0, row = 2)
    usernameEntry.grid(column = 1, row = 1)
    passwordEntry.grid(column = 1, row = 2)
    login_button.grid(column = 1, row = 3)

def _login_btn_clicked():
        usernameEntry = tk.Entry(font=("Roboto 11"))
        passwordEntry = tk.Entry(font=("Roboto 11"))
        username = usernameEntry.get()
        password = passwordEntry.get()
        if username == "username" and password == "password":
            messagebox.showinfo("Welcome")
        else:
            messagebox.showinfo("Error")
            
login()












window.mainloop()
