import os
from tkinter import messagebox
from datetime import date
from Persistencia import bd
from tkinter import *
from tkinter import ttk
import shutil
from util import util

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
        self.window_bd()

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
                        Button(text=str(path), font='Arial 12 bold', bg='Black', fg='White', width=8, height=2)
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
                    messagebox.showinfo('',f'BACKUP FEITO - DATA:{self.data_atual}')

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