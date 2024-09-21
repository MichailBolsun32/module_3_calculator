import tkinter as tk

def get_velius():
    num_1 = int(number1_entry.get())
    num_2 = int(number2_entry.get())
    return num_1, num_2

def insert_velius(velius):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, velius)

def add():
    num_1, num_2 = get_velius()
    sum = num_1 + num_2
    insert_velius(sum)

def sub():
    num_1, num_2 = get_velius()
    sub_ = num_1 - num_2
    insert_velius(sub_)

def mul():
    num_1, num_2 = get_velius()
    mul_ = num_1 * num_2
    insert_velius(mul_)

def div():
    num_1, num_2 = get_velius()
    div_ = num_1 / num_2
    insert_velius(div_)


window = tk.Tk()

window.title('Калькулятор')
window.geometry('350x350')
window.resizable(width=False, height=False)

button_add = tk.Button(window, text='+', width=2, height=1, command=add)
button_add.place(x=100, y=300)
button_sub = tk.Button(window, text='-', width=2, height=1, command=sub)
button_sub.place(x=150, y=300)
button_mul = tk.Button(window, text='*', width=2, height=1, command=mul)
button_mul.place(x=200, y=300)
button_div = tk.Button(window, text='/', width=2, height=1, command=div)
button_div.place(x=250, y=300)

number1_entry = tk.Entry(window, width=30)
number1_entry.place(x=100, y=28)
number2_entry = tk.Entry(window, width=30)
number2_entry.place(x=100, y=78)
answer_entry = tk.Entry(window, width=30)
answer_entry.place(x=100, y=138)

number1 = tk.Label(window, text='Введите первое число:')
number1.place(x=100, y=7)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=100, y=57)
answer = tk.Label(window, text='Результат вычисления:')
answer.place(x=100, y=117)

window.mainloop()
