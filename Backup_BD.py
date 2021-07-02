import os
from tkinter import messagebox
from datetime import date
from Persistencia import bd
from tkinter import *
from tkinter import ttk
import shutil

class Backup_BD:

    def __init__(self):
        
        # DATA ATUAL
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year

        self.data_atual = f'{self.day}-{self.month}-{self.year}'
        self.origem = 'wmotos.db'
        self.list_devices = ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']

        #JANELA MAIN
        self.window_bd()

    def window_bd(self):

        self.windowMain = Tk()
        self.windowMain.title('BACKUP')

        def getDevices():
            devices_disponible = []
            
            for device in self.list_devices:
                path = f"{device}:/"

                if os.path.isdir(path):
                    devices_disponible.append(path)

            return devices_disponible
        
        def startBackup():
            
            if messagebox.askquestion('','NÃO DESLIGUE OU FECHE O COMPUTADOR, DESEJA CONTINUAR?'):

                try:
                    #INCIAR BACKUP
                    self.createBackup(comboPagamento.get())

                    #SUCESSO
                    messagebox.showinfo('',f'BACKUP FEITO - DATA:{self.data_atual}')

                except:
                    messagebox.showerror('','NÃO FOI POSSIVEL REALIZAR O BACKUP')

            #FECHAR A JANELA
            self.windowMain.destroy()

        lblPagamento = Label(self.windowMain, text='ESCOLHA O DISPOSITIVO:')
        lblPagamento.pack()

        comboPagamento = ttk.Combobox(self.windowMain, width=17)

        comboPagamento['values'] = tuple(getDevices())
        comboPagamento.current(0)
        comboPagamento.pack()

        btSalvar = Button(self.windowMain, text='BACKUP', command=startBackup)
        btSalvar.pack()

        self.windowMain.mainloop()
        
    def createBackup(self, device):

        self.destino = f'{device}/{self.data_atual}-wmotos.db'

        #REALIZAR BACKUP PARA UNIDADE REMOVIVEL
        shutil.copy(self.origem, self.destino)