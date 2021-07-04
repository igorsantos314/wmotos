from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from Persistencia import bd
from module_json import json_ws
from tkinter import scrolledtext

class Tela_Editar_OS:

    def __init__(self, id):
        # DATA ATUAL
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year
        self.data_atual = f'{self.day}/{self.month}/{self.year}'

        self.id = id
        
        # OBEJTO OS
        self.window()

    def window(self):

        self.windowMain = Tk()
        self.windowMain.resizable(False, False)
        self.windowMain.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.windowMain.title('EDITAR ORDEM DE SERVIÇO')
        self.windowMain['bg'] = 'White'

        # Data
        lblDataEntrada = Label(self.windowMain, text='Data de Entrada:', font='Arial 12', bg='White')
        lblDataEntrada.place(x=10, y=10)
        
        etDataEntrada = Entry(self.windowMain, font='Arial 12', width=20)
        etDataEntrada.place(x=10, y=35)

        lblDataSaida = Label(self.windowMain, text='Data de Saida:', font='Arial 12', bg='White')
        lblDataSaida.place(x=210, y=10)

        etDataSaida = Entry(self.windowMain, font='Arial 12', width=20)
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
        etObra.place(x=10, y=390)

        lblPecas = Label(self.windowMain, font='Arial 12', text='Valor em Peças:', bg='White')
        lblPecas.place(x=210, y=365)

        etPecas = Entry(self.windowMain, font='Arial 12 bold')
        etPecas.place(x=210, y=390)

        lblOutros = Label(self.windowMain, font='Arial 12', text='Outros Valores:', bg='White')
        lblOutros.place(x=410, y=365)

        etOutros = Entry(self.windowMain, font='Arial 12 bold')
        etOutros.place(x=410, y=390)

        #EDITAR
        imagem_editar = PhotoImage(file=f"src/salvar_editar_48.png")
        btEditar = Button(self.windowMain, image=imagem_editar, bg='White', command=lambda: save())
        btEditar.imagem = imagem_editar
        btEditar.place(x=670, y=430)

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
                if messagebox.askyesno('', 'EDITAR OS?'):

                    bd().updateOS(
                        self.id,
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

                    messagebox.showinfo('','EDITADO COM SUCESSO !')

                #FECHAR TELA
                self.windowMain.destroy()

        def clear():
            # LIMPAR
            etDataEntrada.delete(0, END)
            etDataSaida.delete(0, END)
            etCliente.delete(0, END)
            etVeiculo.delete(0, END)
            #etDesc.delete(0, END)
            #etLaudo.delete(0, END)
            etObra.delete(0, END)
            etPecas.delete(0, END)
            etOutros.delete(0, END)

        def exit():
            self.windowMain.destroy()

        def setDados():
            dados = bd().getOS(self.id)[0]

            etDataEntrada.insert(0, dados[1])
            etDataSaida.insert(0, dados[2])
            etCliente.insert(0, dados[3])
            etTelefone.insert(0, dados[4])
            etVeiculo.insert(0, dados[5])
            stDesc.insert(INSERT, dados[6])
            stLaudo.insert(INSERT, dados[7])
            setPagamento(dados[8])
            setStatus(dados[9])
            etObra.insert(0, str(dados[10]).replace('.',','))
            etPecas.insert(0, str(dados[11]).replace('.',','))
            etOutros.insert(0, str(dados[12]).replace('.',','))

        def setPagamento(pag):

            for pos, i in enumerate(comboPagamento['values']):
                if i == pag:
                    comboPagamento.current(pos)

        def setStatus(status):
            for pos, i in enumerate(comboStatus['values']):
                if i == status:
                    comboStatus.current(pos)
        
        #SETAR DADOS
        setDados()

        self.windowMain.bind("<F11>", self.toggleFullScreen)
        self.windowMain.bind("<Escape>", self.quitFullScreen)

        self.windowMain.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.windowMain.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.windowMain.attributes("-fullscreen", self.fullScreenState)
        self.windowMain.geometry('810x490')

Tela_Editar_OS(17)