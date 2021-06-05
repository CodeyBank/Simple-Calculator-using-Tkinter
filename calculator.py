from tkinter import *

root = Tk()
root.title("Calculator")
root.iconbitmap("Ampeross-Qetto-2-Calc.ico")

screen = Entry(root, fg="blue", bg="white", width=50)
screen.grid(row=0, column=0, columnspan=4, pady=20, ipady=20, ipadx=37)

def mem():
    memory = screen.get()
    screen.insert(END, memory)



def keyboard_input(value):
    # screen.delete(0, END)
    str(value)
    screen.insert(END, value)


def clear_screen():
    screen.delete(0, END)


def button_equal():
    try:
        query = StringVar
        query = str(screen.get())
        add_index = int(query.find("+"))
        sub_index = query.find("-")
        div_index = query.find("/")
        mul_index = query.find("*")

        if query.find("+") != -1:
            firstNumber = float(query[0: add_index])
            secondNumber = float(query[add_index + 1: len(query)])
            result = firstNumber + secondNumber
            screen.delete(0, END)
            screen.insert(0, result)
        elif query.find("-") != -1:
            firstNumber = float(query[0: sub_index])
            secondNumber = float(query[sub_index + 1: len(query)])
            result = firstNumber - secondNumber
            screen.delete(0, END)
            screen.insert(0, result)
        elif query.find("*") != -1:
            firstNumber = float(query[0: mul_index])
            secondNumber = float(query[mul_index + 1: len(query)])
            result = firstNumber * secondNumber
            screen.delete(0, END)
            screen.insert(0, result)
        elif query.find("/") != -1:
            firstNumber = float(query[0: div_index])
            secondNumber = float(query[div_index + 1: len(query)])
            result = firstNumber / secondNumber
            screen.delete(0, END)
            screen.insert(0, result)
        else:
            screen.delete(0, END)
            screen.insert(0, "Error")
    except ValueError:
        print(ValueError)
        screen.delete(0, END)
        screen.insert(0, "No inputs")
# def add():


# define buttons
btn1 = Button(root, text="1", fg="blue", padx=40, pady=20, command=lambda: keyboard_input(1))
btn2 = Button(root, text="2", fg="blue", padx=40, pady=20, command=lambda: keyboard_input(2))
btn3 = Button(root, text="3", fg="blue", padx=40, pady=20, command=lambda: keyboard_input(3))
btn4 = Button(root, text="4", fg="blue", padx=40, pady=20, command=lambda: keyboard_input(4))
btn5 = Button(root, text="5", fg="blue", padx=40, pady=20, command=lambda: keyboard_input(5))
btn6 = Button(root, text="6", fg="blue", padx=40, pady=20, command=lambda: keyboard_input(6))
btn7 = Button(root, text="7", fg="blue", padx=40, pady=20, command=lambda: keyboard_input(7))
btn8 = Button(root, text="8", fg="blue", padx=40, pady=20, command=lambda: keyboard_input(8))
btn9 = Button(root, text="9", fg="blue", padx=40, pady=20, command=lambda: keyboard_input(9))
btn0 = Button(root, text="0", fg="blue", padx=40, pady=20, command=lambda: keyboard_input(0))
btn_clr = Button(root, text="C", fg="blue", padx=38.5, pady=20, command=clear_screen)
btn_add = Button(root, text="+", fg="blue", padx=40, pady=20, command=lambda: keyboard_input("+"))
btn_sub = Button(root, text="-", fg="blue", padx=40, pady=20, command=lambda: keyboard_input("-"))
btn_div = Button(root, text="/", fg="blue", padx=40, pady=20, command=lambda: keyboard_input("/"))
btn_mul = Button(root, text="x", fg="blue", padx=40, pady=20, command=lambda: keyboard_input("*"))
btn_mem = Button(root, text="M", fg="blue", padx=38.2, pady=20, command=mem)
btn_equal = Button(root, text="=", fg="blue", padx=185, pady=20, command=button_equal)

# pack the buttons on the screen

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn_mul.grid(row=3, column=3)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn_sub.grid(row=2, column=3)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn_add.grid(row=1, column=3)

btn0.grid(row=4, column=0)
btn_mem.grid(row=4, column=1)
btn_clr.grid(row=4, column=2)
btn_div.grid(row=4, column=3)
btn_equal.grid(row=5, column=0, columnspan=4)

root.mainloop()
