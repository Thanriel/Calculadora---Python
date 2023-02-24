from tkinter import *


root = Tk()  # Abre a janela gráfica

root.title('Sua calculadora')  # Instancia o título da janela
root.geometry('408x355')
root.minsize(408, 355)
root.maxsize(408, 355)


num1 = ''
divisao = FALSE
multiplicao = FALSE
adcao = FALSE
subtracao = FALSE

root.configure(background='#282828')

e = Entry(
    root,
    width=15,
    borderwidth=4,
    relief=FLAT,
    fg='#FFFFFF',
    bg='#a7a28f',
    font=('futura', 25, 'bold'),
    justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)

# Funções


def botaoClick(num):
    e.insert(END, num)


def botaoDivisao():
    global num1
    global divisao
    divisao = TRUE
    num1 = e.get()
    e.delete(0, END)


def botaoMultiplicacao():
    global num1
    global multiplicao
    multiplicao = TRUE
    num1 = e.get()
    e.delete(0, END)


def botaoSubtracao():
    global num1
    global subtracao
    subtracao = TRUE
    num1 = e.get()
    e.delete(0, END)


def botaoAdcao():
    global num1
    global adcao
    adcao = TRUE
    num1 = e.get()
    e.delete(0, END)


def botaoClear():
    e.delete(0, END)


def botaoIgual():
    global subtracao
    global adcao
    global multiplicao
    global divisao
    num2 = e.get()
    e.delete(0, END)

    if (adcao):
        e.insert(0, int(num1) + int(num2))
        adcao = FALSE

    elif (subtracao):
        e.insert(0, int(num1) - int(num2))
        subtracao = FALSE

    elif (multiplicao):
        e.insert(0, int(num1) + int(num2))
        multiplicao = FALSE

    elif (divisao):
        e.insert(0, int(num1) / int(num2))
        divisao = FALSE


# Botões
btnDivisao = Button(
    root,
    text='/',
    padx=40,
    pady=20,
    command=botaoDivisao,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnDivisao.grid(row=0, column=4)

btnNumOne = Button(
    root,
    text='1',
    padx=40,
    pady=20,
    command=lambda: botaoClick(1),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnNumOne.grid(row=1, column=1)

btnNumTwo = Button(
    root,
    text='2',
    padx=40,
    pady=20,
    command=lambda: botaoClick(2),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnNumTwo.grid(row=1, column=2)

btnNumThree = Button(
    root,
    text='3',
    padx=40,
    pady=20,
    command=lambda: botaoClick(3),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnNumThree.grid(row=1, column=3)

btnMultiplicacao = Button(
    root,
    text='x',
    padx=41,
    pady=20,
    command=botaoMultiplicacao,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnMultiplicacao.grid(row=1, column=4)

btnNumFour = Button(
    root,
    text='4',
    padx=40,
    pady=20,
    command=lambda: botaoClick(4),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnNumFour.grid(row=2, column=1)

btnNumFive = Button(
    root,
    text='5',
    padx=40,
    pady=20,
    command=lambda: botaoClick(5),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnNumFive.grid(row=2, column=2)

btnNumSix = Button(
    root,
    text='6',
    padx=40,
    pady=20,
    command=lambda: botaoClick(6),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnNumSix.grid(row=2, column=3)

btnSubtracao = Button(
    root,
    text='-',
    padx=43,
    pady=20,
    command=botaoSubtracao,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnSubtracao.grid(row=2, column=4)

btnNumSeven = Button(
    root,
    text='7',
    padx=40,
    pady=20,
    command=lambda: botaoClick(7),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnNumSeven.grid(row=3, column=1)

btnNumEight = Button(
    root,
    text='8',
    padx=40,
    pady=20,
    command=lambda: botaoClick(8),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnNumEight.grid(row=3, column=2)

btnNumNine = Button(
    root,
    text='9',
    padx=40,
    pady=20,
    command=lambda: botaoClick(9),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnNumNine.grid(row=3, column=3)

btnAdcao = Button(
    root,
    text='+',
    padx=41,
    pady=20,
    command=botaoAdcao,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnAdcao.grid(row=3, column=4)

btnNumZero = Button(
    root,
    text='0',
    padx=91,
    pady=20,
    command=lambda: botaoClick(9),
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnNumZero.grid(row=4, column=1, columnspan=2)

btnClear = Button(
    root,
    text='C',
    padx=40,
    pady=20,
    command=botaoClear,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnClear.grid(row=4, column=4)

btnEquals = Button(
    root,
    text='=',
    padx=40,
    pady=20,
    command=botaoIgual,
    fg='#FFFFFF',
    activeforeground='#FFFFFF',
    bg='#320064',
    activebackground='#240046',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
btnEquals.grid(row=4, column=3)

root.mainloop()  # Mantem a janela aberta até o usuário decidir fechar
