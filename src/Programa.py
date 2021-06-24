from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import os
from Contabilidade import Contabilidade
from showOS import consulta
from Tela_Cadastrar_OS import Tela_Cadastrar_OS
from Contabilidade import Contabilidade

class Menu_Principal:

    def __init__(self) -> None:
        self.window()

    def window(self):
        # Creating tkinter window
        window = Tk()
        window.geometry('993x480')
        window.title('CONSULTAR OS')

        # BARRA DE FUNÇÕES
        menubar = Menu(window, fg='Black')
        myMenu = Menu(menubar, tearoff=0)

        # MENU FILE
        fileMenuFile = Menu(myMenu, fg='Black')
        fileMenuFile.add_command(label='Nova', command=lambda:Tela_Cadastrar_OS())
        fileMenuFile.add_command(label='Exibir', command=lambda:consulta())
        fileMenuFile.add_separator()
        fileMenuFile.add_command(label='Contabilidade Diaria', command=lambda:consulta())
        fileMenuFile.add_command(label='Contabilidade Mensal', command=lambda:consulta())
        fileMenuFile.add_command(label='Contabilidade Total', command=lambda:Contabilidade())
        fileMenuFile.add_separator()
        fileMenuFile.add_command(
            label='Sair', command=lambda: window.destroy())

        menubar.add_cascade(label="ORDEM DE SERVIÇO", menu=fileMenuFile)

        #LOGO
        imagem = PhotoImage(file=f"{os.getcwd()}\\src\\logo_wmotos.png")
        w = Label(window, image=imagem)
        w.imagem = imagem
        w.pack()

        # configurar file menu
        window.config(menu=menubar)

        window.mainloop()

Menu_Principal()
