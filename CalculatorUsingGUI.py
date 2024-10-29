from tkinter import *
import math
def click(event):
    ex=screen.get()
    text=event.widget.cget("text")  #event.widget will give button and .cget("text") will give text on button
    no = scvalue.get()
    print(text)



    if text == "=":
        if scvalue.get().isdigit():  #if scvalue is digit then convert it into integer
            value= int(scvalue.get())

        else:
            try:
                value = eval(screen.get()) #eval function evalute the string

            except Exception as e:
                print(e)
                value = "Error"
                scvalue.set("Error")
                screen.update()
        scvalue.set(value)
        screen.update()


    elif text == "Cl":
        scvalue.set("")
        screen.update()

    elif text=="C":
        ex=ex[0:len(ex)-1]
        screen.delete(0,END)
        screen.insert(0,ex)

    elif text=="cos":
        answer=math.cos(math.radians(eval(ex)))
        screen.insert(0, answer)

    elif text=="sin":
        answer=math.sin(math.radians(eval(ex)))
        screen.insert(0, answer)

    elif text=="tan":
        answer=math.tan(math.radians(eval(ex)))
        screen.insert(0, answer)

    elif text=="cosh":
        answer=math.cosh(eval(ex))
        screen.insert(0, answer)

    elif text=="sinh":
        answer=math.sinh(eval(ex))
        screen.insert(0, answer)

    elif text=="tanh":
        answer=math.tanh(eval(ex))
        screen.insert(0, answer)

    elif text=="x\u02b8":
        screen.insert(END,"**")

    elif text=="x\u00B3":
        answer=eval(ex)**3
        screen.delete(0, END)
        screen.insert(0, answer)

    elif text=="x\u00B2":
        answer= eval(ex)**2
        screen.delete(0,END)
        screen.insert(0, answer)

    elif text=="3√":
        answer= eval(ex)**(1/3)
        screen.insert(0, answer)

    elif text=="\u221A":
        answer=math.sqrt(eval(ex))
        screen.delete(0, END)
        screen.insert(0, answer)

    elif text=="π":
        answer=math.pi
        screen.delete(0, END)
        screen.insert(0, answer)

    elif text == "2π":
        answer = 2*math.pi
        screen.delete(0, END)
        screen.insert(0, answer)

    elif text=="log":
        answer= math.log2(eval(ex))
        screen.delete(0, END)
        screen.insert(0, answer)

    elif text=="log10":
        answer= math.log10(eval(ex))
        screen.delete(0, END)
        screen.insert(0, answer)

    elif text=="deg":
        answer = math.degrees(eval(ex))
        screen.delete(0, END)
        screen.insert(0, answer)

    elif text=="rad":
        answer= math.radians(eval(ex))
        screen.delete(0, END)
        screen.insert(0, answer)

    elif text=="e":
        answer= math.e
        screen.delete(0, END)
        screen.insert(0, answer)

    elif text == "x!":
        answer = math.factorial(eval(ex))
        screen.delete(0, END)
        screen.insert(0, answer)

    elif text=="exp":
        answer= math.exp(eval(ex))
        screen.delete(0, END)
        screen.insert(0, answer)



    else:
        scvalue.set(scvalue.get() + text)  #set the scvalue and add text to scvalue
        screen.update()  #update function force the updates and it update the screen Entry visit with new value of scvalue



root=Tk()    #To access the method which are present in tk class
root.title("Calculator")

root.geometry("500x800+100+100")
root.minsize(100,250)
root.maxsize(500,800,)

root.configure(background="black")

frame = Frame(root, bg="Grey", borderwidth=8, relief=GROOVE)
frame.pack(side= TOP, fill="x")
l = Label(frame, text="WELCOME TO MY CALCULATOR",fg="red")
l.pack(pady=10)

scvalue = StringVar()
scvalue.set("")
screen=Entry(root, textvar = scvalue, font="Times 40 bold",bg="Sky blue",borderwidth=8,relief="groove")
screen.pack(fill=X, ipadx=10,padx=15,pady=15)


f= Frame(root, bg="Blue",borderwidth=8, relief=GROOVE)
f.pack(side= TOP, fill="x")

b=Button(f, width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue", text="1",font="Times 30 bold",fg="Black")
b.pack(side=LEFT, padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue", text="2",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue",text="3",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="sin",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="sinh",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue", text="+",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue", text="Cl",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)



f= Frame(root, bg="Blue",borderwidth=8, relief=GROOVE)
f.pack(side= TOP, fill="x")

b=Button(f, width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue",text="4",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue", text="5",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue", text="6",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="cos",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="cosh",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue", text="-",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue", text="%",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)


f= Frame(root, bg="Blue",borderwidth=8, relief=GROOVE)
f.pack(side= TOP, fill="x")

b=Button(f, width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue",text="7",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue", text="8",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue",text="9",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="tan",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="tanh",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue",text="*",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue",text="\u221A",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)


f= Frame(root, bg="Blue",borderwidth=8, relief=GROOVE)
f.pack(side= TOP, fill="x")

b=Button(f,width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue", text="0",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue", text=".",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="C",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="log",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="log10",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue", text="/",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=2,height=1,bd=2,relief=SUNKEN,bg="Skyblue",text="=",font="Times 30 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

f= Frame(root, bg="Blue",borderwidth=8, relief=GROOVE)
f.pack(side= TOP, fill="x")

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="e",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="rad",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="π",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="deg",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="exp",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="(",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text=")",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)


f= Frame(root, bg="Blue",borderwidth=8, relief=GROOVE)
f.pack(side= TOP, fill="x")

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="2π",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="x!",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="3√",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="x\u02b8",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="x\u00B2",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(f, width=3,height=2,bd=2,relief=SUNKEN,bg="Skyblue",text="x\u00B3",font="Times 20 bold",fg="Black")
b.pack(side=LEFT,padx=9,pady=5)
b.bind("<Button-1>",click)


root.mainloop()

