from Persistencia import bd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from util import util

class Tela_Vender_Produtos:

    def __init__(self) -> None:
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

        style.map("Treeview", background=[('selected', '#00DB73')], foreground=[('selected', 'Black')])

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
        treevVenda.column("1", width = 70, anchor ='c') 
        treevVenda.column("2", width = 250, anchor ='se')
        treevVenda.column("3", width = 60, anchor ='se')
        treevVenda.column("4", width = 70, anchor ='se')

        # Assigning the heading names to the 
        # respective columns 
        treevVenda.heading("1", text ="Venda Id") 
        treevVenda.heading("2", text ="Nome do Produto")
        treevVenda.heading("3", text ="Quant.")
        treevVenda.heading("4", text ="Valor Total")

        def addCarrinho(event):
            
            quant = self.etQuant.get()

            if quant != '':
                fecharQuantidade(None)
                print(quant)

        def fecharQuantidade(event):

            #DESTRUIR TELA DE QUANT
            self.lblFundo.destroy()
            self.lblQuant.destroy()
            self.etQuant.destroy()

            #HABILITAR TREEVIEW PRODUTO
            treevVenda.state(('!disabled',))

        def setQuantidade(event):

            #DESABILITAR TREEVIEW PRODUTO
            treevVenda.state(('disabled',))

            self.lblFundo = Label(self.windowMain, bg='LemonChiffon', width=20, height=5)
            self.lblFundo.pack(pady=200)
            
            self.lblQuant = Label(self.windowMain, text='Quantidade:', font='Arial 12', bg='LemonChiffon')
            self.lblQuant.place(x=405, y=210)

            self.etQuant = Entry(self.windowMain, font='Arial 12', width=10)
            self.etQuant.insert(0, '1')
            self.etQuant.place(x=405, y=240)
                
            self.etQuant.focus_force()

            self.etQuant.bind('<Return>', addCarrinho)
            self.etQuant.bind('<Escape>', fecharQuantidade)

        #CAPTURA DE TECLAS
        treevProduto.bind('<Return>', setQuantidade)

        self.windowMain.mainloop()

Tela_Vender_Produtos()