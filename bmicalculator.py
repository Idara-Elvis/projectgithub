from tkinter import *

def reset_entry():
    age_tf.delete(0, "end")
    height_tf.delete(0, "end")
    weight_tf.delete(0, "end")

def calculate_bmi(weight_tf, height_tf):
    kg = float(weight_tf.get())
    m = float(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    return bmi

def alter_display():
    bmi= calculate_bmi(weight_tf, height_tf)
    ans.grid(row=9, column=2)
    ans.insert(0, bmi)


window = Tk()
window.title("bmitalks")
window.geometry("500x750")
window.configure(background="pink")

var = IntVar()
screen = Label(text="bmi values in details" , width= 34, background="pink", foreground="purple")
screen.grid(row=0, column=0, sticky="NSEW")

screen = Label(text="bmi less than 18.5 is underweight" , width= 34, background="pink", foreground="purple")
screen.grid(row=0, column=0, sticky="NSEW")

screen = Label(text="bmi greater than 18.5 and less than 24.9 is normal" , width= 34, background="pink", foreground="purple")
screen.grid(row=1, column=0, sticky="NSEW")

screen = Label(text="bmi greater than 24.9 and less than 29.9 is overweight" , width= 34, background="pink", foreground="purple")
screen.grid(row=2, column=0, sticky="NSEW")

screen = Label(text="bmi greater than 29.9 is obesity" , width= 34, background="pink", foreground="purple")
screen.grid(row=3, column=0, sticky="NSEW")

frame= Frame(window, padx=10, pady=10)
frame.grid(row=4, column=0)
frame.configure(background="pink")

age_lb = Label(frame, text= "ENTER YOUR AGE(2-100)")
age_lb.grid(row=5, column=1,)

age_tf= Entry(frame, bg="pink",fg="purple", width=5)
age_tf.grid(row=5, column=2)

gender_lb = Label(frame, text= "SELECT GENDER",bg="pink",fg="purple")
gender_lb.grid(row=6, column=1)

frame2 = Frame(frame,)
frame2.grid(row=6, column=2, pady=5)

ml_rb= Radiobutton(frame2, text= "MALE", variable= var, value= 1)
ml_rb.pack(side = LEFT)

fl_rb= Radiobutton(frame2, text= "FEMALE", variable= var, value=2)
fl_rb.pack(side= RIGHT)

height_lb = Label(frame, text= "ENTER YOUR HEIGHT(cm)")
height_lb.grid(row=7, column=1, padx=5, pady=5)

height_tf = Entry(frame , bg="pink",fg="purple", width=8)
height_tf.grid(row=7, column =2, padx=5, pady=5)
 
weight_lb= Label(frame, text= "ENTER YOUR WEIGHT (kg)")
weight_lb.grid(row=8, column=1, padx=5, pady=5)

weight_tf= Entry(frame, bg="pink",fg="purple", width=8)
weight_tf.grid(row=8, column=2, padx=5, pady=5)

answer_lb= Label(frame, text= "BMI",bg="pink",fg="purple", width=8)
answer_lb.grid(row=9, column=1, padx=5, pady=5)

ans= Entry(frame, bg="pink",fg="purple", width=8)
ans.grid(row=9, column=2, padx=5, pady=5)



frame3= Frame(frame, bg="pink")
frame3.grid(row=10, columnspan=3, pady=10)

calculate_bn= Button(frame3, text= "CALCULATE",bg="pink",fg="purple", width=8, command= lambda: alter_display())
calculate_bn.pack(side= LEFT, padx=5, pady=5)

reset_bn= Button(frame3, text= "RESET", bg="pink",fg="purple", width=8, command= lambda: reset_entry())
reset_bn.pack(side= LEFT, padx=5, pady=5)

exit_bn= Button(frame3, text= "EXIT",bg="pink",fg="purple", width=8, command=lambda: window.destroy())
exit_bn.pack(side= RIGHT, padx=5, pady=5)




window.mainloop()






