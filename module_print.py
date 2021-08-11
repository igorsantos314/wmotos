import os
from datetime import datetime
from tkinter import messagebox
import win32api

class print_document:

    def __init__(self, type, conteudo):
        
        self.caminho = "{}\\imprimir.txt".format(os.getcwd())
        
        # CREAR ARQ DE IMPRESSÃO
        self.createArqPrint(type, conteudo)

        # IMPRIMIR
        self.comprovantePrint()

    def setConteudoToPrintOs(self, conteudo):

        head = '                           ORDEM DE SERVIÇO - W MOTOS  \n'
        head += "________________________________________________________________________________\n"
        head += "CIDADE:                         BEJO JARDIM\n"
        head += "RUA:                            JOÃO BATISTA SENHORINHO\n"
        head += "NÚMERO:                         155\n"
        head += "PONTO DE REFERÊNCIA:            AVENIDA DO SESC\n"
        head += "WHATSAPP:                       (81) 98250-0763\n"
        head += "________________________________________________________________________________\n\n"

        body  = "DADOS DA ORDEM DE SERVIÇO\n"
        body += "________________________________________________________________________________\n"
        body += f"ID:                             {conteudo[0]} \n"
        body += f"DATA DE ENTRADA:                {conteudo[1]} \n"   
        body += f"DATA DE SAIDA:                  {conteudo[2]} \n"    
        body += f"NOME DO CLIENTE:                {conteudo[3]} \n"   
        body += f"TELEFONE 1:                     {conteudo[4]} \n"   
        body += f"TELEFONE 2:                     {conteudo[5]} \n"  
        body += f"VEICULO:                        {conteudo[6]} \n" 
        body += f"PLACA:                          {conteudo[7]} \n"
        body += f"QUILOMETRAGEM:                  {conteudo[8]} \n"
        
        body += "________________________________________________________________________________\n"
        body += "DESCRIÇÃO DO CLIENTE:\n"
        body += f"     {conteudo[9]}"

        body += "________________________________________________________________________________\n"
        body += "LAUDO TECNICO:\n"
        body += f"     {conteudo[10]}"
        body += "________________________________________________________________________________\n\n"
        
        body += f"FORMA DE PAGAMENTO:             {conteudo[11]} \n"
        body += f"STATUS:                         {conteudo[12]} \n"
        body += f"VALOR DE MÃO DE OBRA:           R$ {conteudo[13]:.2f} \n"
        body += f"VALOR EM PEÇAS:                 R$ {conteudo[14]:.2f}\n"
        body += f"OUTROS VALORES:                 R$ {conteudo[15]:.2f}\n"
        body += f"TOTAL:                          R$ {(conteudo[13] + conteudo[14] + conteudo[15]):.2f}\n"

        body += "________________________________________________________________________________\n\n"

        bottom = "IGTEC - IMPRESSO EM: " + datetime.now().strftime('%d/%m/%Y as %H:%M') + "\n\n\n\n\n"

        bottom += "                  ___________________________________________                    \n"
        bottom += "                           Assinatura do Responsável\n\n\n\n\n"

        bottom += "                  ___________________________________________                    \n"
        bottom += "                             Assinatura do Cliente"
        
        return f"{head}{body}{bottom}"

    def setConteudoToPrintVenda(self, conteudo):

        #PEGA O ID E REMOVE PARA ITERAR A LISTA DE PRODUTOS
        venda_id = conteudo[0]
        del conteudo[0]
        
        head = '                               NOTA DE VENDA - W MOTOS  \n'

        body =  "________________________________________________________________________________\n\n"
        body += f"VENDA NÚMERO: {venda_id}\n"
        body +=  "________________________________________________________________________________\n"
        body += "ID   PRODUTO                                 SUB.      QUANT.    TOTAL\n"
        body += "--------------------------------------------------------------------------------\n"

        subtotal = 0
        total = 0
        quantidade = 0

        for produto in conteudo:
            total_produto = float(produto[2].replace(',', '.')) * int(produto[3].replace(',', '.'))

            total += total_produto
            subtotal += float(produto[2].replace(',', '.'))
            quantidade += int(produto[3].replace(',', '.'))

            str_sub = f"{float(produto[2].replace(',', '.')):.2f}"

            t_id    = ' ' * (5-len(produto[0]))
            t_nome  = ' ' * (40-len(produto[1]))
            t_sub   = ' ' * (12-len(str_sub))
            t_quant = ' ' * (8-len(produto[3]))
            
            str_dados = f"{produto[0]}{t_id}{produto[1]}{t_nome}{produto[2]}{t_sub}{produto[3]}{t_quant}{total_produto}\n"
            body += str_dados.replace('.', ',') 
            
        bottom = "\n________________________________________________________________________________\n"

        str_total = f"SUBTOTAL: R${subtotal:.2f}              QUANTIDADE: {quantidade}              TOTAL: R${total:.2f}\n\n"
        bottom += str_total.replace('.', ',')

        bottom += "________________________________________________________________________________\n"
        bottom += "IGTEC - IMPRESSO EM: " + datetime.now().strftime('%d/%m/%Y as %H:%M') + "\n\n\n\n\n"

        return f"{head}{body}{bottom}"

    def createArqPrint(self, type, conteudo):

        #ESCRVE OS DADS NO ARQUIVO DE IMPRESSÃO
        arquivo = open(self.caminho, "w")

        #VERIFICA O TIPO DE IMPRESSÃO
        if type == 'os':
            arquivo.write(
                self.setConteudoToPrintOs(conteudo)
            )

        elif type == 'venda':
            arquivo.write(
                self.setConteudoToPrintVenda(conteudo)
            )

        arquivo.close()

    def comprovantePrint(self):
        try:
            # COMANDO DE IMPRESSÃO
            #os.startfile(self.caminho, "print")
            win32api.ShellExecute(0, "print", self.caminho, None, ".", 0)
            messagebox.showinfo('','AGUARDE, FOI ENVIADO PARA A IMPRESSORA!')
            
        except:
            messagebox.showerror('','ERROR[mdo_print:80] NÃO FOI POSSÍVEL REALIZAR A IMPRESSÃO')