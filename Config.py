from showOS import consulta
from module_json import json_ws
from tkinter import scrolledtext
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
from util import util

class Config:

    def __init__(self):
        self.caminho = 'ws_motos_config.json'
        self.dict = self.ler()

        # OBEJTO OS
        self.login()

    def ler(self):
        #LER ARQUIVO
        with open(self.caminho, 'r', encoding='utf-8') as f:
            return json.load(f)

    def escrever(self, dict):
        #ESCREVER DICIONÁRIO NO JSON
        with open(self.caminho, 'w', encoding='utf-8') as f:
            json.dump(dict, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

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
            
            if etSenha.get() == json_ws().getPwConfig():
                #DESTRUIR JANELA
                windowLogin.destroy()

                #CHAMAR CONTABILIDADE
                self.window()
            else:
                messagebox.showerror('', 'SENHA INCORRETA !')
                windowLogin.destroy()

        etSenha.focus_force()
        windowLogin.bind('<Return>', verify)

        windowLogin.mainloop()

    def window(self):

        self.windowMain = Tk()
        self.windowMain.geometry(util().toCenterScreen(300, 200))
        self.windowMain.resizable(False, False)  
        self.windowMain.title('CONFIGURAÇÕES')
        self.windowMain.focus_force()
        self.windowMain['bg'] = 'White'

        lbl = Label(text='TIPO DE CONFIGURAÇÃO', bg='white')
        lbl.pack()

        comboConfig = ttk.Combobox(self.windowMain, font='Arial 10', width=18)

        comboConfig['values'] = tuple([i for i in self.dict])
        comboConfig.current(0)
        comboConfig.pack()

        bt = Button(self.windowMain, font='Arial 10', text='CONSULTAR', command=lambda:consulta())
        bt.pack(pady=10)
        
        lbl = Label(text='VALORES:', bg='white')
        lbl.pack()

        etValue = Entry(self.windowMain, font='Arial 10')
        etValue.pack()

        def consulta():
            #LIMPAR CAMPO
            etValue.delete(0, END)

            #EXIBIR INFORMAÇÕES
            etValue.insert(
                0, 
                self.dict[comboConfig.get()])

        def save():
           
            if messagebox.askyesno('','DESEJA SALVAR?'):
                 #MODIFICAR NO DICIONÁRIO
                self.dict[comboConfig.get()] = etValue.get()

                #SALVAR
                self.escrever(self.dict)

                messagebox.showinfo('','SALVO !!')
        
        btS = Button(self.windowMain, font='Arial 10', text='SALVAR', command=lambda:save())
        btS.pack(pady=10)

        comboConfig.focus_force()

        self.windowMain.mainloop()