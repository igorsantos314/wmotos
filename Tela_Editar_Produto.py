from Persistencia import bd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from util import util

class Tela_Editar_Produto:

    def __init__(self, id):
        self.id = id
        self.window()

    def window(self):

        self.windowMain = Tk()
        self.windowMain.resizable(False, False)
        self.windowMain.geometry(util().toCenterScreen(400, 210))
        self.windowMain.focus_force()
        self.windowMain.title('IGTEC - EDITAR PRODUTO')
        self.windowMain['bg'] = 'White'

        # Data
        lblNomeProduto = Label(self.windowMain, text='Nome do Produto:', font='Arial 12', bg='White')
        lblNomeProduto.place(x=10, y=10)
        
        etNomeProduto = Entry(self.windowMain, font='Arial 12', width=42)
        etNomeProduto.place(x=10, y=35)

        # Valor Compra e Valor Venda
        lblValorCompra = Label(self.windowMain, text='Valor de Compra', font='Arial 12', bg='White')
        lblValorCompra.place(x=10, y=75)

        etValorCompra = Entry(self.windowMain, font='Arial 12 ', width=20)
        etValorCompra.place(x=10, y=100)

        lblValorVenda = Label(self.windowMain, text='Valor de Venda:', font='Arial 12', bg='White')
        lblValorVenda.place(x=210, y=75)

        etValorVenda = Entry(self.windowMain, font='Arial 12 ', width=20)
        etValorVenda.place(x=210, y=100)

        def save():

            if etNomeProduto.get() != '' and etValorCompra.get() != '' and etValorVenda.get() != '':
                bd().updateProduto(
                    self.id,
                    etNomeProduto.get().upper(),
                    float(etValorCompra.get().replace(',', '.')),
                    float(etValorVenda.get().replace(',', '.'))
                )

                messagebox.showinfo('', 'PRODUTO ATUALIZADO !')

                #FECHAR EDIÇÃO
                self.windowMain.destroy()
                
            else:
                messagebox.showwarning('','PREENCHA TODOS OS CAMPOS!')
        
        def clear():
            #LIMPAR CMAPOS
            etNomeProduto.delete(0, END)
            etValorCompra.delete(0, END)
            etValorVenda.delete(0, END)

        def setCampos():
            #PEGAR INFOS DO BD
            produto = bd().getProdutoId(self.id)[0]
            
            #SETAR CAMPOS
            etNomeProduto.insert(0, produto[1])
            etValorCompra.insert(0, produto[2])
            etValorVenda.insert(0,  produto[3])

        #SALVAR
        imagem_salvar = PhotoImage(file=f"src/salvar_editar_48.png")
        btExibir = Button(self.windowMain, image=imagem_salvar, bg='White', bd=0, command=lambda: save())
        btExibir.imagem = imagem_salvar
        btExibir.place(x=270, y=150)

        #VOLTAR
        imagem_voltar = PhotoImage(file=f"src/voltar_48.png")
        btVoltar = Button(self.windowMain, image=imagem_voltar, bg='White', bd=0, command=lambda: self.windowMain.destroy())
        btVoltar.imagem = imagem_voltar
        btVoltar.place(x=340, y=150)
        
        #SETAR CAMPOS
        setCampos()

        #FOCA NO CAMPO DE NOME
        etNomeProduto.focus_force()

        self.windowMain.mainloop()
#Tela_Editar_Produto(1)