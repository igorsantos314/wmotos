from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from Persistencia import bd
from util import util
from module_json import json_ws

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
