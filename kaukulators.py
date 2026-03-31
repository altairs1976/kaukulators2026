from tkinter import *
from math import *
import tkinter as tk

#izveidojas logs
mansLogs = Tk()
mansLogs.title("Kalkulators")

#padara rāmi pelēku
mansLogs.configure(bg="grey")

#====================================================================================================

def btnClick(number): #taisa pogas
    current = e.get() #nolasa skaitli
    e.delete(0, END) #izdzes skaitli
    newNumber = str(current) + str(number)
    e.insert(0, newNumber)
    return 0 

#====================================================================================================
#visas darbibas
def btnCommand(command): 
    global mathOp #matematiskais operators
    global num1
    mathOp = command
    num1 = float(e.get())
    e.delete(0, END)
    return 0 

#====================================================================================================
#izveido vienādības zīmi kura strādā
def vienads(): 
    global num2
    num2 = float(e.get())
    result = 0

    if mathOp == "+":
        result = num1 + num2
    elif mathOp == "-":
        result = num1 - num2
    elif mathOp == "*":
        result = num1 * num2
    elif mathOp == "/":
        result = num1 / num2

    e.delete(0, END)
    e.insert(0, str(result))
    return 0 

#====================================================================================================
#izveido komandu lau notīrītu
def notirit(): 
    e.delete(0,END)
    num1=0
    mathOp="c"
    return 0 
#====================================================================================================
#izveido komandu lai aprēķinātu kvadrātsakni
def sq_rt(): 
    global operator
    global num1
    global mathOp
    num1=(float(e.get()))
    num1=sqrt(num1)
    e.delete(0,END)
    e.insert(0,num1)
    return 0

#====================================================================================================
#izveido komandu lai apreķina kvadrātu
def kvad(): 
    global operator
    global num1
    global mathOp
    num1=(float(e.get()))
    num1=num1 **2
    e.delete(0,END)
    e.insert(0,num1)
    return 0

#====================================================================================================
#izveido komandu kas ievadis punktu 
def decimal(): 
    current = e.get()
    if "." not in current:  
        e.insert(END, ".")

#====================================================================================================
#komanda kas taisa skaitli negativu un pozitivu
def plus_minus(): 
    global num1
    current = e.get()
    if current:
        num1 = -float(current)
        e.delete(0,END)
        e.insert(0,str(num1))
    return 0 

#====================================================================================================
#ievades logs
e = Entry(mansLogs, width=15, bd=20, font=("Arial black", 20))
e.grid(row=0, column=0, columnspan=4)

#====================================================================================================
#visas pogas (cipari, zimes)
btn0 = Button(mansLogs, text="0", padx="40", pady="20", bd=10,font=("Arial black",10),bg="grey", command=lambda: btnClick(0)) 
btn1 = Button(mansLogs, text="1", padx="40", pady="20", bd=10,font=("Arial black",10),bg="grey", command=lambda: btnClick(1))
btn2 = Button(mansLogs, text="2", padx="40", pady="20", bd=10,font=("Arial black",10),bg="grey", command=lambda: btnClick(2))
btn3 = Button(mansLogs, text="3", padx="40", pady="20", bd=10,font=("Arial black",10),bg="grey", command=lambda: btnClick(3))
btn4 = Button(mansLogs, text="4", padx="40", pady="20", bd=10,font=("Arial black",10),bg="grey", command=lambda: btnClick(4))
btn5 = Button(mansLogs, text="5", padx="40", pady="20", bd=10,font=("Arial black",10),bg="grey", command=lambda: btnClick(5))
btn6 = Button(mansLogs, text="6", padx="40", pady="20", bd=10,font=("Arial black",10),bg="grey", command=lambda: btnClick(6))
btn7 = Button(mansLogs, text="7", padx="40", pady="20", bd=10,font=("Arial black",10),bg="grey", command=lambda: btnClick(7))
btn8 = Button(mansLogs, text="8", padx="40", pady="20", bd=10,font=("Arial black",10),bg="grey", command=lambda: btnClick(8))
btn9 = Button(mansLogs, text="9", padx="40", pady="20", bd=10,font=("Arial black",10),bg="grey", command=lambda: btnClick(9))

btnSum = Button(mansLogs, text="+", padx="40", pady="20", bd=10,font=("Arial black",10),bg="orange", command=lambda: btnCommand("+"))
btnsub = Button(mansLogs, text="-", padx="40", pady="20", bd=10,font=("Arial black",10),bg="orange", command=lambda: btnCommand("-"))
btndevide = Button(mansLogs, text=":", padx="40", pady="20", bd=10,font=("Arial black",10),bg="orange", command=lambda: btnCommand("/"))
btntimes = Button(mansLogs, text="x", padx="40", pady="20", bd=10,font=("Arial black",10),bg="orange", command=lambda: btnCommand("*"))  
btnequal = Button(mansLogs, text="=", padx="40", pady="20", bd=10,font=("Arial black",10),bg="orange", command=vienads)
btnClear = Button(mansLogs, text="C", padx="40", pady="20", bd=10,font=("Arial black",10),fg="red", bg="dark grey", command=notirit)
btnhz = Button(mansLogs, text="+/-", padx="40", pady="20", bd=10,font=("Arial black",10),bg="dark grey", command=plus_minus)
btndecimal = Button(mansLogs, text=".", padx="40", pady="20", bd=10,font=("Arial black",10),bg="dark grey", command=decimal)
btnsquere = Button(mansLogs, text="x²", padx="40", pady="20", bd=10,font=("Arial black",10),bg="dark grey", command=kvad) 
btnroot = Button(mansLogs, text="√", padx="40", pady="20", bd=10,font=("Arial black",10),bg="dark grey",command=sq_rt) 

#====================================================================================================
#pogu izvietojums
btnClear.grid(row=1, column=0) 
btnsquere.grid(row=1, column=1)
btnroot.grid(row=1, column=2)
btndevide.grid(row=1, column=3)

btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)
btnSum.grid(row=4, column=3)

btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
btnsub.grid(row=3, column=3)

btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
btntimes.grid(row=2, column=3)

btn0.grid(row=5, column=1)
btnhz.grid(row=5, column=0)
btndecimal.grid(row=5, column=2)
btnequal.grid(row=5, column=3)

#====================================================================================================
#atkārto kodu 
mansLogs.mainloop()