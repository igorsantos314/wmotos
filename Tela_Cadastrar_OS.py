from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from Persistencia import bd
from module_json import json_ws
from tkinter import scrolledtext
import os
from util import util

class Tela_Cadastrar_OS:

    def __init__(self):
        # DATA ATUAL
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year

        self.data_atual = f'{self.day}/{self.month}/{self.year}'

        # OBEJTO OS
        self.window()
#
    def window(self):

        self.windowMain = Tk()
        self.windowMain.resizable(False, False)
        self.windowMain.geometry(util().toCenterScreen(810, 490))
        self.windowMain.focus_force()
        self.windowMain.title('Cadastrar Ordem de Serviço')
        self.windowMain['bg'] = 'White'
        #self.windowMain.attributes('-fullscreen', True)  
        #self.fullScreenState = False

        # Data
        lblDataEntrada = Label(self.windowMain, text='Data de Entrada:', font='Arial 12', bg='White')
        lblDataEntrada.place(x=10, y=10)
        
        etDataEntrada = Entry(self.windowMain, font='Arial 12', width=20)
        etDataEntrada.insert(0, self.data_atual)
        etDataEntrada.place(x=10, y=35)

        lblDataSaida = Label(self.windowMain, text='Data de Saida:', font='Arial 12', bg='White')
        lblDataSaida.place(x=210, y=10)

        etDataSaida = Entry(self.windowMain, font='Arial 12', width=20)
        etDataSaida.insert(0, self.data_atual)
        etDataSaida.place(x=210, y=35)

        # Cliente e Veiculo
        lblCliente = Label(self.windowMain, text='Cliente:*', font='Arial 12', bg='White')
        lblCliente.place(x=410, y=10)

        etCliente = Entry(self.windowMain, font='Arial 12 ', fg=f'{json_ws().getColorCliente()}', width=20)
        etCliente.place(x=410, y=35)

        lblVeiculo = Label(self.windowMain, text='Veiculo:*', font='Arial 12', bg='White')
        lblVeiculo.place(x=610, y=10)

        etVeiculo = Entry(self.windowMain, font='Arial 12 ', fg=f'{json_ws().getColorVeiculo()}', width=20)
        etVeiculo.place(x=610, y=35)

        #Telefone
        lblTelefone = Label(self.windowMain, font='Arial 12', text='Telefone:', bg='White')
        lblTelefone.place(x=10, y=75)

        etTelefone = Entry(self.windowMain, font='Arial 12', fg=f'{json_ws().getColorTelefone()}', width=20)
        etTelefone.place(x=10, y=100)

        # Descricao e Laudo
        lblDesc = Label(self.windowMain, text='Descrição do Cliente:', font='Arial 12', bg='White')
        lblDesc.place(x=10, y=140)

        stDesc = scrolledtext.ScrolledText(self.windowMain, font='Arial 12', width=41, height=6)
        stDesc.place(x=10, y=165)
        
        lblLaudo = Label(self.windowMain, text='Laudo Tecnico:', font='Arial 12', bg='White')
        lblLaudo.place(x=410, y=140)

        stLaudo = scrolledtext.ScrolledText(self.windowMain, font='Arial 12', width=41, height=6)
        stLaudo.place(x=410, y=165)

        # Pagamento
        lblPagamento = Label(self.windowMain, text='Forma de Pagamento:', font='Arial 12', bg='White')
        lblPagamento.place(x=10, y=295)

        comboPagamento = ttk.Combobox(self.windowMain, font='Arial 12', width=18)

        comboPagamento['values'] = tuple(
            ['DINHEIRO', 'CARTÃO', 'PIX', 'OUTRO'])
        comboPagamento.current(0)
        comboPagamento.place(x=10, y=320)

        # Status
        lblStatus = Label(self.windowMain, font='Arial 12', text='Status:', bg='White')
        lblStatus.place(x=210, y=295)

        comboStatus = ttk.Combobox(self.windowMain, font='Arial 12', width=18)

        comboStatus['values'] = tuple(
            ['EM ESPERA', 'EM ANDAMENTO', 'CONCLUIDO'])
        comboStatus.current(0)
        comboStatus.place(x=210, y=320)

        # Valores
        lblObra = Label(self.windowMain, font='Arial 12', text='Valor mão de Obra:', bg='White')
        lblObra.place(x=10, y=365)

        etObra = Entry(self.windowMain, font='Arial 12 bold')
        etObra.insert(0, '0')
        etObra.place(x=10, y=390)

        lblPecas = Label(self.windowMain, font='Arial 12', text='Valor em Peças:', bg='White')
        lblPecas.place(x=210, y=365)

        etPecas = Entry(self.windowMain, font='Arial 12 bold')
        etPecas.insert(0, '0')
        etPecas.place(x=210, y=390)

        lblOutros = Label(self.windowMain, font='Arial 12', text='Outros Valores:', bg='White')
        lblOutros.place(x=410, y=365)

        etOutros = Entry(self.windowMain, font='Arial 12 bold')
        etOutros.insert(0, '0')
        etOutros.place(x=410, y=390)

        #SALVAR
        imagem_salvar = PhotoImage(file=f"src/salvar_48.png")
        btExibir = Button(self.windowMain, image=imagem_salvar, bg='White', command=lambda: save())
        btExibir.imagem = imagem_salvar
        btExibir.place(x=670, y=430)

        #VOLTAR
        imagem_voltar = PhotoImage(file=f"src/voltar_48.png")
        btVoltar = Button(self.windowMain, image=imagem_voltar, bg='White', command=lambda: exit())
        btVoltar.imagem = imagem_voltar
        btVoltar.place(x=740, y=430)

        # Funcoes
        def save():

            # MENSAGEM DE ERROR
            if etVeiculo.get() == '' or etCliente.get() == '':
                messagebox.showerror(
                    'AVISO', 'CAMPOS OBRIGATÓRIOS NÃO ESTÃO PREENCHIDOS')

            else:
                # SALVAR
                if messagebox.askyesno('', 'SALVAR OS?'):

                    bd().insertOS(
                        etDataEntrada.get(),
                        etDataSaida.get(),
                        etCliente.get().upper(),
                        etTelefone.get(),
                        etVeiculo.get().upper(),
                        stDesc.get("1.0", END).upper(),
                        stLaudo.get("1.0", END).upper(),
                        comboPagamento.get(),
                        comboStatus.get(),
                        float(etObra.get().replace(',','.')),
                        float(etPecas.get().replace(',','.')),
                        float(etOutros.get().replace(',','.'))
                    )

                    messagebox.showinfo('','CADASTRADO COM SUCESSO !')

                # LIMPAR
                clear()

        def clear():
            # LIMPAR
            etDataEntrada.delete(0, END)
            etDataSaida.delete(0, END)
            etCliente.delete(0, END)
            etTelefone.delete(0, END)
            etVeiculo.delete(0, END)
            stDesc.delete("1.0", END)
            stLaudo.delete("1.0", END)
            etObra.insert(0, '0')
            etPecas.insert(0, '0')
            etOutros.insert(0, '0')
            
        def exit():
            #DESTRUIR
            self.windowMain.destroy()
        
        etDataEntrada.focus_force()
        #self.windowMain.bind("<F11>", self.toggleFullScreen)
        #self.windowMain.bind("<Escape>", self.quitFullScreen)

        self.windowMain.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.windowMain.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.windowMain.attributes("-fullscreen", self.fullScreenState)
        print(self.toCenterScreen())

#Tela_Cadastrar_OS()