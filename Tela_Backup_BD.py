import os
from tkinter import messagebox
from datetime import date
from Persistencia import bd
from tkinter import *
from tkinter import ttk
import shutil
from util import util
import hashlib
from module_json import json_ws

class Backup_BD:

    def __init__(self):
        
        # DATA ATUAL
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year

        self.data_atual = f'{self.day}-{self.month}-{self.year}'
        self.origem = 'wmotos.db'
        self.list_devices = ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        self.list_color = [ 'SpringGreen', 'SaddleBrown', 'Black', 'SlateBlue', 'DarkSlateGray',
                            'Indigo', 'DarkRed', 'DarkOrange', 'Goldenrod', 'MidnightBlue']

        #JANELA MAIN
        self.login()

    def login(self):

        windowLogin = Tk()
        windowLogin.resizable(False, False)
        windowLogin.geometry(util().toCenterScreen(160,70))
        windowLogin.focus_force()
        windowLogin.title('IGTEC')
        
        lblSenha = Label(windowLogin, text='Senha:')
        lblSenha.pack()

        etSenha = Entry(windowLogin, font='Arial 12 bold', show='*')
        etSenha.pack()

        def verify(event):
            hash =  hashlib.md5(etSenha.get().encode())
            senha = hash.hexdigest()

            if senha == json_ws().getPwCont():
                #DESTRUIR JANELA
                windowLogin.destroy()

                #CHAMAR CONTABILIDADE
                self.window_bd()
            else:
                messagebox.showerror('', 'SENHA INCORRETA !')
                windowLogin.destroy()

        etSenha.focus_force()
        windowLogin.bind('<Return>', verify)

        windowLogin.mainloop()

    def window_bd(self):

        self.windowMain = Tk()
        self.windowMain.resizable(False, False)
        self.windowMain.geometry(util().toCenterScreen(400, 100))
        self.windowMain.focus_force()
        self.windowMain.title('IGTEC - BACKUP')

        list_bt = []

        def getDevices():
            
            for pos, device in enumerate(self.list_devices):
                path = f"{device}:/"

                #CRIAR BOTOES COM O PATH
                if os.path.isdir(path):
                    
                    list_bt.append(
                        Button(text=str(path), font='Arial 12 bold', bg='DodgerBlue', fg='White', bd=0, width=8, height=2)
                    )
            
            #VERRE LISTA DE BOTOES PARA POSICIONAR E ATTR COMMAND
            for d in list_bt:
                path = f"{d['text']}"
                d['command'] = lambda: startBackup(path)
                d.pack(side=LEFT, padx=2)
        
        def startBackup(device):
            
            if messagebox.askquestion('','NÃO DESLIGUE OU FECHE O COMPUTADOR, DESEJA CONTINUAR?'):

                try:
                    #INCIAR BACKUP
                    self.createBackup(device)

                    #SUCESSO
                    data = self.data_atual.replace('-','/')
                    messagebox.showinfo('',f'BACKUP FEITO - DATA:{data}')

                except:
                    messagebox.showerror('','NÃO FOI POSSIVEL REALIZAR O BACKUP')

            #FECHAR A JANELA
            self.windowMain.destroy()

        def voltar(event):
            self.windowMain.destroy()

        lblDevice = Label(self.windowMain, text='ESCOLHA O DISPOSITIVO:', font='Arial 12 bold')
        lblDevice.pack()

        #BUSCAR DISPOSITIVOS
        getDevices()
        
        #ATALHO
        self.windowMain.bind("<Escape>", voltar)

        self.windowMain.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.windowMain.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.windowMain.attributes("-fullscreen", self.fullScreenState)
        self.windowMain.geometry('730x460')
        
    def createBackup(self, device):

        self.destino = f'{device}/{self.data_atual}-wmotos.db'

        #REALIZAR BACKUP PARA UNIDADE REMOVIVEL
        shutil.copy(self.origem, self.destino)