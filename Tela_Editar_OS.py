from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from util import util
from Persistencia import bd
from module_json import json_ws
from tkinter import scrolledtext
from util import util

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
        self.windowMain.geometry(util().toCenterScreen(810, 490))
        self.windowMain.focus_force()
        self.windowMain.title('IGTEC - EDITAR ORDEM DE SERVIÇO')
        self.windowMain['bg'] = 'White'
        #self.windowMain.attributes('-fullscreen', True)  
        #self.fullScreenState = False
        
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
        etObra.place(x=10, y=390)

        lblPecas = Label(self.windowMain, font='Arial 12', text='Valor em Peças:', bg='White')
        lblPecas.place(x=210, y=365)

        etPecas = Entry(self.windowMain, font='Arial 12 bold')
        etPecas.place(x=210, y=390)

        lblOutros = Label(self.windowMain, font='Arial 12', text='Outros Valores:', bg='White')
        lblOutros.place(x=410, y=365)

        etOutros = Entry(self.windowMain, font='Arial 12 bold')
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

        #EDITAR
        imagem_editar = PhotoImage(file=f"src/salvar_editar_48.png")
        btEditar = Button(self.windowMain, image=imagem_editar, bg='White', bd=0, command=lambda: save())
        btEditar.imagem = imagem_editar
        btEditar.place(x=670, y=430)

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

        # Funcoes
        def save():

            # MENSAGEM DE ERROR
            if etVeiculo.get() == '' or etCliente.get() == '':
                messagebox.showerror(
                    'AVISO', 'CAMPOS OBRIGATÓRIOS NÃO ESTÃO PREENCHIDOS')

            else:
                # SALVAR
                if messagebox.askyesno('', 'EDITAR OS?'):
                    
                    #VERIFICA SE NÃO HÁ NENHUM CAMPO DE VALOR VAZIO
                    verificarCampos()

                    bd().updateOS(
                        self.id,
                        etDataEntrada.get(),
                        etDataSaida.get(),
                        etCliente.get().upper(),
                        etTelefone1.get(),
                        etTelefone2.get(),
                        etVeiculo.get().upper(),
                        etPlaca.get().upper(),
                        etQuilometragem.get().upper(),
                        stDesc.get("1.0", END).upper().replace("\n", ""),
                        stLaudo.get("1.0", END).upper().replace("\n", ""),
                        comboPagamento.get(),
                        comboStatus.get(),
                        float(etObra.get().replace(',','.')),
                        float(etPecas.get().replace(',','.')),
                        float(etOutros.get().replace(',','.'))
                    )

                    messagebox.showinfo('','EDITADO COM SUCESSO !')

                    #FECHAR TELA
                    self.windowMain.destroy()

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

        def exit(event):
            self.windowMain.destroy()

        def setDados():
            dados = bd().getOS(self.id)
            
            #TRATAR DADOS QUE SÃO None
            for pos, i in enumerate(dados):
                if i == None:
                    dados[pos] = ""
            
            etDataEntrada.insert(0, dados[1])
            etDataSaida.insert(0, dados[2])
            etCliente.insert(0, dados[3])
            etTelefone1.insert(0, dados[4])
            etTelefone2.insert(0, dados[5])
            etVeiculo.insert(0, dados[6])
            etPlaca.insert(0, dados[7])
            etQuilometragem.insert(0, dados[8])
            stDesc.insert(INSERT, dados[9])
            stLaudo.insert(INSERT, dados[10])
            setPagamento(dados[11])
            setStatus(dados[12])
            etObra.insert(0, str(dados[13]).replace('.',','))
            etPecas.insert(0, str(dados[14]).replace('.',','))
            etOutros.insert(0, str(dados[15]).replace('.',','))
            
            #CALCULAR O TOTAL
            calcTotal()

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
        
        #CAPTURAR TELCAS
        self.windowMain.bind('<Escape>', exit)

        self.windowMain.mainloop()

#Tela_Editar_OS(13)