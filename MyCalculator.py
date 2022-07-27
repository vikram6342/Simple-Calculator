
import math
from tkinter import *

## functions to provide the hover effect


def on_enter(event,arg):
    if arg == "button_equal":
        button_equal.config(background="#00ff73")
        return
    eval(arg+".config(background='#908b89')")

    
def on_leave(event,arg):
    eval(arg+".config(background ='"+buttonDictionary[arg]+"')")


id2 = 0
ex = 0

### function to initialize the entry fields


def initializer():
    global id2
    id2 = 0
    text1.delete(0,END)
    text2.delete(0,END)


### function that ges executed on button clicks


def numbers(num):
    global id2,ex,s
    if ex!=0  and s:
        text1.delete(0,END)
        ex = 0
    if id2 != 0:
        s = 0
        id2 = 0
        text2.delete(0,END)
    text2.insert(END,num)

### function that gets executed on clicking binary operators

def symbols(symbol):
    global id2,ex
    ex=0
    text1.delete(0,END)
    text1.insert(END,text2.get()+symbol)
    id2+=1


def equals():
    global id2,ex
    exp1 = text1.get()
    exp2 = text2.get()
    initializer()
    try:
        text2.insert(0,str(eval(exp1+exp2)))
        text1.insert(0,exp2)
        ex = 1
        s = 1
    except:
        text1.insert(0,"INVALID SYNTAX")
    id2 = 1

def clearElement():
    text2.delete(0,END)

def clear():
    text1.delete(0,END)
    text2.delete(0,END)

### function that gets executed on clicking unary operators

def unary(operation):
    global id2,ex
    id2 = 1
    try:
        x = float(text2.get())
        text2.delete(0,END)
        text2.insert(0,eval(operation))
        text1.delete(0,END)
    except: 
        text1.insert(0,"INVALID SYNTAX")
        ex = 1

### function to delete one element at a time from second entry field

def del_1():
    text2_string = text2.get()
    text2.delete(len(text2_string)-1,END)

root = Tk()
root.geometry("301x450")
root.resizable(0,0)
root.configure(bg="#171010")

# Making an output Screen


text1 = Entry(root,width=20,font=("Arial 19"),borderwidth=0,bg="#171010",fg="#EEEEEE",justify = "right")
text2 = Entry(root,width=13,font=("Arial 31"),borderwidth=0,bg="#171010",fg="#EEEEEE",justify = "right")
text1.place(x=0,y=0)
text2.place(x=0,y=35)


#making buttons

button_modulo = Button(root,text="%",height=3,width=9,bg="#423F3E",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command= lambda : unary("x/100"))
button_CE = Button(root,text="CE",height=3,width=9,bg="#423F3E",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command = clearElement)
button_C = Button(root,text="C",height=3,width=9,bg="#423F3E",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command=clear)
button_del = Button(root,text="🔙",height=3,width=9,bg="#423F3E",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command = del_1)

button_byx = Button(root,text="1/x",height=3,width=9,bg="#423F3E",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command = lambda: unary("1/x"))
button_xsqr = Button(root,text="X²",height=3,width=9,bg="#423F3E",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command=lambda: unary("math.pow(x,2)"))
button_sqr_root = Button(root,text="²✓X",height=3,width=9,bg="#423F3E",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command = lambda : unary("math.sqrt(x)"))
button_divide = Button(root,text="/",height=3,width=9,bg="#423F3E",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command = lambda : symbols("/"))

button_7 = Button(root,text="7",height=3,width=9,bg="#2B2B2B",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command= lambda : numbers("7"))
button_8 = Button(root,text="8",height=3,width=9,bg="#2B2B2B",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command= lambda : numbers("8"))
button_9 = Button(root,text="9",height=3,width=9,bg="#2B2B2B",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command= lambda : numbers("9"))
button_multiply = Button(root,text="X",height=3,width=9,bg="#423F3E",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command = lambda : symbols("*"))

button_4 = Button(root,text="4",height=3,width=9,bg="#2B2B2B",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command= lambda : numbers("4"))
button_5 = Button(root,text="5",height=3,width=9,bg="#2B2B2B",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command= lambda : numbers("5"))
button_6 = Button(root,text="6",height=3,width=9,bg="#2B2B2B",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command= lambda : numbers("6"))
button_subract = Button(root,text="-",height=3,width=9,bg="#423F3E",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command = lambda : symbols("-"))


button_1 = Button(root,text="1",height=3,width=9,bg="#2B2B2B",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command= lambda : numbers("1"))
button_2 = Button(root,text="2",height=3,width=9,bg="#2B2B2B",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command= lambda : numbers("2"))
button_3 = Button(root,text="3",height=3,width=9,bg="#2B2B2B",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command= lambda : numbers("3"))
button_add = Button(root,text="+",height=3,width=9,bg="#423F3E",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command = lambda : symbols("+"))

button_signChange = Button(root,text="+/-",height=3,width=9,bg="#2B2B2B",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command = lambda: unary("-1*x"))
button_0 = Button(root,text="0",height=3,width=9,bg="#2B2B2B",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command= lambda : numbers("0"))
button_dot = Button(root,text=".",height=3,width=9,bg="#2B2B2B",activebackground="#2b2727",fg="#EEEEEE",activeforeground="#EEEEEE",command= lambda : numbers("."))
button_equal = Button(root,text="=",height=3,width=9,bg="#00BD56",activebackground="#00e667",fg="#EEEEEE",activeforeground="#EEEEEE",command=equals)


# Making a list of buttons to place them:
buttonList = [["button_modulo","button_CE","button_C","button_del"],
              ["button_byx","button_xsqr","button_sqr_root","button_divide"],
              ["button_7","button_8","button_9","button_multiply"],
              ["button_4","button_5","button_6","button_subract"],
              ["button_1","button_2","button_3","button_add"],
              ["button_signChange","button_0","button_dot","button_equal"]]

# Making a dictionary of buttons to bind the button names with the original colors:


buttonDictionary = {
                    "button_modulo" : "#423F3E" , "button_CE" : "#423F3E" , "button_C" : "#423F3E" ,"button_del":"#423F3E",
                    "button_byx": "#423F3E" , "button_xsqr" : "#423F3E" , "button_sqr_root" : "#423F3E", "button_divide":"#423F3E",
                    "button_7" : "#2B2B2B" , "button_8" : "#2B2B2B" , "button_9" : "#2B2B2B" , "button_multiply" : "#423F3E",
                    "button_4" : "#2B2B2B" , "button_5" : "#2B2B2B" , "button_6" : "#2B2B2B" , "button_subract" : "#423F3E",
                    "button_1" : "#2B2B2B" , "button_2" : "#2B2B2B" , "button_3" : "#2B2B2B" , "button_add" : "#423F3E",
                    "button_signChange" : "#2B2B2B" , "button_0" : "#2B2B2B", "button_dot" : "#2B2B2B" , "button_equal" : "#00BD56"
}
y = 100
for buttonRow in buttonList: 
    x = 4
    for buttons in buttonRow:
        xString = "x = "+str(x)
        yString = "y = "+str(y)
        eval(str(buttons)+".place("+xString+","+yString+")") 
        x+=74
    y+=58

## setting the Enter event and exit event

for buttonRow in buttonList:
    for buttons in buttonRow:
        eval(buttons+".bind('<Enter>',lambda event,arg= '"+buttons+"' : on_enter(event,arg))")
        eval(buttons+".bind('<Leave>',lambda event,arg= '"+buttons+"' : on_leave(event,arg))")



root.iconbitmap("calculator.ico")
root.title("Simple Calculator")
root.mainloop()