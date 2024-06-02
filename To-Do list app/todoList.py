from tkinter import *
import tkinter as tk
from tkinter import messagebox

'''Author : SHIVAM AHUJA'''

class todo:
    def __init__(self,root):
        self.root=root
        self.root.title("To-Do list Application")
        self.root.geometry("700x500")

        self.label1= tk.Label(self.root,text= "To-Do List Application", width=10, font=("arial 20 bold"), bd=5, bg='orange',fg='black')
        self.label1.pack(side="top", fill=BOTH)

        self.label2= tk.Label(self.root,text= "Add Task", width=10, font=("arial 15 bold"), bd=5, bg='orange',fg='black')
        self.label2.place(x=40,y=60)

        self.label3= tk.Label(self.root,text= "Tasks", width=10, font=("arial 15 bold"), bd=5, bg='orange',fg='black')
        self.label3.place(x=400,y=60)

        self.showListBox = tk.Listbox(self.root,height=25,width=45,bd=3, font=('arial 15 italic bold'))
        self.showListBox.place(x=350,y=100)

        self.text = tk.Text(self.root,bd=2, height=1, width=15, font=('arial 15 bold'))
        self.text.place(x=35, y=100)
        self.text.config(padx= 8, pady=8)

        def addTask():
            content = self.text.get('1.0',tk.END)
            self.showListBox.insert(tk.END, content)
            with open("data.txt",'a') as f:
                f.write(content + '\n')
                f.seek(0)
                f.close()
            self.text.delete('1.0',tk.END)

        def deleteTask():
            selectIndexs = self.showListBox.curselection()
            if not selectIndexs:
                messagebox.showwarning("No selection", "Please select a task to delete.")
                return
            
            selected_items = self.showListBox.get(selectIndexs)
             # Update the data.txt file
            with open('data.txt', 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if line.strip() not in selected_items:
                        f.write(line)
               # Delete the tasks from the Listbox
            self.showListBox.delete(selectIndexs)
        with open('data.txt','r') as file:
            read = file.readlines()
            for i in read:
                self.showListBox.insert(tk.END,i.strip())

        self.button1 = tk.Button(self.root,text="Add",font=('arial 10 bold'), width=10, bg='orange',fg='black',command=addTask)
        self.button1.place(x=25,y=170)

        self.button2 = tk.Button(self.root,text="Delete",font=('arial 10 bold'), width=10, bg='orange',fg='black',command=deleteTask)
        self.button2.place(x=200,y=170)


def main():
    root = tk.Tk()
    v1 = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()