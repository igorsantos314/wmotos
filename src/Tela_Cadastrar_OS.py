from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from Persistencia import bd

class Tela_Cadastrar_OS:

    def __init__(self):
        # DATA ATUAL
        self.day = date.today().day
        self.month = date.today().month
        self.year = date.today().year

        # OBEJTO OS
        self.window()

    def window(self):

        self.windowMain = Tk()
        self.windowMain.geometry('300x400')
        self.windowMain.title('Cadastrar Ordem de Serviço')

        # Data
        lblDataEntrada = Label(self.windowMain, text='Data de Entrada:')
        lblDataEntrada.place(x=10, y=10)

        etDataEntrada = Entry()
        etDataEntrada.place(x=10, y=30)

        lblDataSaida = Label(self.windowMain, text='Data de Saida:')
        lblDataSaida.place(x=150, y=10)

        etDataSaida = Entry()
        etDataSaida.place(x=150, y=30)

        # Cliente e Veiculo
        lblCliente = Label(self.windowMain, text='Cliente:*')
        lblCliente.place(x=10, y=60)

        etCliente = Entry()
        etCliente.place(x=10, y=80)

        lblVeiculo = Label(self.windowMain, text='Veiculo:*')
        lblVeiculo.place(x=150, y=60)

        etVeiculo = Entry()
        etVeiculo.place(x=150, y=80)

        # Descricao e Laudo
        lblDesc = Label(self.windowMain, text='Descrição do Cliente:')
        lblDesc.place(x=10, y=120)

        etDesc = Entry()
        etDesc.place(x=10, y=140)

        lblLaudo = Label(self.windowMain, text='Laudo Tecnico:')
        lblLaudo.place(x=150, y=120)

        etLaudo = Entry()
        etLaudo.place(x=150, y=140)

        # Pagamento
        lblPagamento = Label(self.windowMain, text='Forma de Pagamento:')
        lblPagamento.place(x=10, y=180)

        comboPagamento = ttk.Combobox(self.windowMain, width=17)

        comboPagamento['values'] = tuple(
            ['DINHEIRO', 'CARTÃO', 'PIX', 'OUTRO'])
        comboPagamento.current(0)
        comboPagamento.place(x=10, y=200)

        # Status
        lblStatus = Label(self.windowMain, text='Status:')
        lblStatus.place(x=150, y=180)

        comboStatus = ttk.Combobox(self.windowMain, width=17)

        comboStatus['values'] = tuple(
            ['EM ESPERA', 'EM ANDAMENTO', 'CONCLUIDO'])
        comboStatus.current(0)
        comboStatus.place(x=150, y=200)

        # Valores
        lblObra = Label(self.windowMain, text='Valor mão de Obra:')
        lblObra.place(x=10, y=240)

        etObra = Entry()
        etObra.insert(0, '0')
        etObra.place(x=10, y=260)

        lblPecas = Label(self.windowMain, text='Valor em Peças:')
        lblPecas.place(x=150, y=240)

        etPecas = Entry()
        etPecas.insert(0, '0')
        etPecas.place(x=150, y=260)

        # Botões de Salvar e Cancelar
        btSalvar = Button(text='SALVAR', width=16,
                          bg='SpringGreen', command=lambda: save())
        btSalvar.place(x=150, y=300)

        btSalvar = Button(text='CANCELAR', width=16, bg='Tomato', command=lambda: exit())
        btSalvar.place(x=150, y=340)

        # Funcoes
        def save():

            # MENSAGEM DE ERROR
            if etVeiculo.get() == '' or etCliente.get() == '':
                messagebox.showerror(
                    'AVISO', 'CAMPOS OBRIGATÓRIOS NÃO ESTÃO PREENCHIDOS')

            else:
                # SALVAR
                if messagebox.askyesno('', 'SALVAR OS?'):

                    bd().insertOS(
                        etDataEntrada.get(),
                        etDataSaida.get(),
                        etCliente.get().upper(),
                        etVeiculo.get().upper(),
                        etDesc.get().upper(),
                        etLaudo.get().upper(),
                        comboPagamento.get(),
                        comboStatus.get(),
                        etObra.get(),
                        etPecas.get()
                    )

                    messagebox.showinfo('','CADASTRADO COM SUCESSO !')

                # LIMPAR
                clear()

        def clear():
            # LIMPAR
            etDataEntrada.delete(0, END)
            etDataSaida.delete(0, END)
            etCliente.delete(0, END)
            etVeiculo.delete(0, END)
            etDesc.delete(0, END)
            etLaudo.delete(0, END)
            etObra.delete(0, END)
            etPecas.delete(0, END)

        def exit():
            self.windowMain.destroy()

        self.windowMain.mainloop()


Tela_Cadastrar_OS()
