from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import colorchooser
from tkinter import Frame
import json
import os

#Functions
def add():
    task=entryBox.get().strip()
    if task == "" :
        messagebox.showwarning(
            "No task",
            "No task entered !"
        )
        return
    # Add task to listbox
    task_list.insert(END,task)
    # Clear Entry    
    entryBox.delete(0,END)
        
    print(task)
    print("You added the task")
#Delete Task    
 
def delete():
    selected = task_list.curselection()
    
    if not selected:
        messagebox.showwarning(
            "No selection",
            "Please select a task to delete"
        )
        retuen
        
    # Delete multiple selected tasks
    for index in reversed(selected):    
        task_list.delete(index)
    print("You deleted the text") 
    
    
def submit():
    tasks = task_list.get(0,END)
    if not tasks:
        messagebox.showwarning(
            "No Tasks",
            "There are no tasks to submit"
        )
        return 
    
    with open ("tasks.json","w") as file:
        json.dump(tasks,file)
        
    for task in tasks:
        print(task)
    print("You submited the text") 
    
def load_tasks():
    try:
        with open ("tasks.json","r") as file:
            tasks = json.load(file)
        for task in tasks:
            task_list.insert(END,task)
      
    except FileNotFoundError:
        pass                           

# GUI of Application 
window =Tk()
window.geometry("500x500")
# window.minsize(500,500)
window.title("TO-DO-LIST")

window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=0)
window.rowconfigure(1, weight=0)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=0)


# Enter TEXT   
frame1 = Frame(window,bg="#FFFFFF",bd=2,width=300,height=300)
frame1.grid(row=0, column=0,sticky="ew")

label1 = Label(frame1,text="To Do list",bg="#FFCCCC",
    font=("Segoe UI", 22, "bold"))
label1.pack(padx=3,pady=3,fill="x")

frame2 = Frame(window,bd=2,relief=RAISED)
frame2.grid(row=1,column=0,sticky="ew",padx=5,pady=5)

entryBox = Entry(frame2,text="Enter your Task",width=50,bg="Light Yellow",font=("Segoe UI", 20))
entryBox.grid(row=0,column=0,sticky="ew",pady=2,padx=2)
frame2.columnconfigure(0, weight=1)



frame3 = Frame(window,bd=2)
frame3.grid(row=2, column=0,sticky="nsew",padx=5,pady=5)
# LISTBOX
task_list = Listbox(frame3,font="Alef,15",fg="Black",bg="#FFCCE5",selectmode=MULTIPLE)
task_list.grid( row=0,column=0,sticky="nsew")

frame3.rowconfigure(0, weight=1)
frame3.columnconfigure(0, weight=1)


#Buttons
frame4= Frame(window,bd=2,height=400,width=500)
frame4.grid(row=3, column=0,sticky="ew",padx=5,pady=5)

#Add Button
add_button = Button(frame4,text="Add",command=add, width=10, font=("Arial",15))
add_button.pack(side=LEFT,fill="x", expand=True)

#Submit Button
submit_button = Button(frame4,text="submit",width=10,font=("Arail",15),command=submit)
submit_button.pack(side=LEFT,fill="x", expand=True)

# Delete Button
delete_button= Button(frame4,text="Delete",width=10,font=("Arial",15),command=delete)
delete_button.pack(side=LEFT,fill="x", expand=True)

# FOR COLOURCHOSSER
# button = Button(frame4,text='selectcolour',width=10,font=("Arial",15),command=click)
# button.pack(side=LEFT,fill="x", expand=True)

window.mainloop()