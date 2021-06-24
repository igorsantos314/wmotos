import sqlite3
import os

class bd:

    def __init__(self):

        #LISTA DE MESES
        self.months = ['JANEIRO', 'FEVEREIRO', 'MARCO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']

        caminhoAtual = os.getcwd()

        self.conection = sqlite3.connect('{}/src/wmotos.db'.format(caminhoAtual))
        self.cur = self.conection.cursor()

    def insertOS(self, data_entrada, saida, nome_cliente, veiculo, desc, laudo_tecnico, forma_pagamento, status, valor_mao_obra, valor_pecas):

        #INSERIR DADOS NA TABELA GASTOS
        command = f'INSERT INTO ordem_servico(entrada, saida, cliente, veiculo, descricao, laudo, pagamento, status, mao_de_obra, valor_de_pecas) VALUES("{data_entrada}", "{saida}", "{nome_cliente}", "{veiculo}", "{desc}", "{laudo_tecnico}", "{forma_pagamento}", "{status}", {valor_mao_obra}, {valor_pecas} )'
        
        self.cur.execute(command)
        self.conection.commit()

    def delOS(self, id):
        #DELETAR OS
        command = f'DELETE FROM ordem_servico WHERE id={id}'
        
        self.cur.execute(command)
        self.conection.commit()

    def getAllOS(self):
        show = "SELECT * FROM ordem_servico"
        self.cur.execute(show)

        #RETORNA LISTA DE OS
        return self.cur.fetchall()

    def getOS(self, id):
        show = f"SELECT * FROM ordem_servico WHERE id={id}"
        self.cur.execute(show)

        #RETORNA LISTA DE OS
        return self.cur.fetchall()

