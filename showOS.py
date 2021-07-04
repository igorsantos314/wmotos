from tkinter import ttk 
from tkinter import *
from Persistencia import bd
from module_print import print_document
from tkinter import messagebox
from Tela_Editar_OS import Tela_Editar_OS

class consulta:

    def __init__(self) -> None:
        self.window()

    def window(self):
        # Creating tkinter self.windowMain 
        self.windowMain = Tk()
        self.windowMain.resizable(False, False)
        self.windowMain.attributes('-fullscreen', True)  
        self.fullScreenState = False
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
        
        #TREEVIEW
        style = ttk.Style(self.windowMain)
        style.theme_use('clam')

        style.configure(    "Treeview",
                            background="Silver",
                            fieldbackground='Silver'
                            )

        style.map("Treeview", background=[('selected', 'Red')], foreground=[('selected', 'White')])

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
        treev2["columns"] = ("1", "2", "3", "4", "5", "8", "9", "10", "11") 

        # Defining heading 
        treev2['show'] = 'headings'

        # Assigning the width and anchor to the 
        # respective columns 
        treev2.column("1", width = 60, anchor ='c') 
        treev2.column("2", width = 90, anchor ='se') 
        treev2.column("3", width = 90, anchor ='se') 
        treev2.column("4", width = 120, anchor ='se')
        treev2.column("5", width = 90, anchor ='se') 
        #treev2.column("6", width = 150, anchor ='se')
        #treev2.column("7", width = 150, anchor ='se') 
        treev2.column("8", width = 150, anchor ='se')
        treev2.column("9", width = 120, anchor ='se') 
        treev2.column("10", width = 120, anchor ='se')
        treev2.column("11", width = 120, anchor ='se')

        # Assigning the heading names to the 
        # respective columns 
        treev2.heading("1", text ="Id") 
        treev2.heading("2", text ="Data Entrada") 
        treev2.heading("3", text ="Data Saida")
        treev2.heading("4", text ="Cliente")
        treev2.heading("5", text ="Veiculo")
        #treev2.heading("6", text ="Descrição")
        #treev2.heading("7", text ="Laudo Tecnico")
        treev2.heading("8", text ="Forma de Pagamento")
        treev2.heading("9", text ="Status")
        treev2.heading("10", text ="Valor Mão de Obra")
        treev2.heading("11", text ="Valor de Peças")

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
                treev2.insert("", 'end', text ="L1", values =(i[0], i[1], i[2], i[3], i[5], i[8], i[9], i[10], i[11]))

        def buscar():
            
            #LIMPA A TABELA
            limparTabela()

            #VARRER LISTA E ADICIONAR NA TABELA
            for i in bd().getNomeVeiculoOS(etBuscar.get().upper()):
                treev2.insert("", 'end', text ="L1", values =(i[0], i[1], i[2], i[3], i[5], i[8], i[9], i[10], i[11]))

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

        def statusConcluido():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updateStatusConcluido(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                getAll()
        
        def statusEspera():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updateStatusEspera(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                getAll()

        def statusAndamento():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updateStatusAndamento(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                getAll()

        def limparTabela():
            treev2.delete(*treev2.get_children())

        #Povoar Tabela
        getAll()

        # Calling mainloop 
        self.windowMain.bind("<F11>", self.toggleFullScreen)
        self.windowMain.bind("<Escape>", self.quitFullScreen)

        self.windowMain.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.windowMain.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.windowMain.attributes("-fullscreen", self.fullScreenState)
        self.windowMain.geometry('993x480')

consulta()