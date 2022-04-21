
from tkinter import *

def select_number(num):
    screen.insert(END, num)


def clear_field():
    screen.delete(1.0, END)

def button_add():
    first_number = screen.get()
    global f_num
    global math
    math= "addition"
    f_num = int(first_number)
    screen.delete(0, END)


def button_sub():
    first_number = screen.get()
    global f_num
    global math
    math= "subtraction"
    f_num = int(first_number)
    screen.delete(0, END)

def button_mul():
    first_number = screen.get()
    global f_num
    global math
    math= "multiplication"
    f_num = int(first_number)
    screen.delete(0, END)


def button_div():
    first_number = screen.get()
    global f_num
    global math
    math= "division"
    f_num = int(first_number)
    screen.delete(0, END)


def button_equal():
    second_number = screen.get()
    screen.delete(0, END)

    if math == "addition":
        screen.insert(0, f_num + int(second_number))
       
    if math == "subtraction":
        screen.insert(0, f_num - int(second_number))    

    if math == "multiplication":
        screen.insert(0, f_num * int(second_number))

    if math == "division":
        screen.insert(0, f_num / int(second_number))

    

window = Tk()
window.title("SIMPLE CALCULATOR FOR SECONDARY SCHOOL")
window.geometry("100x250")
window.configure(padx=10 , pady=10)
window.configure(background="white")

screen = Text(width= 34, height= 5, background="white", foreground="black")
screen.grid(row=0, column=0, sticky="NSEW")
screen.configure(font="-family {sans} -size 13 -weight bold")

space1 = Label(text="", background="white")
space1.grid(row=1, column=0)

frame= Frame(window)
frame.grid(row=2, column=0)
frame.configure(background="white")

btn1 = Button(frame, text = "1" , background= "gray" , foreground = "white", width=5 , height=2, command=lambda: select_number(1))
btn1.grid(row=0 ,column=0, padx=10, pady=10, sticky="NSEW")
btn1.configure(font="-family {sans} -size 13 -weight bold")

btn2= Button(frame,text = "2" , background= "gray" , foreground= "white" , width=5, height=2 ,command=lambda: select_number (2))
btn2.grid(row=0, column= 1, padx=10, pady=10, sticky= "NSEW")
btn2.configure(font="-family {sans} -size 13 -weight bold")

btn3 = Button(frame, text="3" , background= "gray" , foreground= "white" , width=5 , height=2, command=lambda: select_number(3))
btn3.grid(row=0, column=2 , padx=10, pady=10, sticky= "NSEW")
btn3.configure(font="-family {sans} -size 13 -weight bold")

btn4 = Button(frame, text="4" , background= "gray" , foreground= "white" , width=5 , height=2, command=lambda: select_number(4))
btn4.grid(row=1, column=0 , padx=10, pady=10, sticky= "NSEW")
btn4.configure(font="-family {sans} -size 13 -weight bold")

btn5 = Button(frame, text="5" , background= "gray" , foreground= "white" , width=5 , height=2, command=lambda : select_number(5))
btn5.grid(row=1, column=1 , padx=10, pady=10, sticky= "NSEW")
btn5.configure(font="-family {sans} -size 13 -weight bold")


btn6 = Button(frame, text="6" , background= "gray" , foreground= "white" , width=5 , height=2, command=lambda :select_number (6))
btn6.grid(row=1, column=2 , padx=10, pady=10, sticky= "NSEW")
btn6.configure(font="-family {sans} -size 13 -weight bold")

btn7 = Button(frame, text="7" , background= "gray" , foreground= "white" , width=5 , height=2, command=lambda : select_number(7))
btn7.grid(row=2, column=0 , padx=10, pady=10, sticky= "NSEW")
btn7.configure(font="-family {sans} -size 13 -weight bold")

btn8 = Button(frame, text="8" , background= "gray" , foreground= "white" , width=5 , height=2, command=lambda : select_number(8))
btn8.grid(row=2, column=1 , padx=10, pady=10, sticky= "NSEW")
btn8.configure(font="-family {sans} -size 13 -weight bold")

btn9 = Button(frame, text="9" , background= "gray" , foreground= "white" , width=5 , height=2, command=lambda : select_number(9))
btn9.grid(row=2, column=2 , padx=10, pady=10, sticky= "NSEW")
btn9.configure(font="-family {sans} -size 13 -weight bold")

btn0 = Button(frame, text="0" , background= "gray" , foreground= "white" , width=5 , height=2, command=lambda : select_number(0))
btn0.grid(row=3, column=0 , padx=10, pady=10, sticky= "NSEW")
btn0.configure(font="-family {sans} -size 13 -weight bold")

btnplus = Button(frame, text="+" , background= "gray" , foreground= "white" , width=5 , height=2, command=lambda : select_number("+"))
btnplus.grid(row=1, column=3 , padx=10, pady=10, sticky= "NSEW")
btnplus.configure(font="-family {sans} -size 13 -weight bold")



btnsub = Button(frame, text="-" , background= "gray" , foreground= "white" , width=5 , height=2, command=lambda :select_number("-"))
btnsub.grid(row=2, column=3 , padx=10, pady=10, sticky= "NSEW")
btnsub.configure(font="-family {sans} -size 13 -weight bold")

btnmul = Button(frame, text="*" , background= "gray" , foreground= "white" , width=5 , height=2, command=lambda : select_number("*"))
btnmul.grid(row=3, column=1 , padx=10, pady=10, sticky= "NSEW")
btnmul.configure(font="-family {sans} -size 13 -weight bold")

btnequal = Button(frame, text="=" , background= "gray" , foreground= "white" , width=5 , height=2)
btnequal.grid(row=3, column=2 , padx=10, pady=10, sticky= "NSEW")
btnequal.configure(font="-family {sans} -size 13 -weight bold")
btnequal.configure(command = button_equal)

btnclear = Button(frame, text="Ac" , background= "gray" , foreground= "white" , width=10 , height=5,)
btnclear.grid(row=0, column=3 , padx=10, pady=10, sticky= "NSEW")
btnclear.configure(font="-family {sans} -size 13 -weight bold")
btnclear.configure(command= clear_field)


btndiv = Button(frame, text="/" , background= "gray" , foreground= "white" , width=5 , height=2, command=lambda: select_number("/"))
btndiv.grid(row=3, column=3 , padx=10, pady=10, sticky= "NSEW")
btndiv.configure(font="-family {sans} -size 13 -weight bold")

window.mainloop()

