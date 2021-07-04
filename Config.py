from module_json import json_ws
from tkinter import scrolledtext
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Tela_Editar_OS:

    def __init__(self):
        # OBEJTO OS
        self.window()

    def window(self):

        self.windowMain = Tk()
        self.windowMain.resizable(False, False)
        self.windowMain.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.windowMain.title('EDITAR ORDEM DE SERVIÇO')
        self.windowMain['bg'] = 'White'

        self.windowMain.mainloop()

        