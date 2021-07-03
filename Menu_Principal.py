from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import os
from Contabilidade import Contabilidade
from showOS import consulta
from Tela_Cadastrar_OS import Tela_Cadastrar_OS
from Contabilidade import Contabilidade
from module_json import json_ws
from Backup_BD import Backup_BD

class Menu_Principal:

    def __init__(self) -> None:
        self.window()

    def window(self):
        # Creating tkinter window
        window = Tk()
        window.resizable(False, False)
        window.geometry('850x480')
        window.title('WMOTOS - IGOR SANTOS SISTEMAS')
        window['bg'] = 'White'

        #LOGO
        imagem = PhotoImage(file=f"{json_ws().getPathLogo()}")
        w = Label(window, image=imagem)
        w.imagem = imagem
        w.place(x=150, y=150)

        #NOVA ORDEM DE SERVIÇO
        imagem_new_os = PhotoImage(file=f"src/new_os.png")
        btNewOS = Button(window, image=imagem_new_os, bg='White', command=lambda:open('Nova'))
        btNewOS.imagem = imagem_new_os
        btNewOS.place(x=10, y=10)

        #EXIBIR ORDENS DE SERVIÇO
        imagem_exibir = PhotoImage(file=f"src/exibir_os.png")
        btExibir = Button(window, image=imagem_exibir, bg='White', command=lambda:open('Exibir'))
        btExibir.imagem = imagem_exibir
        btExibir.place(x=120, y=10)

        #EXIBIR ORDENS DE SERVIÇO
        imagem_contabilidade = PhotoImage(file=f"src/cont.png")
        btCont = Button(window, image=imagem_contabilidade, bg='White', command=lambda:open('C_Total'))
        btCont.imagem = imagem_contabilidade
        btCont.place(x=230, y=10)

        #BACKUP
        imagem_backup = PhotoImage(file=f"src/backup.png")
        btBackup = Button(window, image=imagem_backup, bg='White', command=lambda:open('Backup'))
        btBackup.imagem = imagem_backup
        btBackup.place(x=340, y=10)

        #BACKUP
        imagem_sair = PhotoImage(file=f"src/sair.png")
        btSair = Button(window, image=imagem_sair, bg='White', command=lambda:window.destroy())
        btSair.imagem = imagem_sair
        btSair.place(x=450, y=10)

        #FECHAR MENU PARA CONTROLE DE TELAS
        def open(w):
            
            #FECHAR MENU
            window.destroy()

            if w == 'Nova':
                #ABRIR JANELA
                Tela_Cadastrar_OS()

                #REABRIR MENU
                Menu_Principal()

            elif w == 'Exibir':
                #ABRIR JANELA
                consulta()

                #REABRIR MENU
                Menu_Principal()
            
            elif w == 'C_Total':
                #ABRIR JANELA
                Contabilidade()

                #REABRIR MENU
                Menu_Principal()

            elif w == 'Backup':
                #ABRIR JANELA
                Backup_BD()

                #REABRIR MENU
                Menu_Principal()

        window.mainloop()

Menu_Principal()        