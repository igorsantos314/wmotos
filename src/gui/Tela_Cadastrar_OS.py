from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date

class Tela_Cadastrar_OS:

    def __init__(self):
        #DATA ATUAL
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year

        self.window()

    def window(self):

        self.windowMain = Tk()
        
        #Data
        lblDataEntrada = Label(self.windowMain, text='Data de Entrada:')
        lblDataEntrada.pack()

        etDataEntrada = Entry()
        etDataEntrada.pack()

        lblDataSaida = Label(self.windowMain, text='Data de Saida:')
        lblDataSaida.pack()

        etDataSaida = Entry()
        etDataSaida.pack()

        #Mes
        lblPagamento = Label(self.windowMain, text='Forma de Pagamento:')
        lblPagamento.pack()

        comboPagamento = ttk.Combobox(self.windowMain, width = 15) 

        comboPagamento['values'] = tuple(['DINHEIRO', 'CARTÃO', 'PIX', 'OUTRO'])
        comboPagamento.current(0)
        comboPagamento.pack()

        #Ano
        lblStatus = Label(self.windowMain, text='Status:')
        lblStatus.pack()

        comboStatus = ttk.Combobox(self.windowMain, width = 15) 

        comboStatus['values'] = tuple(['EM ESPERA', 'EM ANDAMENTO', 'CONCLUIDO'])
        comboStatus.current(0)
        comboStatus.pack()

        self.windowMain.mainloop()

Tela_Cadastrar_OS()