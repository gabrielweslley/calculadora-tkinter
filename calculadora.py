from tkinter import *

#funções dos botões
def limpar():
    display.delete(0, END)

def inserir(valor):
    display.insert(END, valor)

def calcular():
    text_display = display.get()
    result = eval(text_display)
    limpar()
    display.insert(0, str(result))


window = Tk()

window.title("Calculadora")

window.geometry("300x400")


def createButtonResult(text):
    return Button(panel, text=text, bg='grey', bd=2, font="Arial 16 bold", width=5, height=3, command=calcular)

def createButton(text):
    return Button(panel, text=text, bg='grey', bd=2, font="Arial 16 bold", width=5, height=3, command=lambda: inserir(text))

def createButtonClear(text):
    return Button(panel, text=text, bg='grey', bd=2, font="Arial 16 bold", width=5, height=3, command=limpar)

display = Entry(window, font="Arial 20 bold", bg="#1c3ec7", fg="white", width=20)

display.pack()

panel = Frame(window)

panel.pack()

num0 = createButton("0")
num1 = createButton("1")
num2 = createButton("2")
num3 = createButton("3")
num4 = createButton("4")
num5 = createButton("5")
num6 = createButton("6")
num7 = createButton("7")
num8 = createButton("8")
num9 = createButton("9")

div = createButton("÷")
multi = createButton("x")
sub = createButton("-")
sum = createButton("+")
clear = createButtonClear("CE")
result = createButtonResult("=")

num7.grid(row=1, column=0)
num8.grid(row=1, column=1)
num9.grid(row=1, column=2)
div.grid(row=1, column=3)

num4.grid(row=2, column=0)
num5.grid(row=2, column=1)
num6.grid(row=2, column=2)
multi.grid(row=2, column=3)

num1.grid(row=3, column=0)
num2.grid(row=3, column=1)
num3.grid(row=3, column=2)
sub.grid(row=3, column=3)

clear.grid(row=4, column=0)
num0.grid(row=4, column=1)
result.grid(row=4, column=2)
sum.grid(row=4, column=3)

window.mainloop()





