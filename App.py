from tkinter import ttk
from tkinter import *
import os
from tkinter import messagebox
from datetime import date
import json
from datetime import datetime
import sqlite3
from tkinter import scrolledtext
import shutil

class Menu_Principal:

    def __init__(self) -> None:
        #self.validationConnection()
        self.windowMain()

    """def validationConnection(self):
        try:
            if validation().getStatus() == "True":
                self.windowMain()
            else:
                self.windowError = Tk()
                self.windowError.resizable(False, False)
                self.windowError.title('Opss')
                self.windowError.geometry(util().toCenterScreen(250, 30))
                self.windowError['bg'] = 'Black'
                
                lbl = Label(text='ACESSO NEGADO !', font='Arial 12 bold', fg='Red', bg='Black')
                lbl.pack()

                self.windowError.mainloop()
        except:
            pass
    """
    def windowMain(self):
        # Creating tkinter window
        self.window = Tk()
        self.window.resizable(False, False)
        self.window.geometry(util().toCenterScreen(810, 580))
        self.window.focus_force()
        
        self.window.title('IGTEC - By:Igor Santos')
        self.window['bg'] = 'White'

        #LOGO
        imagem = PhotoImage(file=f"{json_ws().getPathLogo()}")
        w = Label(self.window, image=imagem)
        w.imagem = imagem
        w.place(x=0, y=-5)

        #NOVA ORDEM DE SERVIÇO
        imagem_new_os = PhotoImage(file=f"src/new_os.png")
        btNewOS = Button(self.window, image=imagem_new_os, bg='White', command=lambda:open('Nova'))
        btNewOS.imagem = imagem_new_os
        btNewOS.place(x=10, y=10)

        #EXIBIR ORDENS DE SERVIÇO
        imagem_exibir = PhotoImage(file=f"src/exibir_os.png")
        btExibir = Button(self.window, image=imagem_exibir, bg='White', command=lambda:open('Exibir'))
        btExibir.imagem = imagem_exibir
        btExibir.place(x=120, y=10)

        #EXIBIR ORDENS DE SERVIÇO
        imagem_contabilidade = PhotoImage(file=f"src/cont.png")
        btCont = Button(self.window, image=imagem_contabilidade, bg='White', command=lambda:open('C_Total'))
        btCont.imagem = imagem_contabilidade
        btCont.place(x=230, y=10)

        #BACKUP
        imagem_backup = PhotoImage(file=f"src/backup.png")
        btBackup = Button(self.window, image=imagem_backup, bg='White', command=lambda:open('Backup'))
        btBackup.imagem = imagem_backup
        btBackup.place(x=340, y=10)

        #CONFIGURAÇÕES
        imagem_config = PhotoImage(file=f"src/config.png")
        btConfig = Button(self.window, image=imagem_config, bg='White', command=lambda:open('Config'))
        btConfig.imagem = imagem_config
        btConfig.place(x=450, y=10)

        #SAIR
        imagem_sair = PhotoImage(file=f"src/sair.png")
        btSair = Button(self.window, image=imagem_sair, bg='White', command=lambda:self.window.destroy())
        btSair.imagem = imagem_sair
        btSair.place(x=560, y=10)

        #FECHAR MENU PARA CONTROLE DE TELAS
        def open(w):
            
            #FECHAR MENU
            self.window.destroy()

            if w == 'Nova':
                #ABRIR JANELA
                Tela_Cadastrar_OS()

                #REABRIR MENU
                Menu_Principal()

            elif w == 'Exibir':
                #ABRIR JANELA
                consulta()

                #REABRIR MENU
                Menu_Principal()
            
            elif w == 'C_Total':
                #ABRIR JANELA
                Contabilidade()

                #REABRIR MENU
                Menu_Principal()

            elif w == 'Backup':
                #ABRIR JANELA
                Backup_BD()

                #REABRIR MENU
                Menu_Principal()

            elif w == 'Config':
                #ABRIR JANELA
                Config()
                
                #REABRIR MENU
                Menu_Principal()

        self.window.mainloop()
        
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
        self.window.geometry(self.toCenterScreen())

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
            etDataEntrada.insert(0, self.data_atual)

            etDataSaida.delete(0, END)
            etDataSaida.insert(0, self.data_atual)

            etCliente.delete(0, END)
            etTelefone.delete(0, END)
            etVeiculo.delete(0, END)
            stDesc.delete("1.0", END)
            stLaudo.delete("1.0", END)

            etObra.delete(0, END)
            etObra.insert(0, '0')

            etPecas.delete(0, END)
            etPecas.insert(0, '0')

            etOutros.delete(0, END)
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
        self.windowMain.title('EDITAR ORDEM DE SERVIÇO')
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

        #self.windowMain.bind("<F11>", self.toggleFullScreen)
        #self.windowMain.bind("<Escape>", self.quitFullScreen)

        self.windowMain.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.windowMain.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.windowMain.attributes("-fullscreen", self.fullScreenState)
        self.windowMain.geometry('810x490')

