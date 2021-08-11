from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from Persistencia import bd
from module_json import json_ws
from tkinter import scrolledtext
import os
from util import util
from module_print import print_document

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
        self.windowMain.title('IGTEC - CADASTRAR ORDEM DE SERVIÇO')
        self.windowMain['bg'] = 'White'

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

        #Telefone 1
        lblTelefone1 = Label(self.windowMain, font='Arial 12', text='Telefone 1:', bg='White')
        lblTelefone1.place(x=10, y=75)

        etTelefone1 = Entry(self.windowMain, font='Arial 12', fg=f'{json_ws().getColorTelefone()}', width=20)
        etTelefone1.place(x=10, y=100)

        #Telefone 2
        lblTelefone2 = Label(self.windowMain, font='Arial 12', text='Telefone 2:', bg='White')
        lblTelefone2.place(x=210, y=75)

        etTelefone2 = Entry(self.windowMain, font='Arial 12', fg=f'{json_ws().getColorTelefone()}', width=20)
        etTelefone2.place(x=210, y=100)

        #Quilometragem
        lblQuilometragem = Label(self.windowMain, font='Arial 12', text='Quilometragem:', bg='White')
        lblQuilometragem.place(x=410, y=75)

        etQuilometragem = Entry(self.windowMain, font='Arial 12', width=20)
        etQuilometragem.place(x=410, y=100)

        #Placa
        lblPlaca = Label(self.windowMain, font='Arial 12', text='Placa:', bg='White')
        lblPlaca.place(x=610, y=75)

        etPlaca = Entry(self.windowMain, font='Arial 12', width=20)
        etPlaca.place(x=610, y=100)

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

        lblTotal = Label(self.windowMain, text='Total:', font='Arial 12', bg='White')
        lblTotal.place(x=610, y=365)

        self.etTotal = Entry(self.windowMain, font='Arial 12 bold', width=15, state='disable')
        self.etTotal.place(x=610, y=390)
        
        #CALCULADORA
        imagem_total = PhotoImage(file=f"src/troco_48.png")
        btTotal = Button(self.windowMain, image=imagem_total, bg='White', bd=0, command=lambda: calcTotal())
        btTotal.imagem = imagem_total
        btTotal.place(x=740, y=365)

        #SALVAR
        imagem_salvar = PhotoImage(file=f"src/salvar_48.png")
        btExibir = Button(self.windowMain, image=imagem_salvar, bg='White', bd=0, command=lambda: save())
        btExibir.imagem = imagem_salvar
        btExibir.place(x=670, y=430)

        #VOLTAR
        imagem_voltar = PhotoImage(file=f"src/voltar_48.png")
        btVoltar = Button(self.windowMain, image=imagem_voltar, bg='White', bd=0, command=lambda: exit(None))
        btVoltar.imagem = imagem_voltar
        btVoltar.place(x=740, y=430)
        
        def calcTotal():
            #VERIFICA SE NÃO HÁ NENHUM CAMPO DE VALOR VAZIO
            verificarCampos()

            #HABILITA O CAMPO
            self.etTotal['state'] = 'normal'

            #LIMPA E CALCULA
            self.etTotal.delete(0, END)
            self.etTotal.insert(0, f"{(float(etObra.get().replace(',', '.')) + float(etPecas.get().replace(',', '.')) + float(etOutros.get().replace(',', '.')))}")

            #DESABILITA O CAMPO
            self.etTotal['state'] = 'disable'

        def verificarCampos():

            #VERIFICA SE TEM NUMERO NOS CAMPOS DE VALORES
            if etObra.get() == '' or etObra.get() == ' ':
                etObra.delete(0, END)
                etObra.insert(0, "0")
            
            if etPecas.get() == '' or etPecas.get() == ' ':
                etPecas.delete(0, END)
                etPecas.insert(0, "0")

            if etOutros.get() == '' or etOutros.get() == ' ':
                etOutros.delete(0, END)
                etOutros.insert(0, "0")

        # Funcoes
        def save():

            # MENSAGEM DE ERROR
            if etVeiculo.get() == '' or etCliente.get() == '':
                messagebox.showerror(
                    'AVISO', 'CAMPOS OBRIGATÓRIOS NÃO ESTÃO PREENCHIDOS')

            else:
                # SALVAR
                if messagebox.askyesno('', 'SALVAR OS?'):
                
                    #VERIFICA OS CAMPOS DE VALORES
                    verificarCampos()

                    bd().insertOS(
                        etDataEntrada.get(),
                        etDataSaida.get(),
                        etCliente.get().upper(),
                        etTelefone1.get(),
                        etTelefone2.get(),
                        etVeiculo.get().upper(),
                        etPlaca.get().upper(),
                        etQuilometragem.get().upper(),
                        stDesc.get("1.0", END).upper(),
                        stLaudo.get("1.0", END).upper(),
                        comboPagamento.get(),
                        comboStatus.get(),
                        float(etObra.get().replace(',','.')),
                        float(etPecas.get().replace(',','.')),
                        float(etOutros.get().replace(',','.'))
                    )

                    messagebox.showinfo('','CADASTRADO COM SUCESSO !')

                    #IMPRIMIR OS
                    if messagebox.askyesno('', 'IMPRIMIR OS?'):
                        #PEGA O ULTIMO ITEM CADASTRADO
                        conteudo = bd().getOS(
                                        bd().getMaiorIdOS()
                                    )

                        #TRATAR DADOS QUE SÃO None
                        for pos, i in enumerate(conteudo):
                            if i == None:
                                conteudo[pos] = ""

                        print_document(
                            'os',
                            conteudo
                        )

                    # LIMPAR
                    clear()

        def clear():
            # LIMPAR
            etDataEntrada.delete(0, END)
            etDataEntrada.insert(0, self.data_atual)

            etDataSaida.delete(0, END)
            etDataSaida.insert(0, self.data_atual)

            etCliente.delete(0, END)
            etTelefone1.delete(0, END)
            etTelefone2.delete(0, END)
            etVeiculo.delete(0, END)
            etPlaca.delete(0, END)
            etQuilometragem.delete(0, END)
            stDesc.delete("1.0", END)
            stLaudo.delete("1.0", END)

            etObra.delete(0, END)
            etObra.insert(0, '0')

            etPecas.delete(0, END)
            etPecas.insert(0, '0')

            etOutros.delete(0, END)
            etOutros.insert(0, '0')
            
            self.etTotal.delete(0, END)
            
        def exit(event):
            #DESTRUIR
            self.windowMain.destroy()
        
        etDataEntrada.focus_force()

        #CAPTURAR TELCAS
        self.windowMain.bind('<Escape>', exit)

        self.windowMain.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.windowMain.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.windowMain.attributes("-fullscreen", self.fullScreenState)
        print(self.toCenterScreen())

#Tela_Cadastrar_OS()