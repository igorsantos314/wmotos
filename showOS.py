from tkinter import ttk 
from tkinter import *
from Persistencia import bd
from module_print import print_document
from tkinter import messagebox
from Tela_Editar_OS import Tela_Editar_OS
from util import util

class consulta:

    def __init__(self) -> None:
        self.window()
        
    def window(self):
        # Creating tkinter self.windowMain 
        self.windowMain = Tk()
        self.windowMain.resizable(False, False)
        self.windowMain.geometry(util().toCenterScreen(993, 500))
        self.windowMain.focus_force()
        self.windowMain.title('IGTEC - CONSULTAR OS')
        self.windowMain['bg'] = 'White'

        #BUSCAR
        lblBuscar = Label(self.windowMain, text='BUSCAR:', font='Arial 13', bg='White')
        lblBuscar.place(x=440, y=10)

        etBuscar = Entry(self.windowMain, width=59, font='Arial 12')
        etBuscar.place(x=440, y=40)

        #EDITAR
        imagem_editar = PhotoImage(file=f"src/editar_48.png")
        btEditar = Button(self.windowMain, image=imagem_editar, bg='White', bd=0, command=lambda: editar(None))
        btEditar.imagem = imagem_editar
        btEditar.place(x=10, y=10)

        #DELETAR
        imagem_del = PhotoImage(file=f"src/deletar_48.png")
        btDel = Button(self.windowMain, image=imagem_del, bg='White', bd=0, command=lambda: deletar())
        btDel.imagem = imagem_del
        btDel.place(x=80, y=10)

        #IMPRIMIR
        imagem_imprimir = PhotoImage(file=f"src/impressora_48.png")
        btImprimir = Button(self.windowMain, image=imagem_imprimir, bg='White', bd=0, command=lambda: imprimir(None))
        btImprimir.imagem = imagem_imprimir
        btImprimir.place(x=150, y=10)

        #BUSCAR
        imagem_buscar = PhotoImage(file=f"src/buscar_48.png")
        btBuscar = Button(self.windowMain, image=imagem_buscar, bg='White', bd=0, command=lambda: buscar())
        btBuscar.imagem = imagem_buscar
        btBuscar.place(x=220, y=10)

        #LIMPAR
        imagem_limpar = PhotoImage(file=f"src/limpar_48.png")
        btLimpar = Button(self.windowMain, image=imagem_limpar, bg='White', bd=0, command=lambda: limpar())
        btLimpar.imagem = imagem_limpar
        btLimpar.place(x=290, y=10)

        #SAIR
        imagem_sair = PhotoImage(file=f"src/voltar_48.png")
        btSair = Button(self.windowMain, image=imagem_sair, bg='White', bd=0, command=lambda: voltar(None))
        btSair.imagem = imagem_sair
        btSair.place(x=360, y=10)

        #STATUS
        lblStatus = Label(text='STATUS:', bg='White')
        lblStatus.place(x=10, y=70)

        #ESPERA
        imagem_espera = PhotoImage(file=f"src/espera_48.png")
        btEspera = Button(self.windowMain, image=imagem_espera, bg='White', bd=0, command=lambda: statusEspera())
        btEspera.imagem = imagem_espera
        btEspera.place(x=10, y=90)

        #EM ANDAMENTO
        imagem_andamento = PhotoImage(file=f"src/andamento_48.png")
        btAndamento = Button(self.windowMain, image=imagem_andamento, bg='White', bd=0, command=lambda: statusAndamento())
        btAndamento.imagem = imagem_andamento
        btAndamento.place(x=80, y=90)

        #CONCLUIDO
        imagem_concluido = PhotoImage(file=f"src/concluido_48.png")
        btConcluido = Button(self.windowMain, image=imagem_concluido, bg='White', bd=0, command=lambda: statusConcluido())
        btConcluido.imagem = imagem_concluido
        btConcluido.place(x=150, y=90)

        #FORMA DE PAGAMENTO
        lblPagamento = Label(text='FORMA DE PAGAMENTO:', bg='White')
        lblPagamento.place(x=220, y=70)
        
        #DINHEIRO
        imagem_dinheiro = PhotoImage(file=f"src/dinheiro_48.png")
        btDinheiro = Button(self.windowMain, image=imagem_dinheiro, bg='White', bd=0, command=lambda: pagamentoDinheiro())
        btDinheiro.imagem = imagem_dinheiro
        btDinheiro.place(x=220, y=90)

        #CARTÃO
        imagem_cartao = PhotoImage(file=f"src/cartao_48.png")
        btCartao = Button(self.windowMain, image=imagem_cartao, bg='White', bd=0, command=lambda: pagamentoCartao())
        btCartao.imagem = imagem_cartao
        btCartao.place(x=290, y=90)

        #PIX
        imagem_transferencia = PhotoImage(file=f"src/transferencia_48.png")
        btTransferencia = Button(self.windowMain, image=imagem_transferencia, bg='White', bd=0, command=lambda: pagamentoPix())
        btTransferencia.imagem = imagem_transferencia
        btTransferencia.place(x=360, y=90)

        #OUTRO
        imagem_transferencia = PhotoImage(file=f"src/outro_48.png")
        btTransferencia = Button(self.windowMain, image=imagem_transferencia, bg='White', bd=0, command=lambda: pagamentoOutro())
        btTransferencia.imagem = imagem_transferencia
        btTransferencia.place(x=430, y=90)

        #FORMA DE PAGAMENTO
        lblTroco = Label(text='CLIENTE PAGOU:', bg='White', bd=0)
        lblTroco.place(x=500, y=70)

        #TROCO
        imagem_troco = PhotoImage(file=f"src/troco_48.png")
        btTroco = Button(self.windowMain, image=imagem_troco, bg='White', bd=0, command=lambda: troco())
        btTroco.imagem = imagem_troco
        btTroco.place(x=500, y=90)

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

        def voltar(event):
            #FECHAR JANELA PELO BOTÃO OU PELO ESC
            self.windowMain.destroy()

        def imprimir(event):
            
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                #PEGAR A TUPLA
                conteudo = bd().getOS(id)[0]

                #IMPRIMIR
                print_document(conteudo)
        
        def editar(event):
            
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

        def troco():
            if len(treev2.selection()) == 0:
                messagebox.showwarning('','POR FAVOR SELECIONE UMA OS')

            else:
                itemSelecionado = treev2.selection()[0]

                #PEGAR VALORES
                val = float(treev2.item(itemSelecionado, "values")[10])
                
                #CHAMAR JANELA DE TROCO
                self.CalcularTroco(val)

        def limparTabela():
            treev2.delete(*treev2.get_children())

        #Povoar Tabela
        getAll()

        self.windowMain.bind('<Return>', editar)
        self.windowMain.bind('<Escape>', voltar)
        
        #MINUSCULO
        self.windowMain.bind('<Control-p>', imprimir)

        #MAIUSCULO
        self.windowMain.bind('<Control-P>', imprimir)
        
        #MANUAL
        lblAjuda = Label(text='<Esc> Voltar    <Enter> Editar    <Ctrl+p> Imprimir')
        lblAjuda.place(x=10, y=480)
        
        self.windowMain.mainloop()

    def CalcularTroco(self, valor):

        self.windowTroco = Tk()
        self.windowTroco.title('IGTEC - TROCO')
        self.windowTroco.resizable(False, False)
        self.windowTroco.geometry(util().toCenterScreen(400, 250))
        self.windowTroco.focus_force()

        #TOTAL DA OS
        lblTotal = Label(self.windowTroco, text='Total:', font='Arial 15')
        lblTotal.place(x=10, y=30)
        
        etValor = Entry(self.windowTroco, font='Arial 15 bold')
        etValor.insert(0, f"{valor:.2f}".replace('.', ','))
        etValor['state'] = 'disabled'
        etValor.place(x=130, y=30)

        #DESCONTO
        lblDesc = Label(self.windowTroco, text='Desconto:', font='Arial 15')
        lblDesc.place(x=10, y=80)

        etDesc = Entry(self.windowTroco, font='Arial 15 bold')
        etDesc.insert(0, "0,00")
        etDesc.place(x=130, y=80)

        #RECEBEU DO CLIENTE
        lblRecebeu = Label(self.windowTroco, text='Pagou:', font='Arial 15')
        lblRecebeu.place(x=10, y=130)

        etRecebeu = Entry(self.windowTroco, font='Arial 15 bold')
        etRecebeu.place(x=130, y=130)
        
        #TROCO
        lblTroco = Label(self.windowTroco, text='Troco:', font='Arial 15')
        lblTroco.place(x=10, y=180)

        etTroco = Entry(self.windowTroco, font='Arial 15 bold', state='disabled')
        etTroco.place(x=130, y=180)

        etManual = Label(self.windowTroco, text='<Esc> - Voltar    <Enter> - Calcular Troco')
        etManual.place(x=10, y=230)

        def calc(event):

            if etDesc.get() != '' or etRecebeu.get() != '':
                desconto = float(etDesc.get().replace(',','.'))
                troco = float(etRecebeu.get().replace(',','.')) - (valor - desconto)

                #HABILITAR PARA EDIÇÃO
                etTroco['state'] = 'normal'

                #SETAR O VALOR DO TROCO
                etTroco.delete(0, END)
                etTroco.insert(0, f"{troco}".replace('.',','))

                #DESABILITAR
                etTroco['state'] = 'disabled'
            else:
                messagebox.showerror('','PREENCHA TODOS OS CAMPOS PARA CALCULAR !')

        def sair(event):
            self.windowTroco.destroy()

        #FOCAR NO QUE NO CAMPO DE PAGOU
        etRecebeu.focus_force()

        self.windowTroco.bind('<Return>', calc)
        self.windowTroco.bind('<Escape>', sair)

        self.windowTroco.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.windowMain.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.windowMain.attributes("-fullscreen", self.fullScreenState)
        self.windowMain.geometry('993x480')

#consulta()