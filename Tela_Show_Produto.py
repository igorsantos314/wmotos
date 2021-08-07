from Tela_Editar_Produto import Tela_Editar_Produto
from Persistencia import bd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from util import util

class Tela_Show_Produto:

    def __init__(self) -> None:
        self.window()

    def window(self):

        self.windowMain = Tk()
        self.windowMain.resizable(False, False)
        self.windowMain.geometry(util().toCenterScreen(640, 410))
        self.windowMain.focus_force()
        self.windowMain.title('IGTEC - EXIBIR PRODUTOS')
        self.windowMain['bg'] = 'White'

        # Data
        lblNomeProduto = Label(self.windowMain, text='BUSCAR:', font='Arial 12', bg='White')
        lblNomeProduto.place(x=10, y=10)
        
        etNomeProduto = Entry(self.windowMain, font='Arial 12', width=42)
        etNomeProduto.place(x=100, y=10)

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
        treevProduto = ttk.Treeview(self.windowMain, selectmode ='browse', height=15) 

        # Calling pack method w.r.to treeview 
        treevProduto.place(x=10, y=50)

        # Constructing vertical scrollbar 
        # with treeview 
        verscrlbar = ttk.Scrollbar(self.windowMain, 
                                orient ="vertical",
                                command = treevProduto.yview) 

        # scrollbar 
        #verscrlbar.pack(side ='right', fill ='x') 

        # Configuring treeview 
        treevProduto.configure(xscrollcommand = verscrlbar.set) 

        # Defining number of columns 
        treevProduto["columns"] = ("1", "2", "4", "5", "6")

        # Defining heading 
        treevProduto['show'] = 'headings'

        # Assigning the width and anchor to the 
        # respective columns 
        treevProduto.column("1", width = 60, anchor ='c') 
        treevProduto.column("2", width = 250, anchor ='se')
        treevProduto.column("4", width = 100, anchor ='se')
        treevProduto.column("5", width = 100, anchor ='se') 
        treevProduto.column("6", width = 100, anchor ='se')

        # Assigning the heading names to the 
        # respective columns 
        treevProduto.heading("1", text ="Id") 
        treevProduto.heading("2", text ="Nome do Produto") 
        treevProduto.heading("4", text ="Valor de Compra")
        treevProduto.heading("5", text ="Valor de Venda")
        treevProduto.heading("6", text ="Lucro UND.")
        
        def getId():
            if len(treevProduto.selection()) == 0:
                messagebox.showwarning('','POR FAVOR SELECIONE UMA OS')
                return False
            else:
                itemSelecionado = treevProduto.selection()[0]

                #PEGAR VALORES
                id = int(treevProduto.item(itemSelecionado, "values")[0])
                
                return id

        def editar(event):
            
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:
                print(id)
                #FECHHA A JANELA
                self.windowMain.destroy()

                #ABRE JANELA DE EDITAR
                Tela_Editar_Produto(id)

                #REABRE A TELA DE EXIBIR
                Tela_Show_Produto()

        def buscar(event):
            #LIMPAR TABELA
            treevProduto.delete(*treevProduto.get_children())

            #INSERIR NO TREEVIEW DE PRODUTO
            for produto in bd().getNomeProduto(etNomeProduto.get().upper()):
                valor_compra = f'{produto[2]:.2f}'.replace('.', ',')
                valor_venda = f'{produto[3]:.2f}'.replace('.', ',')

                lucro = f'{(produto[3] - produto[2]):.2f}'.replace('.', ',')
                
                treevProduto.insert("", 'end', text ="L1", values=(produto[0], produto[1], valor_compra, valor_venda, lucro))

        def excluir(event):
            id = getId()

            #VERIFICA SE O ID É VALIDO
            if id != False:

                if messagebox.askyesno('', 'EXCLUIR PRODUTO?'):
                    #DELETAR O PRODUTO
                    bd().delProduto(id)

                    #ATUALIZA A TABELA
                    buscar(None)

        def sair(event):
            self.windowMain.destroy()

        #MANUAL
        lblAjuda = Label(text='<Esc> Voltar   <Enter> Editar    <Del> Excluir', bg='White')
        lblAjuda.place(x=10, y=385)

        #FOCA NO CAMPO DE CONSULTA
        etNomeProduto.focus_force()

        #TECLAS DE ATALHO
        treevProduto.bind("<Double-Button-1>", editar)
        treevProduto.bind('<Return>', editar)
        treevProduto.bind('<Delete>', excluir)

        etNomeProduto.bind('<Return>', buscar)

        self.windowMain.bind('<Escape>', sair)

        self.windowMain.mainloop()

#Tela_Show_Produto()