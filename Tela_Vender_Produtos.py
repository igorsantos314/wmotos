from Persistencia import bd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from util import util
from Tela_Cadastrar_Produto import Tela_Cadastrar_Produto
from Tela_Show_Produto import Tela_Show_Produto
from module_print import print_document

class Tela_Vender_Produtos:

    def __init__(self) -> None:
        #VARIAVEIS GLOBAIS
        self.subtotal = 0
        self.quant = 0
        self.total = 0

        self.id_atual = None
        self.enable_venda = True

        self.window()

    def window(self):
        
        self.windowMain = Tk()
        self.windowMain.resizable(False, False)
        self.windowMain.geometry(util().toCenterScreen(1000, 600))
        self.windowMain.focus_force()
        self.windowMain.title('IGTEC - VENDER PRODUTOS')
        self.windowMain['bg'] = 'White'
        
        #TREEVIEW BUSCAR PRODUTO
        lblNomeProduto = Label(self.windowMain, text='BUSCAR:', font='Arial 12', bg='White')
        lblNomeProduto.place(x=10, y=120)
        
        etNomeProduto = Entry(self.windowMain, font='Arial 12', width=35)
        etNomeProduto.place(x=105, y=120)

        style = ttk.Style(self.windowMain)
        style.theme_use('vista')

        style.configure(
            "Treeview",
            background="White",
            fieldbackground='White'
        )

        style.map("Treeview", background=[('selected', 'DodgerBlue')], foreground=[('selected', 'White')])

        # Using treeview widget 
        treevProduto = ttk.Treeview(self.windowMain, selectmode ='browse', height=13) 

        # Calling pack method w.r.to treeview 
        treevProduto.place(x=10, y=160)
        
        # Constructing vertical scrollbar 
        # with treeview 
        verscrlbar = ttk.Scrollbar(self.windowMain, 
                                orient ="vertical",
                                command = treevProduto.yview) 

        # scrollbar 
        #verscrlbar.pack(side ='right', fill ='x') 

        # Configuring treeview 
        treevProduto.configure(xscrollcommand = verscrlbar.set) 

        # Defining number of columns 
        treevProduto["columns"] = ("1", "2", "3")

        # Defining heading 
        treevProduto['show'] = 'headings'

        # Assigning the width and anchor to the 
        # respective columns 
        treevProduto.column("1", width = 60, anchor ='c') 
        treevProduto.column("2", width = 250, anchor ='se')
        treevProduto.column("3", width = 100, anchor ='se')

        # Assigning the heading names to the 
        # respective columns 
        treevProduto.heading("1", text ="Id") 
        treevProduto.heading("2", text ="Nome do Produto") 
        treevProduto.heading("3", text ="Valor")

        #TREEVIEW DE VENDA DE PRODUTOS
        imagem_produtos = PhotoImage(file=f"src/carrinho_compras.png")
        lblVendas = Label(self.windowMain, image=imagem_produtos, bg='White', bd=0)
        lblVendas.imagem = imagem_produtos
        lblVendas.place(x=265, y=10)

        lblVenda = Label(self.windowMain, text='SETOR DE VENDAS', font='Arial 30 bold', bg='White', fg='DodgerBlue')
        lblVenda.place(x=375, y=35)

        treevVenda = ttk.Treeview(self.windowMain, selectmode ='browse', height=15) 

        # Calling pack method w.r.to treeview 
        treevVenda.place(x=440, y=120)

        # Constructing vertical scrollbar 
        # with treeview 
        verscrlbarVenda = ttk.Scrollbar(self.windowMain, 
                                orient ="vertical",
                                command = treevVenda.yview) 

        # scrollbar 
        #verscrlbarVenda.pack(side ='right', fill ='x') 

        # Configuring treeview 
        treevVenda.configure(xscrollcommand = verscrlbarVenda.set) 

        # Defining number of columns 
        treevVenda["columns"] = ("1", "2", "3", "4", "5")

        # Defining heading 
        treevVenda['show'] = 'headings'

        # Assigning the width and anchor to the 
        # respective columns 
        treevVenda.column("1", width = 70, anchor ='c') 
        treevVenda.column("2", width = 237, anchor ='se')
        treevVenda.column("3", width = 70, anchor ='se')
        treevVenda.column("4", width = 70, anchor ='se')
        treevVenda.column("5", width = 70, anchor ='se')

        # Assigning the heading names to the 
        # respective columns 
        treevVenda.heading("1", text ="Id Prod.")
        treevVenda.heading("2", text ="Produto") 
        treevVenda.heading("3", text ="Subtotal")
        treevVenda.heading("4", text ="Quant.")
        treevVenda.heading("5", text ="Total")

        # -- VALORES --
        lblInfoSub = Label(text='SUBTOTAL: ', font='Arial 20', bg='White', fg='Black')
        lblInfoSub.place(x=10, y=470)
        
        lblSubTotal = Label(text='', font='Arial 20 bold', bg='White', fg='DodgerBlue')
        lblSubTotal.place(x=170, y=470)
        
        lblInfoQuant = Label(text='QUANT: ', font='Arial 20', bg='White', fg='Black')
        lblInfoQuant.place(x=440, y=470)

        lblQuant = Label(text='', font='Arial 20 bold', bg='White', fg='DarkOrange')
        lblQuant.place(x=550, y=470)

        lblInfoTotal = Label(text='TOTAL: ', font='Arial 20', bg='White', fg='Black')
        lblInfoTotal.place(x=650, y=470)

        lblTotal = Label(text='', font='Arial 20 bold', bg='White', fg='Green')
        lblTotal.place(x=750, y=470)
        
        # -- BOTÕES DE ACESSO -- 
        tam_bt = 18
        alt_bt = 2
        bg_bt = 'DodgerBlue'
        fg_bt = 'White'

        btCadastrarProduto = Button(text='(F1) Cadastrar Prod.', font='Arial 12 bold', bd=0, bg='DarkOrange', fg=fg_bt, width=tam_bt, height=alt_bt, command=lambda: cadastrarProduto(None))
        btCadastrarProduto.place(x=10, y=540)

        btConsultarProduto = Button(text='(F2) Consultar Prod.', font='Arial 12 bold', bd=0, bg=bg_bt, fg=fg_bt, width=tam_bt, height=alt_bt, command=lambda: exibirProdutos(None))
        btConsultarProduto.place(x=200, y=540)

        btFinalizarVenda = Button(text='(F3) Finalizar Venda', font='Arial 12 bold', bd=0, bg='Green', fg=fg_bt, width=tam_bt, height=alt_bt, command=lambda: salvar(None))
        btFinalizarVenda.place(x=390, y=540)

        btFinalizarVenda = Button(text='(F4) Cancelar Venda', font='Arial 12 bold', bd=0, bg='Red', fg=fg_bt, width=tam_bt, height=alt_bt, command=lambda: cancelarVenda(None))
        btFinalizarVenda.place(x=580, y=540)

        btFinalizarVenda = Button(text='(F6) Consultar Vendas', font='Arial 12 bold', bd=0, bg='DarkSlateGray', fg=fg_bt, width=tam_bt, height=alt_bt, command=lambda: telaVendas(None))
        btFinalizarVenda.place(x=770, y=540)
        
        def refreshValores():
            #SETAR VALORES
            lblSubTotal['text'] = f'R$ {self.subtotal:.2f}'
            lblQuant['text'] = f'{self.quant}'
            lblTotal['text'] = f'R$ {self.total:.2f}'

        def buscar(event):
            #LIMPAR TABELA
            treevProduto.delete(*treevProduto.get_children())

            #INSERIR NO TREEVIEW DE PRODUTO
            for produto in bd().getNomeProduto(etNomeProduto.get().upper()):
                treevProduto.insert("", 'end', text ="L1", values=(produto[0], produto[1], produto[3]))

        def addCarrinho(event):
            
            quant = self.etQuant.get()

            if quant != '':
                
                #LINHA SELECIONADA
                produtoSelecionado = treevProduto.selection()[0]

                #PEGA O ID
                id = treevProduto.item(produtoSelecionado, "values")[0]

                #PEGA O NOME
                nome = treevProduto.item(produtoSelecionado, "values")[1]

                #PEGA O VALOR
                valor = float(treevProduto.item(produtoSelecionado, "values")[2])
                
                #CALULAR O VALOR TOTAL
                total = int(quant) * valor

                #INSERIR NO CARRINHO
                treevVenda.insert("", 'end', text ="L1", values=(id, nome, valor, quant, total))

                #ATUALIZAR VALORES
                self.total += total
                self.subtotal += valor
                self.quant += int(quant)

                refreshValores()

                #FECHAR CAMPO DE QUANTIDADE
                fecharQuantidade(None)

        def removerCarrinho(event):

            if len(treevVenda.selection()) == 0:
                messagebox.showwarning('','POR FAVOR SELECIONE UM ITEM DO CARRINHO')

            else:
                #LINHA SELECIONADA
                produtoSelecionado = treevVenda.selection()[0]

                subtotal = float(treevVenda.item(produtoSelecionado, "values")[2])
                quantidade = int(treevVenda.item(produtoSelecionado, "values")[3])
                
                total = subtotal * quantidade

                #ATUALIZAR VALORES
                self.total -= total
                self.subtotal -= subtotal
                self.quant -= quantidade

                refreshValores()

                #REMOVER DA LISTA
                treevVenda.delete(produtoSelecionado)

        def fecharQuantidade(event):

            #DESTRUIR TELA DE QUANT
            self.lblFundoQuant.destroy()
            self.lblQuant.destroy()
            self.etQuant.destroy()

        def telaQuantidade(event):
            
            if len(treevProduto.selection()) == 0:
                messagebox.showwarning('','POR FAVOR SELECIONE UM PRODUTO')
                
            else:
                self.lblFundoQuant = Label(self.windowMain, bg='DodgerBlue', width=20, height=5)
                self.lblFundoQuant.pack(pady=200)
                
                self.lblQuant = Label(self.windowMain, text='Quantidade:', font='Arial 12 bold', bg='DodgerBlue', fg='White')
                self.lblQuant.place(x=440, y=210)

                self.etQuant = Entry(self.windowMain, font='Arial 12 bold', width=12)
                self.etQuant.insert(0, '1')
                self.etQuant.place(x=440, y=240)
                
                self.etQuant.focus_force()

                self.etQuant.bind('<Return>', addCarrinho)
                self.etQuant.bind('<Escape>', fecharQuantidade)

        # --- TELA EMBUTIDA PARA CONSULTAR VENDAS ---
        def telaVendas(event):
            
            if self.enable_venda:
                
                #DESABILITA PARA EVITAR SOBREPOSIÇÃO
                self.enable_venda = False

                cor_fundo = 'White'

                #LIMPAR
                limpar()

                def seachDataBase():
                    #LIMPA A TABELA PARA A NOVA VENDA
                    limpar_consultar_venda()

                    #FAZ A BUSCA DA VENDA NO BANCO DE DADOS
                    venda = bd().getVendaId(self.id_atual)

                    #LIMPA OS VALORES DA VENDA
                    lblCountConsultaSubtotal['text'] = ''
                    lblCountConsultaQuant['text']    = ''
                    lblCountConsultaTotal['text']    = ''

                    if venda:
                        #VALORES A EXIBIR
                        subtotal = 0
                        quant = 0
                        total = 0
                        
                        #VARRE A LISTA DE PRODUTOS DA VENDA
                        for v in venda:
                            
                            subtotal_produto = float(v[3])
                            quant_produto = int(v[4])
                            total_produto = subtotal_produto * quant_produto

                            #SOMA OS VALORES DA VENDA
                            subtotal += subtotal_produto
                            quant += quant_produto
                            total += total_produto

                            #PREENCHER TABELA COM OS DADOS DA VENDA
                            treevViewVenda.insert("", 'end', text ="L1", 
                                values=(
                                    v[1], 
                                    v[2], 
                                    f"{subtotal_produto:.2f}".replace('.',','), 
                                    v[4], 
                                    f"{total_produto:.2f}".replace('.',',')
                                    )
                            )

                        #SOMA OS VALORES DA VENDA
                        lblCountConsultaSubtotal['text'] = f'R$ {subtotal:.2f}'.replace('.',',')
                        lblCountConsultaQuant['text']    = f'{quant}'
                        lblCountConsultaTotal['text']    = f'R$ {total:.2f}'.replace('.',',')

                #NAVEGAÇÃO
                def nav(position):
                    
                    if self.id_atual == None:
                        self.id_atual = 0
                        lblIdCount['text'] = self.id_atual

                        #EXIBE VENDA
                        seachDataBase()

                    elif position == -1 and self.id_atual < 1:
                        pass

                    else:
                        #ATUALIZA ID DA VENDA
                        self.id_atual += position
                        lblIdCount['text'] = self.id_atual
                        
                        #EXIBE VENDA
                        seachDataBase()

                def limpar_consultar_venda():
                    #LIMPAR TABELA PARA RECEBER NOVA VENDA
                    treevViewVenda.delete(*treevViewVenda.get_children())

                def fechar_consultar_venda():
                    #RESETAR ID DA CONSULTA
                    self.id_atual = None

                    #DESTRUIR ITENS
                    self.lblFundoVendas.destroy()
                    treevViewVenda.destroy()
                    
                    lblIdCount.destroy()
                    lblNumeroVenda.destroy()

                    btDireita.destroy()
                    btEsquerda.destroy()
                    btDeletar.destroy()
                    btEditar.destroy()
                    btImpressora.destroy()

                    lblBuscarVenda.destroy()
                    etBuscarVenda.destroy()

                    #VALORES
                    lblConsultaSubtotal.destroy()
                    lblCountConsultaSubtotal.destroy()

                    lblConsultaQuant.destroy()
                    lblCountConsultaQuant.destroy()

                    lblConsultaTotal.destroy()
                    lblCountConsultaTotal.destroy()

                    btSair.destroy()

                    #FOCAR NO CAMPO DE BUSCA
                    etNomeProduto.focus_force()

                    #HABILITAR PARA ABRIR TELA DE EDIÇÃO
                    self.enable_venda = True

                def consulta_venda(event):

                    #VERIFICA SE O USUARIO DIGITOU UM VALOR VALIDO
                    try:
                        #PEGA O ID DO USUARIO
                        self.id_atual = int(etBuscarVenda.get())

                        #EXIBE O ID
                        lblIdCount['text'] = self.id_atual

                        #EXIBE VENDA
                        seachDataBase()
                    except:
                        #LIMPA O CAMPO DE CONSULTA
                        etBuscarVenda.delete(0, END)
                        etBuscarVenda.focus_force()

                        messagebox.showerror('','DIGITE UM VALOR VÁLIDO !')

                def deletar_venda():
                    
                    #VERIFICA SE A VENDA É VALIDA
                    if len(treevViewVenda.get_children()) == 0:
                        messagebox.showwarning('','ESTÁ VENDA É VAZIA !')

                    elif messagebox.askyesno('',f'APAGAR VENDA NÚMERO {self.id_atual} ?'):
                        #APAGAR VENDA
                        bd().delVenda(self.id_atual)

                        #LIMPA OS DADOS
                        limpar_consultar_venda()

                        etBuscarVenda.delete(0, END)
                        self.id_atual = None

                        #LIMPA O CAMPO DE ID
                        lblIdCount['text'] = ''

                        messagebox.showinfo('','APAGADO !')

                def imprimir():
                    
                    if len(treevViewVenda.get_children()) == 0:
                        messagebox.showwarning('','ESTÁ VENDA É VAZIA !')

                    elif messagebox.askyesno('',f'IMPRIMIR VENDA NÚMERO {self.id_atual} ?'):
                        
                        list_to_print = [self.id_atual]

                        #VARRE A LISTA DE VENDA ATUAL
                        for item in treevViewVenda.get_children():
                            
                            tuple_dados = ( treevViewVenda.item(item, "values")[0],
                                            treevViewVenda.item(item, "values")[1],
                                            treevViewVenda.item(item, "values")[2],
                                            treevViewVenda.item(item, "values")[3],
                                            treevViewVenda.item(item, "values")[4]
                                            )

                            list_to_print.append(tuple_dados)

                        #ENVIAR PARA IMPRESSÃO
                        print_document('venda', list_to_print)

                        #MENSAGEM
                        #messagebox.showinfo('', 'AGUARDE, ENVIADO PARA A IMPRESSORA !')

                def editar_venda():
                    messagebox.showinfo('','EM DESENVOLVIMENTO ...')
                    
                self.lblFundoVendas = Label(self.windowMain, bg=cor_fundo, width=150, height=50)
                self.lblFundoVendas.pack()

                #EXIBIR O ID DA VENDA
                lblNumeroVenda = Label(text='Venda Nº:', font='Arial 25 bold', bg=cor_fundo)
                lblNumeroVenda.place(x=10, y=10)
                
                lblIdCount = Label(text='', font='Arial 25 bold', bg=cor_fundo, fg='#912FBD')
                lblIdCount.place(x=180, y=10)

                #CAMPO PARA BUSCAR VENDA
                lblBuscarVenda = Label(text='Buscar:', font='Arial 12', bg=cor_fundo)
                lblBuscarVenda.place(x=10, y=70)

                etBuscarVenda = Entry(font='Arial 12 bold', fg='#912FBD')
                etBuscarVenda.place(x=80, y=70)

                #OPÇÕES
                imagem_impressora = PhotoImage(file=f"src/impressora_48.png")
                btImpressora = Button(self.windowMain, image=imagem_impressora, bg=cor_fundo, bd=0, command=lambda:imprimir())
                btImpressora.imagem = imagem_impressora
                btImpressora.place(x=795, y=50)

                imagem_editar = PhotoImage(file=f"src/editar_48.png")
                btEditar = Button(self.windowMain, image=imagem_editar, bg=cor_fundo, bd=0, command=lambda:editar_venda())
                btEditar.imagem = imagem_editar
                btEditar.place(x=845, y=50)

                imagem_deletar = PhotoImage(file=f"src/deletar_48.png")
                btDeletar = Button(self.windowMain, image=imagem_deletar, bg=cor_fundo, bd=0, command=lambda:deletar_venda())
                btDeletar.imagem = imagem_deletar
                btDeletar.place(x=895, y=50)

                imagem_sair = PhotoImage(file=f"src/fechar_consulta.png")
                btSair = Button(self.windowMain, image=imagem_sair, bg=cor_fundo, bd=0, command=lambda:fechar_consultar_venda())
                btSair.imagem = imagem_sair
                btSair.place(x=945, y=50)

                #NAVEGAÇÃO ENTRE VENDAS
                imagem_direita = PhotoImage(file=f"src/seta_direita_48.png")
                btDireita = Button(self.windowMain, image=imagem_direita, bg=cor_fundo, bd=0, command=lambda:nav(1))
                btDireita.imagem = imagem_direita
                btDireita.place(x=745, y=50)

                imagem_esquerda = PhotoImage(file=f"src/seta_esquerda_48.png")
                btEsquerda = Button(self.windowMain, image=imagem_esquerda, bg=cor_fundo, bd=0, command=lambda:nav(-1))
                btEsquerda.imagem = imagem_esquerda
                btEsquerda.place(x=695, y=50)

                #TABELA PARA EXIBIR A VENDA
                treevViewVenda = ttk.Treeview(self.windowMain, selectmode ='browse', height=16)
                treevViewVenda.place(x=10, y=100)

                treevViewVenda["columns"] = ("1", "2", "3", "4", "5")
                treevViewVenda['show'] = 'headings'

                treevViewVenda.column("1", width = 120, anchor ='c') 
                treevViewVenda.column("2", width = 455, anchor ='se')
                treevViewVenda.column("3", width = 150, anchor ='se')
                treevViewVenda.column("4", width = 100, anchor ='se')
                treevViewVenda.column("5", width = 150, anchor ='se')

                treevViewVenda.heading("1", text ="Id") 
                treevViewVenda.heading("2", text ="Nome do Produto") 
                treevViewVenda.heading("3", text ="Subtotal")
                treevViewVenda.heading("4", text ="Quantidade")
                treevViewVenda.heading("5", text ="Total")

                # ---- VALORES DA COMPRA ----
                lblConsultaSubtotal = Label(text='Subtotal:', font='Arial 20', bg=cor_fundo)
                lblConsultaSubtotal.place(x=10, y=460)
                
                lblCountConsultaSubtotal = Label(text='', font='Arial 20 bold', fg='DodgerBlue', bg=cor_fundo)
                lblCountConsultaSubtotal.place(x=130, y=460)

                lblConsultaQuant = Label(text='Quantidade:', font='Arial 20', bg=cor_fundo)
                lblConsultaQuant.place(x=350, y=460)
                
                lblCountConsultaQuant = Label(text='', font='Arial 20 bold', fg='DarkOrange', bg=cor_fundo)
                lblCountConsultaQuant.place(x=510, y=460)

                lblConsultaTotal = Label(text='Total:', font='Arial 20', bg=cor_fundo)
                lblConsultaTotal.place(x=730, y=460)
                
                lblCountConsultaTotal = Label(text='', font='Arial 20 bold', fg='Green', bg=cor_fundo)
                lblCountConsultaTotal.place(x=810, y=460)
                
                #FOCA NO CAMPO DE DIGITAR O ID DA VENDA
                etBuscarVenda.focus_force()

                #TECLAS DE ATALHO
                etBuscarVenda.bind('<Return>', consulta_venda)
            
        def limpar():
            #LIMPA AS TABELAS
            treevProduto.delete(*treevProduto.get_children())
            treevVenda.delete(*treevVenda.get_children())

            #RESETA OS VALORES
            self.total = 0
            self.subtotal = 0
            self.quant = 0

            refreshValores()

        def salvar(event):
            
            if self.enable_venda:
                #VERIFICA SE TEM ALGUM ITEM NO CARRINHO
                if len(treevVenda.get_children()) != 0:
                    if messagebox.askyesno('','FINALIZAR VENDA?'):
                        
                        list_prod = []

                        for item in treevVenda.get_children():
                            
                            tuple_dados = ( treevVenda.item(item, "values")[0],
                                            treevVenda.item(item, "values")[1],
                                            treevVenda.item(item, "values")[2],
                                            treevVenda.item(item, "values")[3])
                            
                            list_prod.append(tuple_dados)
                        
                        #ENVIAR PRO BANCO DE DADOS
                        bd().insertVendaProduto(list_prod)

                        #LIMPAR VENDA
                        limpar()
                        
                        messagebox.showinfo('','SALVO !')

                        #FOCAR NO CAMPO DE CONSULTA
                        etNomeProduto.focus_force()
                        
                        #PEGAR O ID DA VENDA
                        id_current = bd().getMaxIdVenda()

                        #SETA O ID NA LISTA PARA IMPRESSÃO
                        list_impressao = [
                            id_current
                        ]

                        #VARRE A LISTA DE PRODUTOS
                        for p in list_prod:
                            #MANDA OARA UMA LISTA DE IMPRESSAO
                            list_impressao.append(p)
                        
                        if messagebox.askyesno('','IMPRIMIR COMPROVANTE?'):
                            #IMPRIMIR A VENDA
                            print_document('venda', list_impressao)
                            
                else:
                    messagebox.showwarning('','CARRINHO VAZIO :(')
        
        def cancelarVenda(event):
            if self.enable_venda:
                if messagebox.askyesno('','CANCELAR VENDA?'):
                    try:
                        #TENTA FECHAR TELA DE QUANTIDADE CASO ABERTA
                        fecharQuantidade(None)
                    except:
                        pass
                        
                    #LIMPAR
                    limpar()
        
        def sair(event):
            #FECHAR JANELA
            self.windowMain.destroy()

        def cadastrarProduto(event):

            if self.enable_venda:
                #FECHAR JANELA
                sair(None)

                #ABRIR TELA DE CADASTRAR PRODUTO
                Tela_Cadastrar_Produto()

                #CHAMAR SETOR DE VENDAS
                Tela_Vender_Produtos()

        def exibirProdutos(event):
            if self.enable_venda:
                #FECHAR JANELA
                sair(None)

                #ABRIR TELA DE CADASTRAR PRODUTO
                Tela_Show_Produto()
                
                #CHAMAR SETOR DE VENDAS
                Tela_Vender_Produtos()

        #INICIALIZAR VALORES
        refreshValores()

        #FOCAR NO CAMPO DE BUSCAR POR NOME
        etNomeProduto.focus_force()

        #CAPTURA DE TECLAS
        treevProduto.bind('<Return>', telaQuantidade)
        treevVenda.bind('<Delete>', removerCarrinho)

        etNomeProduto.bind('<Return>', buscar)

        self.windowMain.bind('<F1>', cadastrarProduto)
        self.windowMain.bind('<F2>', exibirProdutos)
        self.windowMain.bind('<F3>', salvar)
        self.windowMain.bind('<F4>', cancelarVenda)
        self.windowMain.bind('<F6>', telaVendas)

        self.windowMain.bind('<Escape>', sair)

        self.windowMain.mainloop()

#Tela_Vender_Produtos()