from Persistencia import bd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from util import util

class Tela_Vender_Produtos:

    def __init__(self) -> None:
        #VARIAVEIS GLOBAIS
        self.subtotal = 0
        self.quant = 0
        self.total = 0

        self.window()

    def window(self):
        
        self.windowMain = Tk()
        self.windowMain.resizable(False, False)
        self.windowMain.geometry(util().toCenterScreen(940, 550))
        self.windowMain.focus_force()
        self.windowMain.title('IGTEC - VENDER PRODUTOS')
        self.windowMain['bg'] = 'White'
        
        #NOVO PRODUTO
        imagem_novo_produto = PhotoImage(file=f"src/novo_produto_48.png")
        btNovo_produto = Button(self.windowMain, image=imagem_novo_produto, bg='White', bd=0, command=lambda: '')
        btNovo_produto.imagem = imagem_novo_produto
        btNovo_produto.place(x=10, y=10)

        #EXIBIR PRODUTOS
        imagem_produtos = PhotoImage(file=f"src/produtos_48.png")
        btProdutos = Button(self.windowMain, image=imagem_produtos, bg='White', bd=0, command=lambda: '')
        btProdutos.imagem = imagem_produtos
        btProdutos.place(x=80, y=10)

        #TREEVIEW BUSCAR PRODUTO
        lblNomeProduto = Label(self.windowMain, text='BUSCAR:', font='Arial 12', bg='White')
        lblNomeProduto.place(x=10, y=90)
        
        etNomeProduto = Entry(self.windowMain, font='Arial 12', width=35)
        etNomeProduto.place(x=105, y=90)

        style = ttk.Style(self.windowMain)
        style.theme_use('vista')

        style.configure(
            "Treeview",
            background="White",
            fieldbackground='White'
        )

        style.map("Treeview", background=[('selected', 'DarkTurquoise')], foreground=[('selected', 'Black')])

        # Using treeview widget 
        treevProduto = ttk.Treeview(self.windowMain, selectmode ='browse', height=15) 

        # Calling pack method w.r.to treeview 
        treevProduto.place(x=10, y=120)

        # Constructing vertical scrollbar 
        # with treeview 
        verscrlbar = ttk.Scrollbar(self.windowMain, 
                                orient ="vertical",
                                command = treevProduto.yview) 

        # scrollbar 
        verscrlbar.pack(side ='right', fill ='x') 

        # Configuring treeview 
        treevProduto.configure(xscrollcommand = verscrlbar.set) 

        # Defining number of columns 
        treevProduto["columns"] = ("1", "2", "3")

        # Defining heading 
        treevProduto['show'] = 'headings'

        # Assigning the width and anchor to the 
        # respective columns 
        treevProduto.column("1", width = 60, anchor ='c') 
        treevProduto.column("2", width = 250, anchor ='se')
        treevProduto.column("3", width = 100, anchor ='se')

        # Assigning the heading names to the 
        # respective columns 
        treevProduto.heading("1", text ="Id") 
        treevProduto.heading("2", text ="Nome do Produto") 
        treevProduto.heading("3", text ="Valor")

        #TREEVIEW DE VENDA DE PRODUTOS
        lblVenda = Label(self.windowMain, text='CARRINHO:', font='Arial 18 bold', bg='White')
        lblVenda.place(x=440, y=5)

        treevVenda = ttk.Treeview(self.windowMain, selectmode ='browse', height=19) 

        # Calling pack method w.r.to treeview 
        treevVenda.place(x=440, y=40)

        # Constructing vertical scrollbar 
        # with treeview 
        verscrlbarVenda = ttk.Scrollbar(self.windowMain, 
                                orient ="vertical",
                                command = treevVenda.yview) 

        # scrollbar 
        verscrlbarVenda.pack(side ='right', fill ='x') 

        # Configuring treeview 
        treevVenda.configure(xscrollcommand = verscrlbarVenda.set) 

        # Defining number of columns 
        treevVenda["columns"] = ("1", "2", "3", "4")

        # Defining heading 
        treevVenda['show'] = 'headings'

        # Assigning the width and anchor to the 
        # respective columns 
        treevVenda.column("1", width = 250, anchor ='c') 
        treevVenda.column("2", width = 60, anchor ='se')
        treevVenda.column("3", width = 60, anchor ='se')
        treevVenda.column("4", width = 70, anchor ='se')

        # Assigning the heading names to the 
        # respective columns 
        treevVenda.heading("1", text ="Nome do Produto") 
        treevVenda.heading("2", text ="Subtotal")
        treevVenda.heading("3", text ="Quant.")
        treevVenda.heading("4", text ="Total")

        # -- VALORES --
        lblSubTotal = Label(text='SUBTOTAL: ', font='Arial 20', bg='White', fg='Blue')
        lblSubTotal.place(x=10, y=470)

        lblQuant = Label(text='QUANT: ', font='Arial 20', bg='White', fg='Red')
        lblQuant.place(x=440, y=470)

        lblTotal = Label(text='TOTAL: ', font='Arial 20 bold', bg='White', fg='Green')
        lblTotal.place(x=650, y=470)

        def refreshValores():
            #SETAR VALORES
            lblSubTotal['text'] = f'SUBTOTAL:  R$ {self.subtotal:.2f}'
            lblQuant['text'] = f'QUANT: {self.quant}'
            lblTotal['text'] = f'TOTAL: R$ {self.total:.2f}'

        def buscar(event):
            #LIMPAR TABELA
            treevProduto.delete(*treevProduto.get_children())

            #INSERIR NO TREEVIEW DE PRODUTO
            for produto in bd().getNomeProduto(etNomeProduto.get().upper()):
                treevProduto.insert("", 'end', text ="L1", values=(produto[0], produto[1], produto[3]))

        def addCarrinho(event):
            
            quant = self.etQuant.get()

            if quant != '':
                
                #LINHA SELECIONADA
                produtoSelecionado = treevProduto.selection()[0]

                #PEGA O NOME
                nome = treevProduto.item(produtoSelecionado, "values")[1]

                #PEGA O VALOR
                valor = float(treevProduto.item(produtoSelecionado, "values")[2])
                
                #CALULAR O VALOR TOTAL
                total = int(quant) * valor

                #INSERIR NO CARRINHO
                treevVenda.insert("", 'end', text ="L1", values=(nome, valor, quant, total))

                #ATUALIZAR VALORES
                self.total += total
                self.subtotal += valor
                self.quant += int(quant)

                refreshValores()

                #FECHAR CAMPO DE QUANTIDADE
                fecharQuantidade(None)

        def removerCarrinho(event):

            if len(treevVenda.selection()) == 0:
                messagebox.showwarning('','POR FAVOR SELECIONE UM ITEM DO CARRINHO')

            else:
                #LINHA SELECIONADA
                produtoSelecionado = treevVenda.selection()[0]

                subtotal = float(treevVenda.item(produtoSelecionado, "values")[1])
                quantidade = int(treevVenda.item(produtoSelecionado, "values")[2])
                
                total = subtotal * quantidade

                #ATUALIZAR VALORES
                self.total -= total
                self.subtotal -= subtotal
                self.quant -= quantidade

                refreshValores()

                #REMOVER DA LISTA
                treevVenda.delete(produtoSelecionado)

        def fecharQuantidade(event):

            #DESTRUIR TELA DE QUANT
            self.lblFundo.destroy()
            self.lblQuant.destroy()
            self.etQuant.destroy()

            #HABILITAR TREEVIEW PRODUTO

        def setQuantidade(event):
            
            if len(treevProduto.selection()) == 0:
                messagebox.showwarning('','POR FAVOR SELECIONE UM PRODUTO')
                
            else:
                #DESABILITAR TREEVIEW PRODUTO

                self.lblFundo = Label(self.windowMain, bg='DarkTurquoise', width=20, height=5)
                self.lblFundo.pack(pady=200)
                
                self.lblQuant = Label(self.windowMain, text='Quantidade:', font='Arial 12', bg='DarkTurquoise', fg='White')
                self.lblQuant.place(x=405, y=210)

                self.etQuant = Entry(self.windowMain, font='Arial 12', width=10)
                self.etQuant.insert(0, '1')
                self.etQuant.place(x=405, y=240)
                    
                self.etQuant.focus_force()

                self.etQuant.bind('<Return>', addCarrinho)
                self.etQuant.bind('<Escape>', fecharQuantidade)

        #INICIALIZAR VALORES
        refreshValores()

        #FOCAR NO CAMPO DE BUSCAR POR NOME
        etNomeProduto.focus_force()

        #CAPTURA DE TECLAS
        treevProduto.bind('<Return>', setQuantidade)
        treevVenda.bind('<Delete>', removerCarrinho)

        etNomeProduto.bind('<Return>', buscar)

        self.windowMain.mainloop()

Tela_Vender_Produtos()