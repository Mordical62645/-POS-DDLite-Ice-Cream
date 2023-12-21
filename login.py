#Modules 
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess

#Index and dictionary
account = {}
account["ADMIN"] = {
    "username": "ADMIN",
    "password": "ADMIN"
}

#Declaration of variables
global user
user=None

global p2
p2=None

root = tk.Tk()
root.title("Dreamy D'lights")
root.geometry('1220x900')
root.iconbitmap("DDL_1.ico")
root.resizable(False, False)

login_image = PhotoImage(master=root, file="galaxy.png")
canvas = Canvas(root, width = 1220, height = 900)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=login_image)


def sign_login():
    answer = messagebox.askyesno("Notification", "Already have an account?")
    if answer == True:
        login_Main()
    
def sign_signup():
    global i
    global user
    global p2

    
    user = sign_entry_username.get()
    p1 = sign_pass1.get()
    p2 = sign_pass2.get()

    if sign_entry_username.get() == 'Enter username here' or sign_entry_username.get() == '':
        messagebox.showwarning("Warning", "Please enter a username")
        return
    
    if p1 == p2:
        messagebox.showinfo("Sign in Successful", "Welcome, Dear Customer")
        account[user] = {
            "username": user,
            "password": p2
        }
        login_Main()
    else:
        messagebox.showwarning("Warning", "Password doesn't match")


def sign_on_entry_click(event):
    if sign_entry_username.get() == 'Enter username here':
        sign_entry_username.delete(0, tk.END)
        sign_entry_username.config(fg='black')

def sign_on_focus_out(event):
    if sign_entry_username.get() == '':
        sign_entry_username.insert(0, 'Enter username here')
        sign_entry_username.config(fg='gray')

def sign_password_visible():
    if sign_show_password.get():
        sign_pass1.config(show="")
        sign_pass2.config(show="")
        sign_show_password_checkbox.configure(text = "Hide Password")
    else:
        sign_pass1.config(show="•")
        sign_pass2.config(show="•")
        sign_show_password_checkbox.configure(text = "Show Password")

def sign_Main():
    sign_frame = tk.Frame(root, width = 650, height = 500, bg = "#363C66")
    sign_frame.place(x = 300, y= 120)

    signlabel = tk.Label(sign_frame, text = " Sign Up", font = ('georgia', 40, 'bold'), bg = "#363C66", fg='white')
    signlabel.place(x = 220, y = 60)

    templabel = tk.Label(sign_frame, text = "Create a temporary account", font = ('georgia', 12, 'bold'), bg = "#363C66", fg='white')
    templabel.place(x = 220, y = 130)

    sign_label_username = tk.Label(sign_frame, text="Username:", font = ('georgia',15,'bold'), bg = "#363C66", fg='white')
    sign_label_username.place(x = 60, y = 179)

    sign_label_password1 = tk.Label(sign_frame, text="Enter Password:", font = ('georgia',15,'bold'), bg = "#363C66", fg='white')
    sign_label_password1.place(x = 60, y = 240)

    global sign_pass1
    sign_pass1 = tk.Entry(sign_frame, show="•")
    sign_pass1.configure(width = 25,  font = ('georgia', 15))
    sign_pass1.place(x = 250, y = 240)

    sign_label_password2 = tk.Label(sign_frame, text="Confirm Password:", font = ('georgia',15,'bold'), bg = "#363C66", fg='white')
    sign_label_password2.place(x = 60, y = 290)

    global sign_pass2
    sign_pass2 = tk.Entry(sign_frame, show="•")
    sign_pass2.configure(width = 23,  font = ('georgia', 15))
    sign_pass2.place(x = 274, y = 290)

    global sign_entry_username
    sign_entry_username = tk.Entry(sign_frame)
    sign_entry_username.configure(width = 30, font = ('georgia', 15), fg='gray')
    sign_entry_username.insert(0, 'Enter username here')
    sign_entry_username.bind('<FocusIn>', sign_on_entry_click)
    sign_entry_username.bind('<FocusOut>', sign_on_focus_out)
    sign_entry_username.place(x = 190, y = 180)

    global sign_show_password
    global sign_show_password_checkbox
    sign_show_password = tk.BooleanVar()
    sign_show_password_checkbox = ttk.Checkbutton(sign_frame, text="Show Password", variable=sign_show_password, command=sign_password_visible)
    sign_show_password_checkbox.place(x = 274, y = 340)

    sign_btn_login = tk.Button(sign_frame, text="Back",font = ('georgia', 15), command=sign_login)
    sign_btn_login.configure(width = 15, height = 1)
    sign_btn_login.place(x = 130, y = 380)

    sign_btn_signup = tk.Button(sign_frame, text="Submit",font = ('georgia', 15), command=sign_signup)
    sign_btn_signup.configure(width = 15, height = 1)
    sign_btn_signup.place(x = 330, y = 380)

    return root


