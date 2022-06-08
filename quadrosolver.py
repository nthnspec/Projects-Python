from tkinter import *
from math import sqrt

def solve(a,b,c):
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = f'Дискриминант равен {D}. \nКорни уравнения Х1 = {x1} и Х2 = {x2}'        
    else:
        text = f'Дискриминант меньше нуля. Уравнение не имеет решений.' 
    return text

def insert(value):
    output.delete("0.0","end")
    output.insert("0.0",value)    

def clear(event):
    caller = event.widget
    caller.delete("0", "end")

def handle():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        insert(solve(a_val, b_val, c_val))
    except ValueError:
        insert("Убедитесь, что все поля заполнены")

root = Tk()
root.title("Калькулятор квадратых уравнений")
root.minsize(325,230)
root.resizable(width=False, height=False)

frame = Frame(root)
frame.grid()
a = Entry(frame, width=3)
a.grid(row=1,column=1,padx=(10,0))
a.bind("<FocusIn>", clear)
a_lab = Label(frame, text="x**2+").grid(row=1,column=2)

b = Entry(frame, width=3)
b.bind("<FocusIn>", clear)
b.grid(row=1,column=3)
b_lab = Label(frame, text="x+").grid(row=1, column=4)

c = Entry(frame, width=3)
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)
c_lab = Label(frame, text="= 0").grid(row=1, column=6)

but = Button(frame, text="Решить", command=handle).grid(row=1, column=7, padx=(10,0))

output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
output.grid(row=2, columnspan=8)

root.mainloop() 