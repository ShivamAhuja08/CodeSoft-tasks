import tkinter as tk
from tkinter import *
from random import randint
from tkinter import messagebox


def generator():
    genPwd_entry.delete(0,END)
    userName = name_entry.get().strip()

    pwdLength = my_entry.get().strip()

    if not userName or not pwdLength:
        messagebox.showerror("Error", "Please enter your name and password length.")
        return
    
    try:
        password_length = int(pwdLength)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")
        return

    if password_length <= 0:
        messagebox.showerror("Error", "Password length should be greater than 0.")
        return

    my_pwd = ""
    for x in range(password_length):
        my_pwd += chr(randint(33,126))
    genPwd_entry.insert(0,my_pwd)

def clipboard():
    root.clipboard_clear()
    root.clipboard_append(genPwd_entry.get())
    messagebox.showinfo("I Thank you for visiting our application", "Password copied to clipboard successfully!")

root = tk.Tk()
root.geometry("600x400")
root.resizable(width=False, height=False)
root.config(bg="#1C2833") 
root.title("Password generator- SHIVAM AHUJA")
photo = tk.PhotoImage(file= "F:\Code Soft tasks\password generator/secure.jpg")
root.iconphoto(False, photo)

lf = LabelFrame(root, text="Enter password details", font=("Helvetica", 12, "bold"), bg="#212121", fg="white")
lf.pack(pady=20)

name_label = Label(lf, text="Enter your name:", font=("Helvetica", 12, "bold"), bg="#212121", fg="white")
name_label.pack()
name_entry = Entry(lf, font="Helvetica 15")
name_entry.pack(ipadx=25, padx=30, pady=10)

pwd_label = Label(lf, text="Enter password length:", font=("Helvetica", 12, "bold"), bg="#212121", fg="white")
pwd_label.pack()
my_entry = Entry(lf, font="Helvetica 15")
my_entry.pack(ipadx=25, padx=30, pady=10)


# Create entry box for generated password
label = tk.Label(root,text="Generated Password:",font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white")
label.pack(side=tk.TOP, padx=10)
genPwd_entry = Entry(root,text="", font="Arial 15",bg="black", fg="white")
genPwd_entry.pack(side=tk.TOP, ipadx=30, padx=40, pady=15)

# create frame for button
my_frame = tk.Frame(root)
my_frame.config(bg="#2b2b2b")
my_frame.pack(pady=20)

btn1 =tk.Button(my_frame, text="Create Strong password", font=("Helvetica",12,"bold"), bg="#0000FF", fg="white", command=generator)
btn1.grid(row=0, column=0, padx=10)
btn2 =tk.Button(my_frame, text="Copy to clipBoard", font=("Helvetica",12,"bold"), bg="#FFEB3B", fg="black", command=clipboard)
btn2.grid(row=0, column=1, padx=10)


root.mainloop()