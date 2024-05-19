from tkinter import *
import tkinter as tk

def click(event):
    global scvalue
    text = event.widget.cget("text")  # cget() is used to get text from button
    
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())
                scvalue.set(value)
                entry.update()
            except Exception as e:
                print(e)
                value = "Error"
                scvalue.set(value)
                entry.update()
    elif text == "C":
        scvalue.set("")
        entry.update()
    else:
        scvalue.set(scvalue.get()+text)
        entry.update()
    

root = tk.Tk()
root.geometry("450x500")
root.resizable(width=False, height=False)
root.configure(bg="#17161b")
root.title("Calculator by SHIVAM AHUJA")
photo = PhotoImage(file= "D:\CodeSoft tasks\Calculator application\images\calci_logo.png")
root.iconphoto(False, photo)


scvalue = StringVar()
scvalue.set("")
entry = tk.Entry(root,textvariable=scvalue, font="lucida 20 bold")
entry.pack(ipadx=5, pady=30)

# btn_frame =tk.Frame(root, bg="gray")
# btn_frame.pack(pady=20)

button = tk.Button(root, text="C",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#3697f5", fg="#fff")
button.place(x=20,y=100)
button.bind("<Button-1>", click)
button = tk.Button(root, text="/",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=120,y=100)
button.bind("<Button-1>", click)
button = tk.Button(root, text="%",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=220,y=100)
button.bind("<Button-1>", click)
button = tk.Button(root, text="*",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=320,y=100)
button.bind("<Button-1>", click)

button = tk.Button(root, text="7",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=20,y=180)
button.bind("<Button-1>", click)
button = tk.Button(root, text="8",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=120,y=180)
button.bind("<Button-1>", click)
button = tk.Button(root, text="9",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=220,y=180)
button.bind("<Button-1>", click)
button = tk.Button(root, text="-",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=320,y=180)
button.bind("<Button-1>", click)

button = tk.Button(root, text="4",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=20,y=260)
button.bind("<Button-1>", click)
button = tk.Button(root, text="5",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=120,y=260)
button.bind("<Button-1>", click)
button = tk.Button(root, text="6",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=220,y=260)
button.bind("<Button-1>", click)
button = tk.Button(root, text="+",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=320,y=260)
button.bind("<Button-1>", click)

button = tk.Button(root, text="1",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=20,y=340)
button.bind("<Button-1>", click)
button = tk.Button(root, text="2",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=120,y=340)
button.bind("<Button-1>", click)
button = tk.Button(root, text="3",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=220,y=340)
button.bind("<Button-1>", click)
button = tk.Button(root, text="0",width=11,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=20,y=420)
button.bind("<Button-1>", click)

button = tk.Button(root, text=".",width=5,height=1,font=("Arial", 20, "bold"),bd=1, bg="#2a2d36", fg="#fff")
button.place(x=220,y=420)
button.bind("<Button-1>", click)
button = tk.Button(root, text="=",width=5,height=3,font=("Arial", 20, "bold"),bd=1, bg="#fe9037", fg="#fff")
button.place(x=320,y=340)
button.bind("<Button-1>", click)


root.mainloop()
