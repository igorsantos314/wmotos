import os
from datetime import datetime

class print_document:

    def __init__(self, conteudo):
        
        self.caminho = "{}\\imprimir.txt".format(os.getcwd())
        
        # CREAR ARQ DE IMPRESSÃO
        self.createArqPrint(conteudo)

        # IMPRIMIR
        self.comprovantePrint()

    def setConteudoToPrint(self, conteudo):

        head =  ''
        head += '             __        __    __  __    ___    _____    ___    ____   \n'
        head += '             \ \      / /   |  \/  |  / _ \  |_   _|  / _ \  / ___|  \n'
        head += '              \ \ /\ / /    | |\/| | | | | |   | |   | | | | \___ \  \n'
        head += '               \ V  V /     | |  | | | |_| |   | |   | |_| |  ___) | \n'
        head += '                \_/\_/      |_|  |_|  \___/    |_|    \___/  |____/  \n'
        head += "--------------------------------------------------------------------------------\n"
        head += "CIDADE:                BEJO JARDIM\n"
        head += "RUA:                   JOÃO BATISTA SENHORINHO\n"
        head += "NÚMERO:                155\n"
        head += "PONTO DE REFERÊNCIA:   AVENIDA DO SESC\n"
        head += "WHATSAPP:              (81) 98250-0763\n"
        head += "--------------------------------------------------------------------------------\n\n"

        body  = "ORDEM DE SERVIÇO\n"
        body += "--------------------------------------------------------------------------------\n"
        body +=  "ID:                             " + conteudo[0] + "\n"
        body += "DATA DE ENTRADA:                " + conteudo[1] + "\n"   
        body += "DATA DE SAIDA:                  " + conteudo[2] + "\n"    
        body += "NOME DO CLIENTE:                " + conteudo[3] + "\n"        
        body += "VEICULO:                        " + conteudo[4] + "\n\n" 

        body += "--------------------------------------------------------------------------------\n"
        body += "DESCRIÇÃO DO CLIENTE:\n"
        body += "     " + conteudo[5] + "\n"

        body += "--------------------------------------------------------------------------------\n"
        body += "LAUDO TECNICO:\n"
        body += "     " + conteudo[6] + "\n"
        body += "--------------------------------------------------------------------------------\n\n"
        
        body += "FORMA DE PAGAMENTO:             " + conteudo[7] + "\n"
        body += "STATUS:                         " + conteudo[8] + "\n"
        body += "VALOR DE MÃO DE OBRA:           R$ " + conteudo[9] + "\n"
        body += "VALOR EM PEÇAS:                 R$ " + conteudo[10]+ "\n"

        body += "--------------------------------------------------------------------------------\n\n"

        bottom = "DATA E HORA IMPRESSÃO: " + datetime.now().strftime('%d/%m/%Y %H:%M')

        return f"{head}{body}{bottom}"

    def createArqPrint(self, conteudo):

        #ESCRVE OS DADS NO ARQUIVO DE IMPRESSÃO
        arquivo = open(self.caminho, "w")
        arquivo.write(self.setConteudoToPrint(conteudo))

        arquivo.close()

    def comprovantePrint(self):
        # COMANDO DE IMPRESSÃO
        os.startfile(self.caminho, "print")