def login_login():
    global user
    global p2
    username = login_entry_username.get()
    password = login_entry_password.get()

    account_user = account.get(username)

    if not account_user:
        messagebox.showerror("Login Failed", "Account does not exist")
        print("Account does not exist")
        return 
    
    if username == "admin" or password == "admin":
        messagebox.showerror("Login Failed", "Account does not exist")
        print("Account does not exist")
        return 
    
    elif account_user["username"] == username and account_user["password"] == password:
        messagebox.showinfo("Login Successful", "Welcome, Dear Customer")
        root.withdraw()
        subprocess.Popen(["Main.py"], shell=True)
        
        
def login_click_signup():
    sign_Main()

def login_on_entry_click(event):
    if login_entry_username.get() == 'Enter username here':
        login_entry_username.delete(0, tk.END)
        login_entry_username.config(fg='black')

def login_on_focus_out(event):
    if login_entry_username.get() == '':
        login_entry_username.insert(0, 'Enter username here')
        login_entry_username.config(fg='gray')

def login_password_visible():
    if login_show_password.get():
        login_entry_password.config(show="")
        login_show_password_checkbox.configure(text = "Hide Password")

    else:
        login_entry_password.config(show="•")
        login_show_password_checkbox.configure(text = "Show Password")

def login_Main(): 
    login_frame = tk.Frame(root, width = 650, height = 500, bg = "#363C66")
    login_frame.place(x = 300, y= 120)

    login_label = tk.Label(login_frame, text = " WELCOME", font = ('georgia', 40, 'bold'), bg = "#363C66", fg='white')
    login_label.place(x = 170, y = 60)

    login_label_username = tk.Label(login_frame, text="Username:", font = ('georgia',15,'bold'), bg = "#363C66", fg='white')
    login_label_username.place(x = 60, y = 179)

    login_label_password = tk.Label(login_frame, text="Password:", font = ('georgia',15,'bold'), bg = "#363C66", fg='white')
    login_label_password.place(x = 60, y = 240)

    global login_entry_username
    login_entry_username = tk.Entry(login_frame)
    login_entry_username.configure(width = 30, font = ('georgia', 15), fg='gray')
    login_entry_username.insert(0, 'Enter username here')
    login_entry_username.bind('<FocusIn>', login_on_entry_click)
    login_entry_username.bind('<FocusOut>', login_on_focus_out)
    login_entry_username.place(x = 190, y = 180)

    global login_entry_password
    login_entry_password = tk.Entry(login_frame, show="•")
    login_entry_password.configure(width = 30,  font = ('georgia', 15))
    login_entry_password.place(x = 190, y = 240)

    global login_show_password
    global login_show_password_checkbox
    login_show_password = tk.BooleanVar()
    login_show_password_checkbox = ttk.Checkbutton(login_frame, text="Show Password", variable=login_show_password, command=login_password_visible)
    login_show_password_checkbox.place(x = 190, y = 290)

    btn_login = tk.Button(login_frame, text="Login",font = ('georgia', 15), command=login_login)
    btn_login.configure(width = 15, height = 1)
    btn_login.place(x = 120, y = 330)

    btn_sign = tk.Button(login_frame, text="Sign up",font = ('georgia', 15), command=login_click_signup)
    btn_sign.configure(width = 15, height = 1)
    btn_sign.place(x = 330, y = 330)

    return root

root = login_Main()
root.mainloop()
