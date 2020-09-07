from tkinter import *
# setting some things up.
window = Tk()
window.title("simple calculator by __ilprofessore ")
window.resizable(width=False, height=False)
# declaring some variables, this is not a must but i like it this way.
new_num = ""
num = 0
operation = ""

# the decimal button.
def button_deci():
    global num
    input_box.insert(num, ".")
    num += 1

# creating the equal function.
def button_equal():
    global new_num
# using if statement to differentiate between operations.
    if operation == "addition":
        opp = float(new_num) + float(input_box.get())
        button_clear()
        input_box.insert(0, opp)
    elif operation == "subtraction":
        opp = float(new_num) - float(input_box.get())
        button_clear()
        input_box.insert(0, opp)
    elif operation == "multiplication":
        opp = float(new_num) * float(input_box.get())
        button_clear()
        input_box.insert(0, opp)
    elif operation == "division":
        opp = float(new_num) / float(input_box.get())
        button_clear()
        input_box.insert(0, opp)
# creating the clear function.
def button_clear():
    input_box.delete(0, END)
# creating the addition function.
def button_add():
    global new_num
    global operation
    operation = "addition"
    new_num = input_box.get()
    button_clear()
# creating the subtraction function.
def button_subtract():
    global new_num
    global operation
    operation = "subtraction"
    new_num = input_box.get()
    button_clear()
# creating the multiplication function.
def button_multiply():
    global new_num
    global operation
    operation = "multiplication"
    new_num = input_box.get()
    button_clear()
# creating the division function.
def button_divide():
    global new_num
    global operation
    operation = "division"
    new_num = input_box.get()
    button_clear()
# this function will display the inputs onto the entry widget.
def button_click(digit):
    global num
    input_box.insert(num, str(digit))
    num += 1
# creating the input entry widget.
input_box = Entry(window, width=65, borderwidth=5)
input_box.grid(row=0, column=0, columnspan=4)
# creating button 1.
button_1 = Button(window, padx=60, pady=10, text="1", command=lambda: button_click(1))
button_1.grid(row=1, column=1)
# creating button 2.
button_2 = Button(window, padx=60, pady=10, text="2", command=lambda: button_click(2))
button_2.grid(row=1, column=2)
# creating button 3.
button_3 = Button(window, padx=60, pady=10, text="3", command=lambda: button_click(3))
button_3.grid(row=1, column=3)
# creating button 4.
button_4 = Button(window, padx=60, pady=10, text="4", command=lambda: button_click(4))
button_4.grid(row=2, column=1)
# creating button 5.
button_5 = Button(window, padx=60, pady=10, text="5", command=lambda: button_click(5))
button_5.grid(row=2, column=2)
# creating button 6.
button_6 = Button(window, padx=60, pady=10, text="6", command=lambda: button_click(6))
button_6.grid(row=2, column=3)
# creating button 7.
button_7 = Button(window, padx=60, pady=10, text="7", command=lambda: button_click(7))
button_7.grid(row=3, column=1)
# creating button 8.
button_8 = Button(window, padx=60, pady=10, text="8", command=lambda: button_click(8))
button_8.grid(row=3, column=2)
# creating button 9.
button_9 = Button(window, padx=60, pady=10, text="9", command=lambda: button_click(9))
button_9.grid(row=3, column=3)
# creating button 0.
button_0 = Button(window, padx=60, pady=10, text="0", command=lambda: button_click(0))
button_0.grid(row=4, column=1)
# creating addition button.
button_add_var = Button(window, padx=60, pady=10, text="+", command=button_add)
button_add_var.grid(row=4, column=2)
# creating subtraction button.
button_subtract_var = Button(window, padx=60, pady=10, text="-", command=button_subtract)
button_subtract_var.grid(row=6, column=1)
# creating multiplication button.
button_multiply_var = Button(window, padx=60, pady=10, text="*", command=button_multiply)
button_multiply_var.grid(row=6, column=2)
# creating division button.
button_divide_var = Button(window, padx=61, pady=10, text="/", command=button_divide)
button_divide_var.grid(row=6, column=3)
# creating clear button.
button_clear_var = Button(window, padx=59, pady=10, text="C", command=button_clear)
button_clear_var.grid(row=4, column=3)
# creating equal button.
button_equal_var = Button(window, padx=196, pady=10, text="=", command=button_equal)
button_equal_var.grid(row=5, column=1, columnspan=3)

button_decimal = Button(window, padx=198, pady=10, text=".", command=button_deci)
button_decimal.grid(row=7, column=1, columnspan=3)

# the end |(* don't even try to steal my code or i'll claim your deeds on Judgement Day.
window.mainloop()
