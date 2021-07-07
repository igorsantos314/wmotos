import os
from datetime import datetime
from tkinter import messagebox

class print_document:

    def __init__(self, conteudo):
        
        self.caminho = "{}\\imprimir.txt".format(os.getcwd())
        
        # CREAR ARQ DE IMPRESSÃO
        self.createArqPrint(conteudo)

        # IMPRIMIR
        self.comprovantePrint()

    def setConteudoToPrint(self, conteudo):

        head = '                           ORDEM DE SERVIÇO - W MOTOS  \n'
        head += "________________________________________________________________________________\n"
        head += "CIDADE:                BEJO JARDIM\n"
        head += "RUA:                   JOÃO BATISTA SENHORINHO\n"
        head += "NÚMERO:                155\n"
        head += "PONTO DE REFERÊNCIA:   AVENIDA DO SESC\n"
        head += "WHATSAPP:              (81) 98250-0763\n"
        head += "________________________________________________________________________________\n\n"

        body  = "DADOS DA ORDEM DE SERVIÇO\n"
        body += "________________________________________________________________________________\n"
        body += f"ID:                             {conteudo[0]} \n"
        body += f"DATA DE ENTRADA:                {conteudo[1]} \n"   
        body += f"DATA DE SAIDA:                  {conteudo[2]} \n"    
        body += f"NOME DO CLIENTE:                {conteudo[3]} \n"   
        body += f"TELEFONE:                       {conteudo[4]} \n"     
        body += f"VEICULO:                        {conteudo[5]} \n\n" 

        body += "________________________________________________________________________________\n"
        body += "DESCRIÇÃO DO CLIENTE:\n"
        body += f"     {conteudo[6]}"

        body += "________________________________________________________________________________\n"
        body += "LAUDO TECNICO:\n"
        body += f"     {conteudo[7]}"
        body += "________________________________________________________________________________\n\n"
        
        body += f"FORMA DE PAGAMENTO:             {conteudo[8]} \n"
        body += f"STATUS:                         {conteudo[9]} \n"
        body += f"VALOR DE MÃO DE OBRA:           R$ {conteudo[10]:.2f} \n"
        body += f"VALOR EM PEÇAS:                 R$ {conteudo[11]:.2f}\n"
        body += f"OUTROS VALORES:                 R$ {conteudo[12]:.2f}\n"
        body += f"TOTAL:                          R$ {(conteudo[10] + conteudo[11] + conteudo[12]):.2f}\n"

        body += "________________________________________________________________________________\n\n"

        bottom = "DATA E HORA IMPRESSÃO: " + datetime.now().strftime('%d/%m/%Y %H:%M') + "\n\n\n\n\n"

        bottom += "                  ___________________________________________                    \n"
        bottom += "                           Assinatura do Responsável\n\n\n\n\n"

        bottom += "                  ___________________________________________                    \n"
        bottom += "                             Assinatura do Cliente"
        
        return f"{head}{body}{bottom}"

    def createArqPrint(self, conteudo):

        #ESCRVE OS DADS NO ARQUIVO DE IMPRESSÃO
        arquivo = open(self.caminho, "w")
        arquivo.write(self.setConteudoToPrint(conteudo))

        arquivo.close()

    def comprovantePrint(self):
        try:
            # COMANDO DE IMPRESSÃO
            os.startfile(self.caminho, "print")
            messagebox.showinfo('','IMPRESSÃO REALIZADA')
            
        except:
            messagebox.showerror('','ERROR[mdo_print:80] NÃO FOI POSSÍVEL REALIZAR A IMPRESSÃO')