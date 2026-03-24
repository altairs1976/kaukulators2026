from tkinter import*
from math import*
import tkinter as tk

mansLogs=Tk()
mansLogs.title("Kaukulators")

#====================================================================================================

def btnClick(number):
    current=e.get()
    e.delete(0,END)
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)
    return 0 

#====================================================================================================

e=Entry(mansLogs,width=15,bd=20,font=("Arial black",20))
e.grid(row=0,column=0,columnspan=4)

#====================================================================================================

btn0=Button(mansLogs,text="0",padx="40",pady="20", command=lambda:btnClick(0))
btn1=Button(mansLogs,text="1",padx="40",pady="20", command=lambda:btnClick(1))
btn2=Button(mansLogs,text="2",padx="40",pady="20", command=lambda:btnClick(2))
btn3=Button(mansLogs,text="3",padx="40",pady="20", command=lambda:btnClick(3))
btn4=Button(mansLogs,text="4",padx="40",pady="20", command=lambda:btnClick(4))
btn5=Button(mansLogs,text="5",padx="40",pady="20", command=lambda:btnClick(5))
btn6=Button(mansLogs,text="6",padx="40",pady="20", command=lambda:btnClick(6))
btn7=Button(mansLogs,text="7",padx="40",pady="20", command=lambda:btnClick(7))
btn8=Button(mansLogs,text="8",padx="40",pady="20", command=lambda:btnClick(8))
btn9=Button(mansLogs,text="9",padx="40",pady="20", command=lambda:btnClick(9))


btnSum=Button(mansLogs,text="+",padx="40",pady="20", command=lambda:btnCommand("+"))
btnsub=Button(mansLogs,text="-",padx="40",pady="20", command=lambda:btnCommand("-"))
btndevide=Button(mansLogs,text=":",padx="40",pady="20", command=lambda:btnCommand("/"))
btntimes=Button(mansLogs,text="x",padx="40",pady="20", command=lambda:btnCommand("x"))
btnequal=Button(mansLogs,text="=",padx="40",pady="20", command=vienads)
btnClear=Button(mansLogs,text="c",padx="40",pady="20")
btnhz=Button(mansLogs,text="+/-",padx="40",pady="20")
btndecimal=Button(mansLogs,text=",",padx="40",pady="20")
btnsquere=Button(mansLogs,text="x²",padx="40",pady="20") 
btnroot=Button(mansLogs,text="√",padx="40",pady="20")




btnClear.grid(row=1, column=0)
btnsquere.grid(row=1, column=1)
btnroot.grid(row=1, column=2)
btndevide.grid(row=1, column=3)



btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)
btnSum.grid(row=4, column=3)

btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
btnsub.grid(row=3, column=3)

btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
btntimes.grid(row=2, column=3)

btn0.grid(row=5,column=1)
btnhz.grid(row=5,column=0)
btndecimal.grid(row=5,column=2)
btnequal.grid(row=5,column=3)

def vienads():
    global num2
    num2=(float(e.get()))
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0 

def btnCommand(command):
    global number
    global mathOp
    global num1
    global num3
    mathOp=command
    num1=(float(e.get()))
    e.delete(0,END)
    return 0 
 






mansLogs.mainloop()