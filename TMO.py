import json
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class tmo:

    def __init__(self):
        self.caminho = 'ws_motos_tmo.json'
        self.dict = self.ler()

        self.windowAddService()

    def ler(self):
        #LER ARQUIVO
        with open(self.caminho, 'r', encoding='utf-8') as f:
            return json.load(f)

    def escrever(self, dict):
        #ESCREVER DICIONÁRIO NO JSON
        with open(self.caminho, 'w', encoding='utf-8') as f:
            json.dump(dict, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

    def listarItens(self):
        
        list_arq = {}

        for dir, sub, arq in os.walk('F:/CATALOGO'):
            for i in arq:
                list_arq[i.replace('.pdf','').upper()] = {}

        #print(list_arq)
        self.escrever(list_arq)
   
    def window(self):

        self.windowMain = Tk()
        self.windowMain.title('CUSTO DE MÃO DE OBRA')
        self.windowMain.geometry('500x500')
        self.windowMain['bg'] = 'White'

        # VEICULOS
        lblMoto = Label(self.windowMain, text='MOTOCICLETA:', font='Arial 15', bg='White')
        lblMoto.place(x=10, y=10)

        comboMoto = ttk.Combobox(self.windowMain, font='Arial 12', width=50)

        comboMoto['values'] = tuple(
            [veiculo for veiculo in self.dict])
        comboMoto.place(x=10, y=50)

        btConsultarVeiculo = Button(text='CONSULTAR VEICULO', font='Arial 12', width=25)
        btConsultarVeiculo.place(x=10, y=90)

        # SERVICÇOS
        lblServico = Label(self.windowMain, text='SERVIÇO:', font='Arial 15', bg='White')
        lblServico.place(x=10, y=170)

        self.comboServico = ttk.Combobox(self.windowMain, font='Arial 12', width=50)
        self.comboServico.place(x=10, y=210)
        #self.comboServico['values'] = tuple()

        self.windowMain.mainloop()

    def windowAddService(self):
        windowService = Tk()

        # VEICULOS
        lblMoto = Label(windowService, text='MOTOCICLETA:', font='Arial 15', bg='White')
        lblMoto.pack()

        comboMoto = ttk.Combobox(windowService, font='Arial 12', width=50)

        comboMoto['values'] = tuple(
            [veiculo for veiculo in self.dict])
        comboMoto.pack()

        lbl = Label(windowService, text='NOME SERVICO', font='Arial 15')
        lbl.pack()

        key = Entry(font='Arial 15')
        key.pack()

        #--
        lbl = Label(windowService, text='TMO DO SERVICO', font='Arial 15')
        lbl.pack()

        value = Entry(windowService, font='Arial 15')
        value.pack()
        
        btConsultarVeiculo = Button(windowService, text='GUARDAR TMO', font='Arial 12', width=25, command=lambda:save())
        btConsultarVeiculo.pack()

        def save():
            self.dict[comboMoto.get()][key.get().upper()] = value.get()
            self.escrever(self.dict)

            print('SALVO')

            key.delete(0, END)
            key.focus()

        windowService.mainloop()
tmo()