from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from Persistencia import bd

class Contabilidade:

    def __init__(self):
        # DATA ATUAL
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year

        self.id = id

        # OBEJTO OS
        self.window()

    def window(self):

        self.windowMain = Tk()
        self.windowMain.title('CONTABILIDADE')
        self.windowMain['bg'] = "Black"

        lbl = Label(self.windowMain, text='VALOR TOTAL DE MÃO DE OBRA', font='Arial 12 bold', bg="Black", fg='white')
        lbl.pack()

        lblTotal = Label(self.windowMain, text='', font='Arial 30 bold', bg="Black", fg='SpringGreen')
        lblTotal.pack()

        def setValor():
            #PEGAR O VALOR TOTAL
            lblTotal['text'] = f'R$ {bd().getAllMaoObra()}'

        #SETAR VALOR
        setValor()

        self.windowMain.mainloop()