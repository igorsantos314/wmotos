from tkinter import ttk
from tkinter import *
from Contabilidade import Contabilidade
from showOS import consulta
from Tela_Cadastrar_OS import Tela_Cadastrar_OS
from Contabilidade import Contabilidade
from module_json import json_ws
from Backup_BD import Backup_BD
from util import util
from Config import Config

class Menu_Principal:

    def __init__(self) -> None:
        self.windowMain()

    def windowMain(self):
        # Creating tkinter window
        self.window = Tk()
        self.window.resizable(False, False)
        self.window.geometry(util().toCenterScreen(810, 490))
        self.window.focus_force()
        #self.window.attributes('-fullscreen', True)  
        #self.fullScreenState = False
        
        self.window.title('WMOTOS - IGOR SANTOS SISTEMAS')
        self.window['bg'] = 'White'

        #LOGO
        imagem = PhotoImage(file=f"{json_ws().getPathLogo()}")
        w = Label(self.window, image=imagem)
        w.imagem = imagem
        w.place(x=150, y=150)

        #NOVA ORDEM DE SERVIÇO
        imagem_new_os = PhotoImage(file=f"src/new_os.png")
        btNewOS = Button(self.window, image=imagem_new_os, bg='White', command=lambda:open('Nova'))
        btNewOS.imagem = imagem_new_os
        btNewOS.place(x=10, y=10)

        #EXIBIR ORDENS DE SERVIÇO
        imagem_exibir = PhotoImage(file=f"src/exibir_os.png")
        btExibir = Button(self.window, image=imagem_exibir, bg='White', command=lambda:open('Exibir'))
        btExibir.imagem = imagem_exibir
        btExibir.place(x=120, y=10)

        #EXIBIR ORDENS DE SERVIÇO
        imagem_contabilidade = PhotoImage(file=f"src/cont.png")
        btCont = Button(self.window, image=imagem_contabilidade, bg='White', command=lambda:open('C_Total'))
        btCont.imagem = imagem_contabilidade
        btCont.place(x=230, y=10)

        #BACKUP
        imagem_backup = PhotoImage(file=f"src/backup.png")
        btBackup = Button(self.window, image=imagem_backup, bg='White', command=lambda:open('Backup'))
        btBackup.imagem = imagem_backup
        btBackup.place(x=340, y=10)

        #CONFIGURAÇÕES
        imagem_config = PhotoImage(file=f"src/config.png")
        btConfig = Button(self.window, image=imagem_config, bg='White', command=lambda:open('Config'))
        btConfig.imagem = imagem_config
        btConfig.place(x=450, y=10)

        #SAIR
        imagem_sair = PhotoImage(file=f"src/sair.png")
        btSair = Button(self.window, image=imagem_sair, bg='White', command=lambda:self.window.destroy())
        btSair.imagem = imagem_sair
        btSair.place(x=560, y=10)

        #FECHAR MENU PARA CONTROLE DE TELAS
        def open(w):
            
            #FECHAR MENU
            self.window.destroy()

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

            elif w == 'Config':
                #ABRIR JANELA
                Config()
                
                #REABRIR MENU
                Menu_Principal()

        #self.window.bind("<F11>", self.toggleFullScreen)
        #self.window.bind("<Escape>", self.quitFullScreen)

        self.window.mainloop()
        
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
        self.window.geometry(self.toCenterScreen())