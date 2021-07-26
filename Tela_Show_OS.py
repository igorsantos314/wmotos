from tkinter import ttk 
from tkinter import *
from Persistencia import bd
from module_print import print_document
from tkinter import messagebox
from Tela_Editar_OS import Tela_Editar_OS
from util import util
from module_json import json_ws

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
        lblBuscar.place(x=10, y=100)

        etBuscar = Entry(self.windowMain, width=96, font='Arial 12')
        etBuscar.place(x=104, y=100)

        #STATUS
        lblStatus = Label(text='STATUS:', bg='White')
        lblStatus.place(x=10, y=10)

        #ESPERA
        imagem_espera = PhotoImage(file=f"src/espera_48.png")
        btEspera = Button(self.windowMain, image=imagem_espera, bg='White', bd=0, command=lambda: statusEspera())
        btEspera.imagem = imagem_espera
        btEspera.place(x=10, y=30)

        #EM ANDAMENTO
        imagem_andamento = PhotoImage(file=f"src/andamento_48.png")
        btAndamento = Button(self.windowMain, image=imagem_andamento, bg='White', bd=0, command=lambda: statusAndamento())
        btAndamento.imagem = imagem_andamento
        btAndamento.place(x=80, y=30)

        #CONCLUIDO
        imagem_concluido = PhotoImage(file=f"src/concluido_48.png")
        btConcluido = Button(self.windowMain, image=imagem_concluido, bg='White', bd=0, command=lambda: statusConcluido())
        btConcluido.imagem = imagem_concluido
        btConcluido.place(x=150, y=30)

        #FORMA DE PAGAMENTO
        lblPagamento = Label(text='FORMA DE PAGAMENTO:', bg='White')
        lblPagamento.place(x=220, y=10)
        
        #DINHEIRO
        imagem_dinheiro = PhotoImage(file=f"src/dinheiro_48.png")
        btDinheiro = Button(self.windowMain, image=imagem_dinheiro, bg='White', bd=0, command=lambda: pagamentoDinheiro())
        btDinheiro.imagem = imagem_dinheiro
        btDinheiro.place(x=220, y=30)

        #CARTÃO
        imagem_cartao = PhotoImage(file=f"src/cartao_48.png")
        btCartao = Button(self.windowMain, image=imagem_cartao, bg='White', bd=0, command=lambda: pagamentoCartao())
        btCartao.imagem = imagem_cartao
        btCartao.place(x=290, y=30)

        #PIX
        imagem_transferencia = PhotoImage(file=f"src/transferencia_48.png")
        btTransferencia = Button(self.windowMain, image=imagem_transferencia, bg='White', bd=0, command=lambda: pagamentoPix())
        btTransferencia.imagem = imagem_transferencia
        btTransferencia.place(x=360, y=30)

        #OUTRO
        imagem_transferencia = PhotoImage(file=f"src/outro_48.png")
        btTransferencia = Button(self.windowMain, image=imagem_transferencia, bg='White', bd=0, command=lambda: pagamentoOutro())
        btTransferencia.imagem = imagem_transferencia
        btTransferencia.place(x=430, y=30)

        #CLIENTE PAGOU
        lblTroco = Label(text='CLIENTE PAGOU:', bg='White', bd=0)
        lblTroco.place(x=500, y=10)

        #TROCO
        imagem_troco = PhotoImage(file=f"src/troco_48.png")
        btTroco = Button(self.windowMain, image=imagem_troco, bg='White', bd=0, command=lambda: troco())
        btTroco.imagem = imagem_troco
        btTroco.place(x=500, y=30)

        #TREEVIEW
        style = ttk.Style(self.windowMain)
        style.theme_use('vista')

        style.configure(
            "Treeview",
            background="White",
            fieldbackground='White'
        )

        style.map("Treeview", background=[('selected', 'DodgerBlue')], foreground=[('selected', 'White')])

        # Using treeview widget 
        treev2 = ttk.Treeview(self.windowMain, selectmode ='browse', height=15) 

        # Calling pack method w.r.to treeview 
        treev2.place(x=10, y=140)

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
        treev2.heading("8", text ="Pagamento")
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

        def getAll():
            #VARRER LISTA E ADICIONAR NA TABELA
            for i in bd().getAllOS():
                total = f"{(i[10] + i[11] + i[12]):.2f}"
                treev2.insert("", 'end', text ="L1", values =(i[0], i[1], i[2], i[3], i[5], i[8], i[9], i[10], i[11], i[12], total))

        def buscar(event):
            
            #LIMPA A TABELA
            limparTabela()

            #VARRER LISTA E ADICIONAR NA TABELA
            for i in bd().getNomeVeiculoOS(etBuscar.get().upper()):
                total = f"{(i[10] + i[11] + i[12]):.2f}"
                treev2.insert("", 'end', text ="L1", values =(i[0], i[1], i[2], i[3], i[5], i[8], i[9], i[10], i[11], i[12], total))

        def limpar(event):
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
                print_document('os', conteudo)
        
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

        def deletar(event):
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
                buscar(None)
        
        def statusEspera():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updateStatusEspera(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                buscar(None)

        def statusAndamento():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updateStatusAndamento(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                buscar(None)

        #--- FORMA DE PAGAMENTO ---
        def pagamentoDinheiro():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updatePagamentoDinheiro(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                buscar(None)

        def pagamentoCartao():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updatePagamentoCartao(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                buscar(None)

        def pagamentoPix():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updatePagamentoPix(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                buscar(None)

        def pagamentoOutro():
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                bd().updatePagamentoOutro(id)

                #LIMPA A TABELA
                limparTabela()

                #ATUALIZAR TABELA
                buscar(None)

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

        def popup(event):
            self.menuPopup.post(event.x_root, event.y_root)
        
        #MENU POPUP
        self.menuPopup = Menu(self.windowMain, tearoff=0)
        self.menuPopup.add_command(label="Editar", command=lambda: editar(None))
        self.menuPopup.add_command(label="Imprimir", command=lambda: imprimir(None))
        self.menuPopup.add_separator()
        
        self.menuPopup.add_command(label="Em Espera", command=lambda: statusEspera())
        self.menuPopup.add_command(label="Em Andamento", command=lambda: statusAndamento())
        self.menuPopup.add_command(label="Concluido", command=lambda: statusConcluido())
        self.menuPopup.add_separator()

        self.menuPopup.add_command(label="Pagamento em Dinheiro", command=lambda: pagamentoDinheiro())
        self.menuPopup.add_command(label="Pagamento em Cartão", command=lambda: pagamentoCartao())
        self.menuPopup.add_command(label="Pagamento com Pix", command=lambda: pagamentoPix())
        self.menuPopup.add_command(label="Outro", command=lambda: pagamentoOutro())
        self.menuPopup.add_separator()

        self.menuPopup.add_command(label="Excluir", command=lambda: deletar(None))

        if json_ws().getShowOsInit() == "True":
            #Povoar Tabela
            getAll()
        
        """ def key_press(event):
            key = event
            print(key, 'is pressed')

        self.windowMain.bind('<Key>', key_press)"""

        #CAPTURA DE BOTOES
        self.windowMain.bind('<Escape>', voltar)
        
        #MINUSCULO
        self.windowMain.bind('<Control-p>', imprimir)
        self.windowMain.bind('<Control-l>', limpar)

        #MAIUSCULO
        self.windowMain.bind('<Control-P>', imprimir)
        self.windowMain.bind('<Control-L>', limpar)
        
        #CAPTURA BOTAO NO TREVIEW
        treev2.bind("<Button-3>", popup)
        treev2.bind("<Double-Button-1>", editar)
        treev2.bind('<Return>', editar)
        treev2.bind('<Delete>', deletar)

        #CAPTURA DO CAMPO DE CONSULTA
        etBuscar.bind('<Return>', buscar)

        #MANUAL
        lblAjuda = Label(text='<Esc> Voltar    <Enter> Editar    <Del> Deletar    <Ctrl+p> Imprimir    <Ctrl+l> Limpar', bg='White')
        lblAjuda.place(x=10, y=475)
        
        self.windowMain.mainloop()

    def CalcularTroco(self, valor):

        self.windowTroco = Tk()
        self.windowTroco.title('IGTEC - TROCO')
        self.windowTroco['bg'] = 'White'
        self.windowTroco.resizable(False, False)
        self.windowTroco.geometry(util().toCenterScreen(400, 250))
        self.windowTroco.focus_force()

        #TOTAL DA OS
        lblTotal = Label(self.windowTroco, text='Total:', font='Arial 15', bg='White')
        lblTotal.place(x=10, y=30)
        
        etValor = Entry(self.windowTroco, font='Arial 15 bold')
        etValor.insert(0, f"{valor:.2f}".replace('.', ','))
        etValor['state'] = 'disabled'
        etValor.place(x=130, y=30)

        #DESCONTO
        lblDesc = Label(self.windowTroco, text='Desconto:', font='Arial 15', bg='White')
        lblDesc.place(x=10, y=80)

        etDesc = Entry(self.windowTroco, font='Arial 15 bold')
        etDesc.insert(0, "0,00")
        etDesc.place(x=130, y=80)

        #RECEBEU DO CLIENTE
        lblRecebeu = Label(self.windowTroco, text='Pagou:', font='Arial 15', bg='White')
        lblRecebeu.place(x=10, y=130)

        etRecebeu = Entry(self.windowTroco, font='Arial 15 bold')
        etRecebeu.place(x=130, y=130)
        
        #TROCO
        lblTroco = Label(self.windowTroco, text='Troco:', font='Arial 15', bg='White')
        lblTroco.place(x=10, y=180)

        etTroco = Entry(self.windowTroco, font='Arial 15 bold', state='disabled')
        etTroco.place(x=130, y=180)

        lblManual = Label(self.windowTroco, text='<Esc> Voltar    <Enter> Calcular Troco', bg='White')
        lblManual.place(x=10, y=230)

        def calc(event):

            try:
                desconto = float(etDesc.get().replace(',','.'))
                troco = float(etRecebeu.get().replace(',','.')) - (valor - desconto)

                #HABILITAR PARA EDIÇÃO
                etTroco['state'] = 'normal'

                #SETAR O VALOR DO TROCO
                etTroco.delete(0, END)
                etTroco.insert(0, f"{troco}".replace('.',','))

                #DESABILITAR
                etTroco['state'] = 'disabled'
            except:
                messagebox.showerror('','PREENCHA OS CAMPOS CORRETAMENTE!')

                #FOCAR NA JANELA
                self.windowTroco.focus_force()

                #FOCAR NO CAMPO
                etRecebeu.focus_force()

        def exit(event):
            self.windowTroco.destroy()
        
        #FOCAR NO QUE NO CAMPO DE PAGOU
        etRecebeu.focus_force()

        self.windowTroco.bind('<Return>', calc)
        self.windowTroco.bind('<Escape>', exit)

        self.windowTroco.mainloop()

#consulta()