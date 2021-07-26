from tkinter import *
def add():
    

    try:
        
        tot=int(E1.get())+int(E2.get())
        print(tot)
        val.set(tot)
    except ValueError as a:
        tot="Enter only numeric value"
        val.set(tot)
        print("Enter only numeric value",a)
def sub():
    
    try:
        
        tot=int(E1.get())-int(E2.get())
        print(tot)
        val.set(tot)
    except ValueError as a:
        tot="Enter only numeric value"
        val.set(tot)
        print("Enter only numeric value",a)
def multi():
    
    try:
        
        tot=int(E1.get())*int(E2.get())
        print(tot)
        val.set(tot)
    except ValueError as a:
        tot="Enter only numeric value"
        val.set(tot)
        print("Enter only numeric value","",a)
def div():
    try:
        
        tot=int(E1.get())/int(E2.get())
        print(tot)
        val.set(tot)
    except ZeroDivisionError as a:
        tot="cannot divide by zero '0'"
        val.set(tot)
        print(tot,"",a)

    except ValueError as a:
        tot="Enter only numeric value"
        val.set(tot)
        print("Enter only numeric value",a)

A=Tk()
val=StringVar()
A.geometry("200x200")

L1=Label(A,text="Number 1")
L1.grid(row=0,column=0,sticky=W)

E1=Entry(A,bd=5)
E1.grid(row=0,column=1,sticky=W)


L2=Label(A,text="Number 2")
L2.grid(row=1,column=0,sticky=W)

E2=Entry(A,bd=5)
E2.grid(row=1,column=1,sticky=W)


L3=Label(A,text="Result")
L3.grid(row=2,column=0,sticky=W)

L4=Label(A,textvariable=val)
L4.grid(row=2,column=1,sticky=W)

B = Button(A, text = "ADD",bg="black",fg="white",activebackground="blue",activeforeground="yellow",command=add)
B.grid(row=3,column=1,sticky=W)

B = Button(A, text = "SUBTRACT",bg="black",fg="white",activebackground="blue",activeforeground="yellow",command=sub)
B.grid(row=4,column=1,sticky=W)

B = Button(A, text = "MUTIPLICATION",bg="black",fg="white",activebackground="blue",activeforeground="yellow",command=multi)
B.grid(row=5,column=1,sticky=W)

B = Button(A, text = "DIVISION",bg="black",fg="white",activebackground="blue",activeforeground="yellow",command=div)
B.grid(row=6,column=1,sticky=W)

A.mainloop()