class consulta:

    def __init__(self) -> None:
        self.window()
        
    def window(self):
        # Creating tkinter self.windowMain 
        self.windowMain = Tk()
        self.windowMain.resizable(False, False)
        self.windowMain.geometry(util().toCenterScreen(993, 480))
        self.windowMain.focus_force()
        self.windowMain.title('CONSULTAR OS')
        self.windowMain['bg'] = 'White'

        #BUSCAR
        lblBuscar = Label(self.windowMain, text='BUSCAR:', font='Arial 13', bg='White')
        lblBuscar.place(x=440, y=10)

        etBuscar = Entry(self.windowMain, width=59, font='Arial 12')
        etBuscar.place(x=440, y=40)

        #EDITAR
        imagem_editar = PhotoImage(file=f"src/editar_48.png")
        btEditar = Button(self.windowMain, image=imagem_editar, bg='White', command=lambda: editar())
        btEditar.imagem = imagem_editar
        btEditar.place(x=10, y=10)

        #DELETAR
        imagem_del = PhotoImage(file=f"src/deletar_48.png")
        btDel = Button(self.windowMain, image=imagem_del, bg='White', command=lambda: deletar())
        btDel.imagem = imagem_del
        btDel.place(x=80, y=10)

        #IMPRIMIR
        imagem_imprimir = PhotoImage(file=f"src/impressora_48.png")
        btImprimir = Button(self.windowMain, image=imagem_imprimir, bg='White', command=lambda: imprimir())
        btImprimir.imagem = imagem_imprimir
        btImprimir.place(x=150, y=10)

        #BUSCAR
        imagem_buscar = PhotoImage(file=f"src/buscar_48.png")
        btBuscar = Button(self.windowMain, image=imagem_buscar, bg='White', command=lambda: buscar())
        btBuscar.imagem = imagem_buscar
        btBuscar.place(x=220, y=10)

        #LIMPAR
        imagem_limpar = PhotoImage(file=f"src/limpar_48.png")
        btLimpar = Button(self.windowMain, image=imagem_limpar, bg='White', command=lambda: limpar())
        btLimpar.imagem = imagem_limpar
        btLimpar.place(x=290, y=10)

        #SAIR
        imagem_sair = PhotoImage(file=f"src/voltar_48.png")
        btSair = Button(self.windowMain, image=imagem_sair, bg='White', command=lambda: self.windowMain.destroy())
        btSair.imagem = imagem_sair
        btSair.place(x=360, y=10)

        #STATUS
        lblStatus = Label(text='STATUS:', bg='White')
        lblStatus.place(x=10, y=70)

        #ESPERA
        imagem_espera = PhotoImage(file=f"src/espera_48.png")
        btEspera = Button(self.windowMain, image=imagem_espera, bg='White', command=lambda: statusEspera())
        btEspera.imagem = imagem_espera
        btEspera.place(x=10, y=90)

        #EM ANDAMENTO
        imagem_andamento = PhotoImage(file=f"src/andamento_48.png")
        btAndamento = Button(self.windowMain, image=imagem_andamento, bg='White', command=lambda: statusAndamento())
        btAndamento.imagem = imagem_andamento
        btAndamento.place(x=80, y=90)

        #CONCLUIDO
        imagem_concluido = PhotoImage(file=f"src/concluido_48.png")
        btConcluido = Button(self.windowMain, image=imagem_concluido, bg='White', command=lambda: statusConcluido())
        btConcluido.imagem = imagem_concluido
        btConcluido.place(x=150, y=90)

        #FORMA DE PAGAMENTO
        lblPagamento = Label(text='FORMA DE PAGAMENTO:', bg='White')
        lblPagamento.place(x=220, y=70)
        
        #DINHEIRO
        imagem_dinheiro = PhotoImage(file=f"src/dinheiro_48.png")
        btDinheiro = Button(self.windowMain, image=imagem_dinheiro, bg='White', command=lambda: pagamentoDinheiro())
        btDinheiro.imagem = imagem_dinheiro
        btDinheiro.place(x=220, y=90)

        #CARTÃO
        imagem_cartao = PhotoImage(file=f"src/cartao_48.png")
        btCartao = Button(self.windowMain, image=imagem_cartao, bg='White', command=lambda: pagamentoCartao())
        btCartao.imagem = imagem_cartao
        btCartao.place(x=290, y=90)

        #PIX
        imagem_transferencia = PhotoImage(file=f"src/transferencia_48.png")
        btTransferencia = Button(self.windowMain, image=imagem_transferencia, bg='White', command=lambda: pagamentoPix())
        btTransferencia.imagem = imagem_transferencia
        btTransferencia.place(x=360, y=90)

        #OUTRO
        imagem_transferencia = PhotoImage(file=f"src/outro_48.png")
        btTransferencia = Button(self.windowMain, image=imagem_transferencia, bg='White', command=lambda: pagamentoOutro())
        btTransferencia.imagem = imagem_transferencia
        btTransferencia.place(x=430, y=90)

        #TREEVIEW
        style = ttk.Style(self.windowMain)
        style.theme_use('clam')

        style.configure(
            "Treeview",
            background="Silver",
            fieldbackground='Silver'
        )

        style.map("Treeview", background=[('selected', '#00DB73')], foreground=[('selected', 'Black')])

        # Using treeview widget 
        treev2 = ttk.Treeview(self.windowMain, selectmode ='browse', height=14) 

        # Calling pack method w.r.to treeview 
        treev2.place(x=10, y=160)

        # Constructing vertical scrollbar 
        # with treeview 
        verscrlbar = ttk.Scrollbar(self.windowMain, 
                                orient ="vertical", 
                                command = treev2.yview) 

        # scrollbar 
        verscrlbar.pack(side ='right', fill ='x') 

        # Configuring treeview 
        treev2.configure(xscrollcommand = verscrlbar.set) 

        # Defining number of columns 
        treev2["columns"] = ("1", "2", "3", "4", "5", "8", "9", "10", "11", "12", "13") 

        # Defining heading 
        treev2['show'] = 'headings'

        # Assigning the width and anchor to the 
        # respective columns 
        treev2.column("1", width = 60, anchor ='c') 
        treev2.column("2", width = 90, anchor ='se') 
        treev2.column("3", width = 90, anchor ='se') 
        treev2.column("4", width = 120, anchor ='se')
        treev2.column("5", width = 90, anchor ='se') 
        treev2.column("8", width = 90, anchor ='se')
        treev2.column("9", width = 120, anchor ='se') 
        treev2.column("10", width = 75, anchor ='se')
        treev2.column("11", width = 75, anchor ='se')
        treev2.column("12", width = 75, anchor ='se')
        treev2.column("13", width = 75, anchor ='se')

        # Assigning the heading names to the 
        # respective columns 
        treev2.heading("1", text ="Id") 
        treev2.heading("2", text ="Data Entrada") 
        treev2.heading("3", text ="Data Saida")
        treev2.heading("4", text ="Cliente")
        treev2.heading("5", text ="Veiculo")
        treev2.heading("8", text ="Forma de Pagamento")
        treev2.heading("9", text ="Status")
        treev2.heading("10", text ="M. de Obra")
        treev2.heading("11", text ="Peças")
        treev2.heading("12", text ="Outros")
        treev2.heading("13", text ="Total")
        
        def getId():
            if len(treev2.selection()) == 0:
                messagebox.showwarning('','POR FAVOR SELECIONE UMA OS')
                return False
            else:
                itemSelecionado = treev2.selection()[0]

                #PEGAR VALORES
                id = int(treev2.item(itemSelecionado, "values")[0])
                
                return id
            #Deletar Item
            #treev2.delete(itemSelecionado)

        def getAll():
            #VARRER LISTA E ADICIONAR NA TABELA
            for i in bd().getAllOS():
                total = f"{(i[10] + i[11] + i[12]):.2f}"
                treev2.insert("", 'end', text ="L1", values =(i[0], i[1], i[2], i[3], i[5], i[8], i[9], i[10], i[11], i[12], total))

        def buscar():
            
            #LIMPA A TABELA
            limparTabela()

            #VARRER LISTA E ADICIONAR NA TABELA
            for i in bd().getNomeVeiculoOS(etBuscar.get().upper()):
                total = f"{(i[10] + i[11] + i[12]):.2f}"
                treev2.insert("", 'end', text ="L1", values =(i[0], i[1], i[2], i[3], i[5], i[8], i[9], i[10], i[11], i[12], total))

        def limpar():
            #LIMPAR CAMPO DE CONSULTA
            etBuscar.delete(0, END)

            #LIMPAR TABELA
            limparTabela()

        def imprimir():
            
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                #PEGAR A TUPLA
                conteudo = bd().getOS(id)[0]

                #IMPRIMIR
                print_document(conteudo)
        
        def editar():
            
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                #FECHHA A JANELA
                self.windowMain.destroy()

                #ABRE JANELA DE EDITAR
                Tela_Editar_OS(id)

                #REABRE A TELA DE EXIBIR
                consulta()

        def deletar():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:

                if messagebox.askyesno('', 'DESEJA APAGAR A OS?') == True:
                    #APGAR NO BANCO DE DADOS
                    bd().delOS(id)

                    messagebox.showinfo('','DELETADO COM SUCESSO!')

            #LIMPA TUDO
            limparTabela()

            #CARREGA ALTERAÇÕES
            getAll()

        #--- STATUS ---
        def statusConcluido():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updateStatusConcluido(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                buscar()
        
        def statusEspera():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updateStatusEspera(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                buscar()

        def statusAndamento():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updateStatusAndamento(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                buscar()

        #--- FORMA DE PAGAMENTO ---
        def pagamentoDinheiro():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updatePagamentoDinheiro(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                buscar()

        def pagamentoCartao():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updatePagamentoCartao(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                buscar()

        def pagamentoPix():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updatePagamentoPix(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                buscar()

        def pagamentoOutro():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updatePagamentoOutro(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                buscar()

        def limparTabela():
            treev2.delete(*treev2.get_children())

        #Povoar Tabela
        getAll()

        self.windowMain.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.windowMain.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.windowMain.attributes("-fullscreen", self.fullScreenState)
        self.windowMain.geometry('993x480')

class bd:

    def __init__(self):

        #LISTA DE MESES
        self.months = ['JANEIRO', 'FEVEREIRO', 'MARCO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']

        self.conection = sqlite3.connect(json_ws().getPathBd())
        self.cur = self.conection.cursor()

    def insertOS(self, data_entrada, saida, nome_cliente, telefone, veiculo, desc, laudo_tecnico, forma_pagamento, status, valor_mao_obra, valor_pecas, valor_outros):

        #INSERIR DADOS NA TABELA GASTOS
        command = f'INSERT INTO ordem_servico(entrada, saida, cliente, telefone, veiculo, descricao, laudo, pagamento, status, mao_de_obra, valor_de_pecas, valor_outros) VALUES("{data_entrada}", "{saida}", "{nome_cliente}", "{telefone}", "{veiculo}", "{desc}", "{laudo_tecnico}", "{forma_pagamento}", "{status}", {valor_mao_obra}, {valor_pecas}, {valor_outros})'
        
        self.cur.execute(command)
        self.conection.commit()

    def delOS(self, id):
        #DELETAR OS
        command = f'DELETE FROM ordem_servico WHERE id={id}'
        
        self.cur.execute(command)
        self.conection.commit()

    def updateOS(self, id, data_entrada, saida, nome_cliente, telefone, veiculo, desc, laudo_tecnico, forma_pagamento, status, valor_mao_obra, valor_pecas, valor_outros):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET entrada='{data_entrada}', saida='{saida}', cliente='{nome_cliente}', telefone='{telefone}', veiculo='{veiculo}', descricao='{desc}', laudo='{laudo_tecnico}', pagamento='{forma_pagamento}', status='{status}', mao_de_obra={valor_mao_obra}, valor_de_pecas={valor_pecas}, valor_outros={valor_outros} WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updateStatusConcluido(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET status='CONCLUIDO' WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updateStatusAndamento(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET status='EM ANDAMENTO' WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updateStatusEspera(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET status='EM ESPERA' WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updatePagamentoDinheiro(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET pagamento='DINHEIRO' WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updatePagamentoCartao(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET pagamento='CARTÃO' WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updatePagamentoPix(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET pagamento='PIX' WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updatePagamentoOutro(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET pagamento='OUTRO' WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def getAllOS(self):
        show = "SELECT * FROM ordem_servico"
        self.cur.execute(show)

        #RETORNA LISTA DE OS
        return self.cur.fetchall()

    def getOS(self, id):
        show = f"SELECT * FROM ordem_servico WHERE id={id}"
        self.cur.execute(show)

        #RETORNA LISTA DE OS
        return self.cur.fetchall()

    def getNomeVeiculoOS(self, str):

        show = f"SELECT * FROM ordem_servico WHERE cliente LIKE '%{str}%' OR veiculo LIKE '%{str}%'"
        self.cur.execute(show)

        #RETORNA LISTA DE OS
        return self.cur.fetchall()

    # --- CONTABILIDADE ---
    def getAllMaoObra(self):

        show = f"SELECT sum(mao_de_obra) FROM ordem_servico WHERE status='CONCLUIDO'"
        self.cur.execute(show)

        valor = self.cur.fetchall()[0][0]

        if  valor == None:
            return 0

        #RETORNA O VALOR TOTAL
        return valor

    def getContabilidadeDia(self, data):

        show = f"SELECT sum(mao_de_obra) FROM ordem_servico WHERE saida='{data}' and status='CONCLUIDO'"
        self.cur.execute(show)

        valor = self.cur.fetchall()[0][0]

        if  valor == None:
            return 0

        #RETORNA O VALOR DO DIA
        return valor

    def getContabilidadeMes(self, data):

        show = f"SELECT sum(mao_de_obra) FROM ordem_servico WHERE saida LIKE '%{data}' and status='CONCLUIDO'"
        self.cur.execute(show)

        valor = self.cur.fetchall()[0][0]

        if  valor == None:
            return 0

        #RETORNA O VALOR DO MÊS
        return valor

    def getContabilidadeDinheiro(self):

        show = f"SELECT sum(mao_de_obra) FROM ordem_servico WHERE pagamento='DINHEIRO'"
        self.cur.execute(show)

        valor = self.cur.fetchall()[0][0]

        if  valor == None:
            return 0

        #RETORNA O VALOR DO MÊS
        return valor

    def getContabilidadeCartao(self):

        show = f"SELECT sum(mao_de_obra) FROM ordem_servico WHERE pagamento='CARTÃO'"
        self.cur.execute(show)

        valor = self.cur.fetchall()[0][0]

        if  valor == None:
            return 0

        #RETORNA O VALOR DO MÊS
        return valor

    def getContabilidadePix(self):

        show = f"SELECT sum(mao_de_obra) FROM ordem_servico WHERE pagamento='PIX'"
        self.cur.execute(show)

        valor = self.cur.fetchall()[0][0]

        if  valor == None:
            return 0

        #RETORNA O VALOR DO MÊS
        return valor

    # --- BACKUP ---
    def toJson(self):

        for os in self.getAllOS():
            pass

class print_document:

    def __init__(self, conteudo):
        
        self.caminho = "{}\\imprimir.txt".format(os.getcwd())
        
        # CREAR ARQ DE IMPRESSÃO
        self.createArqPrint(conteudo)

        # IMPRIMIR
        self.comprovantePrint()

    def setConteudoToPrint(self, conteudo):

        head = '                           ORDEM DE SERVIÇO - W MOTOS  \n'
        head += "________________________________________________________________________________\n"
        head += "CIDADE:                BEJO JARDIM\n"
        head += "RUA:                   JOÃO BATISTA SENHORINHO\n"
        head += "NÚMERO:                155\n"
        head += "PONTO DE REFERÊNCIA:   AVENIDA DO SESC\n"
        head += "WHATSAPP:              (81) 98250-0763\n"
        head += "________________________________________________________________________________\n\n"

        body  = "DADOS DA ORDEM DE SERVIÇO\n"
        body += "________________________________________________________________________________\n"
        body += f"ID:                             {conteudo[0]} \n"
        body += f"DATA DE ENTRADA:                {conteudo[1]} \n"   
        body += f"DATA DE SAIDA:                  {conteudo[2]} \n"    
        body += f"NOME DO CLIENTE:                {conteudo[3]} \n"   
        body += f"TELEFONE:                       {conteudo[4]} \n"     
        body += f"VEICULO:                        {conteudo[5]} \n\n" 

        body += "________________________________________________________________________________\n"
        body += "DESCRIÇÃO DO CLIENTE:\n"
        body += f"     {conteudo[6]}"

        body += "________________________________________________________________________________\n"
        body += "LAUDO TECNICO:\n"
        body += f"     {conteudo[7]}"
        body += "________________________________________________________________________________\n\n"
        
        body += f"FORMA DE PAGAMENTO:             {conteudo[8]} \n"
        body += f"STATUS:                         {conteudo[9]} \n"
        body += f"VALOR DE MÃO DE OBRA:           R$ {conteudo[10]:.2f} \n"
        body += f"VALOR EM PEÇAS:                 R$ {conteudo[11]:.2f}\n"
        body += f"OUTROS VALORES:                 R$ {conteudo[12]:.2f}\n"
        body += f"TOTAL:                          R$ {(conteudo[10] + conteudo[11] + conteudo[12]):.2f}\n"

        body += "________________________________________________________________________________\n\n"

        bottom = "DATA E HORA IMPRESSÃO: " + datetime.now().strftime('%d/%m/%Y %H:%M') + "\n\n\n\n\n"

        bottom += "                  ___________________________________________                    \n"
        bottom += "                           Assinatura do Responsável\n\n\n\n\n"

        bottom += "                  ___________________________________________                    \n"
        bottom += "                             Assinatura do Cliente"
        
        return f"{head}{body}{bottom}"

    def createArqPrint(self, conteudo):

        #ESCRVE OS DADS NO ARQUIVO DE IMPRESSÃO
        arquivo = open(self.caminho, "w")
        arquivo.write(self.setConteudoToPrint(conteudo))

        arquivo.close()

    def comprovantePrint(self):
        try:
            # COMANDO DE IMPRESSÃO
            os.startfile(self.caminho, "print")
            messagebox.showinfo('','IMPRESSÃO REALIZADA')
            
        except:
            messagebox.showerror('','ERROR[mdo_print:80] NÃO FOI POSSÍVEL REALIZAR A IMPRESSÃO')

class json_ws:

    def __init__(self):
        self.caminho = 'ws_motos_config.json'
        self.dict = self.ler()

    def ler(self):
        #LER ARQUIVO
        with open(self.caminho, 'r', encoding='utf-8') as f:
            return json.load(f)

    def escrever(self, dict):
        #ESCREVER DICIONÁRIO NO JSON
        with open(self.caminho, 'w', encoding='utf-8') as f:
            json.dump(dict, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

    def atualizar(self):
        #PEGAR JSON E SALVA EM UM DICT
        self.dict_finance = self.ler()

    def getPathLogo(self):
        return f"{os.getcwd()}/{self.dict['path_logo']}"

    def getPathBd(self):
        return f"{os.getcwd()}/{self.dict['path_bd']}"

    def getColorCliente(self):
        return self.dict['color_cliente']

    def getColorVeiculo(self):
        return self.dict['color_veiculo']

    def getColorTelefone(self):
        return self.dict['color_telefone']

    def getWidthScreen(self):
        return self.dict['width_screen']

    def getHeightScreen(self):
        return self.dict['heigth_screen']

    def getPwCont(self):
        return self.dict['pw_cont']
    
    def getPwConfig(self):
        return self.dict['pw_config']

class Contabilidade:

    def __init__(self):
        # DATA ATUAL
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year
        self.data_atual = f'{self.day}/{self.month}/{self.year}'

        self.id = id

        self.login()

    def login(self):

        windowLogin = Tk()
        windowLogin.resizable(False, False)
        windowLogin.geometry(util().toCenterScreen(160,70))
        windowLogin.focus_force()
        windowLogin.title('')
        
        lblSenha = Label(windowLogin, text='Senha:')
        lblSenha.pack()

        etSenha = Entry(windowLogin, font='Arial 12 bold', show='*')
        etSenha.pack()

        def verify(event):
            
            if etSenha.get() == json_ws().getPwCont():
                #DESTRUIR JANELA
                windowLogin.destroy()

                #CHAMAR CONTABILIDADE
                self.window()
            else:
                messagebox.showerror('', 'SENHA INCORRETA !')
                windowLogin.destroy()

        etSenha.focus_force()
        windowLogin.bind('<Return>', verify)

        windowLogin.mainloop()

    def window(self):

        self.windowMain = Tk()
        self.windowMain.resizable(False, False)
        self.windowMain.geometry(util().toCenterScreen(730, 500))
        self.windowMain.focus_force()
        self.windowMain.title('CONTABILIDADE W MOTOS')
        #self.windowMain.attributes('-fullscreen', True)  
        #self.fullScreenState = False

        #Data
        lblData = Label(self.windowMain, text='Dia:')
        lblData.place(x=10, y=20)

        comboData = ttk.Combobox(self.windowMain, width = 8) 

        comboData['values'] = tuple(['{}'.format(i) for i in range(1, 32)])
        comboData.current(self.day-1)
        comboData.place(x=10, y=40)

        #Mes
        lblMes = Label(self.windowMain, text='Mês:')
        lblMes.place(x=130, y=20)

        comboMes = ttk.Combobox(self.windowMain, width = 8) 

        comboMes['values'] = tuple(['{}'.format(i) for i in range(1, 13)])
        comboMes.current(self.month-1)
        comboMes.place(x=130, y=40)

        #Ano
        lblAno = Label(self.windowMain, text='Ano:')
        lblAno.place(x=250, y=20)

        comboAno = ttk.Combobox(self.windowMain, width = 8) 

        comboAno['values'] = tuple(['{}'.format(i) for i in range(2021, 2051)])
        comboAno.current(self.year - 2021)
        comboAno.place(x=250, y=40)

        #CONTANIER
        lblContDia = Label(self.windowMain, text='RECEITA DIA', font='Arial 15', width=20, height=2, bg='#fee440')
        lblContDia.place(x=10, y=80)

        contValorDia = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, bg='White')
        contValorDia.place(x=10, y=132)

        lblContMes = Label(self.windowMain, text='RECEITA MÊS', font='Arial 15', width=20, height=2, bg='#00bbf9')
        lblContMes.place(x=250, y=80)

        contValorMes = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, bg='White')
        contValorMes.place(x=250, y=132)

        lblContTotal = Label(self.windowMain, text='RECEITA TOTAL', font='Arial 15', width=20, height=2, bg='#00f5d4')
        lblContTotal.place(x=490, y=80)

        contValorTotal = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, bg='White')
        contValorTotal.place(x=490, y=132)

        #FORMA DE PAGAMENTO
        lblContDinheiro = Label(self.windowMain, text='DINHEIRO', font='Arial 15', width=20, height=2, bg='#ee6055')
        lblContDinheiro.place(x=10, y=232)

        contValorDinheiro = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, bg='White')
        contValorDinheiro.place(x=10, y=284)

        lblContCartao = Label(self.windowMain, text='CARTÃO', font='Arial 15', width=20, height=2, bg='#60d394')
        lblContCartao.place(x=250, y=232)

        contValorCartao = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, bg='White')
        contValorCartao.place(x=250, y=284)

        lblContPix = Label(self.windowMain, text='PIX/TED', font='Arial 15', width=20, height=2, bg='#aaf683')
        lblContPix.place(x=490, y=232)

        contValorPix = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, bg='White')
        contValorPix.place(x=490, y=284)

        #RESERVA DE EMERGÊNCIA
        lblReservaMes = Label(self.windowMain, text='RESERVA DO MÊS', font='Arial 15', width=20, height=2, bg='#836FFF', fg='White')
        lblReservaMes.place(x=10, y=384)

        contReservaMes = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, bg='White')
        contReservaMes.place(x=10, y=436)

        lblReservaTotal = Label(self.windowMain, text='RESERVA TOTAL', font='Arial 15', width=20, height=2, bg='#00CED1', fg='White')
        lblReservaTotal.place(x=250, y=384)

        contReservaTotal = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, bg='White')
        contReservaTotal.place(x=250, y=436)

        def setValeusData():
            #SETAR O VALOR TOTAL
            valor_total = bd().getAllMaoObra()
            contValorTotal['text'] = f'R$ {valor_total:.2f}'.replace('.', ',')

            #SETAR O VALOR MÊS
            m = f'/{comboMes.get()}/{comboAno.get()}'
            valor_mes = bd().getContabilidadeMes(m)
            contValorMes['text'] = f'R$ {valor_mes:.2f}'.replace('.', ',')
            
            #SETAR O VALOR DIA
            d = f'{comboData.get()}/{comboMes.get()}/{comboAno.get()}'
            contValorDia['text'] = f'R$ {bd().getContabilidadeDia(d):.2f}'.replace('.', ',')
            
            #SETAR RESERVA MENSAL
            contReservaMes['text'] = f'R$ {(valor_mes*0.10):.2f}'.replace('.', ',')

            #SETAR PROJEÇÃO TOTAL
            contReservaTotal['text'] = f'R$ {(valor_total*0.10):.2f}'.replace('.', ',')

        def setValuesPagamento():
            #DINHEIRO
            contValorDinheiro['text'] = f'R$ {bd().getContabilidadeDinheiro():.2f}'.replace('.', ',')

            #CARTAO
            contValorCartao['text'] = f'R$ {bd().getContabilidadeCartao():.2f}'.replace('.', ',')

            #PIX
            contValorPix['text'] = f'R$ {bd().getContabilidadePix():.2f}'.replace('.', ',')

        #EDITAR
        imagem_buscar = PhotoImage(file=f"src/buscar_48.png")
        btBuscar = Button(self.windowMain, image=imagem_buscar, bg='White', command=lambda: setValeusData())
        btBuscar.imagem = imagem_buscar
        btBuscar.place(x=350, y=10)
        
        #VOLTAR
        imagem_voltar = PhotoImage(file=f"src/voltar_48.png")
        btVoltar = Button(self.windowMain, image=imagem_voltar, bg='White', command=lambda: self.windowMain.destroy())
        btVoltar.imagem = imagem_voltar
        btVoltar.place(x=420, y=10)

        #SETAR VALORES
        setValeusData()
        setValuesPagamento()
        
        #self.windowMain.bind("<F11>", self.toggleFullScreen)
        #self.windowMain.bind("<Escape>", self.quitFullScreen)

        self.windowMain.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.windowMain.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.windowMain.attributes("-fullscreen", self.fullScreenState)
        self.windowMain.geometry('730x460')

class Config:

    def __init__(self):
        self.caminho = 'ws_motos_config.json'
        self.dict = self.ler()

        # OBEJTO OS
        self.login()

    def ler(self):
        #LER ARQUIVO
        with open(self.caminho, 'r', encoding='utf-8') as f:
            return json.load(f)

    def escrever(self, dict):
        #ESCREVER DICIONÁRIO NO JSON
        with open(self.caminho, 'w', encoding='utf-8') as f:
            json.dump(dict, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

    def login(self):

        windowLogin = Tk()
        windowLogin.resizable(False, False)
        windowLogin.geometry(util().toCenterScreen(160,70))
        windowLogin.focus_force()
        windowLogin.title('')
        
        lblSenha = Label(windowLogin, text='Senha:')
        lblSenha.pack()

        etSenha = Entry(windowLogin, font='Arial 12 bold', show='*')
        etSenha.pack()

        def verify(event):
            
            if etSenha.get() == json_ws().getPwConfig():
                #DESTRUIR JANELA
                windowLogin.destroy()

                #CHAMAR CONTABILIDADE
                self.window()
            else:
                messagebox.showerror('', 'SENHA INCORRETA !')
                windowLogin.destroy()

        etSenha.focus_force()
        windowLogin.bind('<Return>', verify)

        windowLogin.mainloop()

    def window(self):

        self.windowMain = Tk()
        self.windowMain.geometry(util().toCenterScreen(300, 200))
        self.windowMain.resizable(False, False)  
        self.windowMain.title('CONFIGURAÇÕES')
        self.windowMain.focus_force()
        self.windowMain['bg'] = 'White'

        lbl = Label(text='TIPO DE CONFIGURAÇÃO', bg='white')
        lbl.pack()

        comboConfig = ttk.Combobox(self.windowMain, font='Arial 10', width=18)

        comboConfig['values'] = tuple([i for i in self.dict])
        comboConfig.current(0)
        comboConfig.pack()

        bt = Button(self.windowMain, font='Arial 10', text='CONSULTAR', command=lambda:consulta())
        bt.pack(pady=10)
        
        lbl = Label(text='VALORES:', bg='white')
        lbl.pack()

        etValue = Entry(self.windowMain, font='Arial 10')
        etValue.pack()

        def consulta():
            #LIMPAR CAMPO
            etValue.delete(0, END)

            #EXIBIR INFORMAÇÕES
            etValue.insert(
                0, 
                self.dict[comboConfig.get()])

        def save():
           
            if messagebox.askyesno('','DESEJA SALVAR?'):
                 #MODIFICAR NO DICIONÁRIO
                self.dict[comboConfig.get()] = etValue.get()

                #SALVAR
                self.escrever(self.dict)

                messagebox.showinfo('','SALVO !!')
        
        btS = Button(self.windowMain, font='Arial 10', text='SALVAR', command=lambda:save())
        btS.pack(pady=10)

        comboConfig.focus_force()

        self.windowMain.mainloop()

class Backup_BD:

    def __init__(self):
        
        # DATA ATUAL
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year

        self.data_atual = f'{self.day}-{self.month}-{self.year}'
        self.origem = 'wmotos.db'
        self.list_devices = ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        self.list_color = [ 'SpringGreen', 'SaddleBrown', 'Black', 'SlateBlue', 'DarkSlateGray',
                            'Indigo', 'DarkRed', 'DarkOrange', 'Goldenrod', 'MidnightBlue']

        #JANELA MAIN
        self.window_bd()

    def window_bd(self):

        self.windowMain = Tk()
        self.windowMain.resizable(False, False)
        self.windowMain.geometry(util().toCenterScreen(400, 100))
        self.windowMain.focus_force()
        self.windowMain.title('BACKUP')
        #self.windowMain.attributes('-fullscreen', True)  
        #self.fullScreenState = False

        list_bt = []

        def getDevices():
            
            for pos, device in enumerate(self.list_devices):
                path = f"{device}:/"

                #CRIAR BOTOES COM O PATH
                if os.path.isdir(path):
                    
                    list_bt.append(
                        Button(text=str(path), font='Arial 12 bold', bg=self.list_color[0], fg='black', width=8, height=2)
                    )
            
            #VERRE LISTA DE BOTOES PARA POSICIONAR E ATTR COMMAND
            for d in list_bt:
                path = f"{d['text']}"
                d['command'] = lambda: startBackup(path)
                d.pack(side=LEFT, padx=2)
        
        def startBackup(device):
            
            if messagebox.askquestion('','NÃO DESLIGUE OU FECHE O COMPUTADOR, DESEJA CONTINUAR?'):

                try:
                    #INCIAR BACKUP
                    self.createBackup(device)

                    #SUCESSO
                    messagebox.showinfo('',f'BACKUP FEITO - DATA:{self.data_atual}')

                except:
                    messagebox.showerror('','NÃO FOI POSSIVEL REALIZAR O BACKUP')

            #FECHAR A JANELA
            self.windowMain.destroy()

        lblDevice = Label(self.windowMain, text='ESCOLHA O DISPOSITIVO:', font='Arial 12 bold')
        lblDevice.pack()

        #BUSCAR DISPOSITIVOS
        getDevices()

        #VOLTAR
        imagem_voltar = PhotoImage(file=f"src/voltar_48.png")
        btVoltar = Button(self.windowMain, image=imagem_voltar, bg='White', command=lambda: self.windowMain.destroy())
        btVoltar.imagem = imagem_voltar
        btVoltar.pack(side=LEFT, padx=2)

        #self.windowMain.bind("<F11>", self.toggleFullScreen)
        #self.windowMain.bind("<Escape>", self.quitFullScreen)

        self.windowMain.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.windowMain.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.windowMain.attributes("-fullscreen", self.fullScreenState)
        self.windowMain.geometry('730x460')
        
    def createBackup(self, device):

        self.destino = f'{device}/{self.data_atual}-wmotos.db'

        #REALIZAR BACKUP PARA UNIDADE REMOVIVEL
        shutil.copy(self.origem, self.destino)

class util:

    def __init__(self) -> None:
        pass

    def toCenterScreen(self, width, height):
        pos_x = float(json_ws().getWidthScreen())/2 - width/2
        pos_y = float(json_ws().getHeightScreen())/2 - height/2
        
        if pos_x < 0:
            pos_x = pos_x * -1

        if pos_y < 0:
            pos_y = pos_y * -1

        return f'{width}x{height}+{pos_x:.0f}+{pos_y:.0f}'

Menu_Principal()