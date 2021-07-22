from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from Persistencia import bd
from util import util
from module_json import json_ws
from Tela_Plot_Graficos import plotGraphs
import hashlib

class Contabilidade:

    def __init__(self):
        # DATA ATUAL
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year
        self.data_atual = f'{self.day}/{self.month}/{self.year}'

        self.id = id
        
        #self.window()
        self.login()

    def login(self):

        windowLogin = Tk()
        windowLogin.resizable(False, False)
        windowLogin.geometry(util().toCenterScreen(160,70))
        windowLogin.focus_force()
        windowLogin.title('IGTEC')
        
        lblSenha = Label(windowLogin, text='Senha:')
        lblSenha.pack()

        etSenha = Entry(windowLogin, font='Arial 12 bold', show='*')
        etSenha.pack()

        def verify(event):
            hash =  hashlib.md5(etSenha.get().encode())
            senha = hash.hexdigest()

            if senha == json_ws().getPwCont():
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
        self.windowMain['bg'] = 'White'
        self.windowMain.focus_force()
        self.windowMain.title('IGTEC - CONTABILIDADE')

        #Data
        lblData = Label(self.windowMain, text='Dia:', bg='White')
        lblData.place(x=10, y=20)

        comboData = ttk.Combobox(self.windowMain, width = 8) 

        comboData['values'] = tuple(['{}'.format(i) for i in range(1, 32)])
        comboData.current(self.day-1)
        comboData.place(x=10, y=40)

        #Mes
        lblMes = Label(self.windowMain, text='Mês:', bg='White')
        lblMes.place(x=130, y=20)

        comboMes = ttk.Combobox(self.windowMain, width = 8) 

        comboMes['values'] = tuple(['{}'.format(i) for i in range(1, 13)])
        comboMes.current(self.month-1)
        comboMes.place(x=130, y=40)

        #Ano
        lblAno = Label(self.windowMain, text='Ano:', bg='White')
        lblAno.place(x=250, y=20)

        comboAno = ttk.Combobox(self.windowMain, width = 8) 

        comboAno['values'] = tuple(['{}'.format(i) for i in range(2021, 2051)])
        comboAno.current(self.year - 2021)
        comboAno.place(x=250, y=40)

        #CONTANIER
        lblContDia = Label(self.windowMain, text='RECEITA DIA', font='Arial 15', width=20, height=2, borderwidth = 1, relief="ridge", bg='#fee440')
        lblContDia.place(x=10, y=80)

        contValorDia = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, borderwidth = 1, relief="ridge", bg='White')
        contValorDia.place(x=10, y=129)

        lblContMes = Label(self.windowMain, text='RECEITA MÊS', font='Arial 15', width=20, height=2, borderwidth = 1, relief="ridge", bg='#00bbf9')
        lblContMes.place(x=250, y=80)

        contValorMes = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, borderwidth = 1, relief="ridge", bg='White')
        contValorMes.place(x=250, y=129)

        lblContTotal = Label(self.windowMain, text='RECEITA TOTAL', font='Arial 15', width=20, height=2, borderwidth = 1, relief="ridge", bg='#00f5d4')
        lblContTotal.place(x=490, y=80)

        contValorTotal = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, borderwidth = 1, relief="ridge", bg='White')
        contValorTotal.place(x=490, y=129)

        #FORMA DE PAGAMENTO
        lblReceitaProduto = Label(self.windowMain, text='RECEITA PRODUTOS', font='Arial 15', width=20, height=2, borderwidth = 1, relief="ridge", bg='#ee6055')
        lblReceitaProduto.place(x=10, y=232)

        contReceitaProduto = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, borderwidth = 1, relief="ridge", bg='White')
        contReceitaProduto.place(x=10, y=281)

        lblLucro = Label(self.windowMain, text='LUCRO PRODUTOS', font='Arial 15', width=20, borderwidth = 1, relief="ridge", height=2, bg='#60d394')
        lblLucro.place(x=250, y=232)

        contLucro = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, bg='White', borderwidth = 1, relief="ridge")
        contLucro.place(x=250, y=281)

        #RESERVA DE EMERGÊNCIA
        lblReservaMes = Label(self.windowMain, text='RESERVA DO MÊS', font='Arial 15', width=20, height=2, borderwidth = 1, relief="ridge", bg='#836FFF', fg='White')
        lblReservaMes.place(x=10, y=384)

        contReservaMes = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, bg='White', borderwidth = 1, relief="ridge")
        contReservaMes.place(x=10, y=433)

        lblReservaTotal = Label(self.windowMain, text='RESERVA TOTAL', font='Arial 15', width=20, height=2, borderwidth = 1, relief="ridge", bg='#00CED1', fg='White')
        lblReservaTotal.place(x=250, y=384)

        contReservaTotal = Label(self.windowMain, text='', font='Arial 15', width=20, height=2, bg='White' , borderwidth = 1, relief="ridge")
        contReservaTotal.place(x=250, y=433)

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

        def setValuesProdutos():
            #DINHEIRO
            contReceitaProduto['text'] = f'R$ {bd().getReceitaProd():.2f}'.replace('.', ',')

            #CARTAO
            contLucro['text'] = f'R$ {bd().getLucroProd():.2f}'.replace('.', ',')

        def setGraph():
            
            #ANO CORRENTE
            ano = comboAno.get()

            #PEGAR RECEITA DE MAO DE OBRA, PECAS E OUTROS E PLOTAR GRAFICO
            plotGraphs().generateGraphYear(
                ano,
                bd().getReceitaMaoObra(ano),
                bd().getReceitaPecas(ano),
                bd().getReceitaOutros(ano)
            )

        #EDITAR
        imagem_buscar = PhotoImage(file=f"src/buscar_48.png")
        btBuscar = Button(self.windowMain, image=imagem_buscar, bg='White', bd=0, command=lambda: setValeusData())
        btBuscar.imagem = imagem_buscar
        btBuscar.place(x=350, y=10)
        
        #GRAFICO
        imagem_grafico = PhotoImage(file=f"src/grafico_48.png")
        btGrafico = Button(self.windowMain, image=imagem_grafico, bg='White', bd=0, command=lambda: setGraph())
        btGrafico.imagem = imagem_grafico
        btGrafico.place(x=420, y=10)

        #VOLTAR
        imagem_voltar = PhotoImage(file=f"src/voltar_48.png")
        btVoltar = Button(self.windowMain, image=imagem_voltar, bg='White', bd=0, command=lambda: exit(None))
        btVoltar.imagem = imagem_voltar
        btVoltar.place(x=490, y=10)

        def exit(event):
            self.windowMain.destroy()

        #SETAR VALORES
        setValeusData()
        setValuesProdutos()
        
        #CAPTURAR TELCAS
        self.windowMain.bind('<Escape>', exit)
        
        self.windowMain.mainloop()

#Contabilidade()