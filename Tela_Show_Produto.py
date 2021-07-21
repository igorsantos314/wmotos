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
        treev2 = ttk.Treeview(self.windowMain, selectmode ='browse', height=15) 

        # Calling pack method w.r.to treeview 
        treev2.place(x=10, y=50)

        # Constructing vertical scrollbar 
        # with treeview 
        verscrlbar = ttk.Scrollbar(self.windowMain, 
                                orient ="vertical",
                                command = treev2.yview) 

        # scrollbar 
        #verscrlbar.pack(side ='right', fill ='x') 

        # Configuring treeview 
        treev2.configure(xscrollcommand = verscrlbar.set) 

        # Defining number of columns 
        treev2["columns"] = ("1", "2", "4", "5", "6")

        # Defining heading 
        treev2['show'] = 'headings'

        # Assigning the width and anchor to the 
        # respective columns 
        treev2.column("1", width = 60, anchor ='c') 
        treev2.column("2", width = 250, anchor ='se')
        treev2.column("4", width = 100, anchor ='se')
        treev2.column("5", width = 100, anchor ='se') 
        treev2.column("6", width = 100, anchor ='se')

        # Assigning the heading names to the 
        # respective columns 
        treev2.heading("1", text ="Id") 
        treev2.heading("2", text ="Nome do Produto") 
        treev2.heading("4", text ="Valor de Compra")
        treev2.heading("5", text ="Valor de Venda")
        treev2.heading("6", text ="Lucro UND.")
        
        def getAll():
            #VARRER LISTA E ADICIONAR NA TABELA
            for i in bd().getAllProduto():
                lucro = f"{(i[3] - i[2]):.2f}"
                treev2.insert("", 'end', text ="L1", values =(i[0], i[1], i[2], i[3], lucro))
        
        #POVOAR TABELA
        getAll()

        #MANUAL
        lblAjuda = Label(text='<Esc> Voltar   <Enter> Editar', bg='White')
        lblAjuda.place(x=10, y=390)

        self.windowMain.mainloop()

#Tela_Show_Produtos()