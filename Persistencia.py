import sqlite3
import os
from module_json import json_ws

class bd:

    def __init__(self):

        #LISTA DE MESES
        self.months = ['JANEIRO', 'FEVEREIRO', 'MARCO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']

        self.conection = sqlite3.connect(json_ws().getPathBd())
        self.cur = self.conection.cursor()

    def insertOS(self, data_entrada, saida, nome_cliente, telefone, veiculo, desc, laudo_tecnico, forma_pagamento, status, valor_mao_obra, valor_pecas, valor_outros):

        #INSERIR DADOS NA TABELA ORDEMS DE SERVIÇO
        command = f'INSERT INTO ordem_servico(entrada, saida, cliente, telefone, veiculo, descricao, laudo, pagamento, status, mao_de_obra, valor_de_pecas, valor_outros) VALUES("{data_entrada}", "{saida}", "{nome_cliente}", "{telefone}", "{veiculo}", "{desc}", "{laudo_tecnico}", "{forma_pagamento}", "{status}", {valor_mao_obra}, {valor_pecas}, {valor_outros})'
        
        self.cur.execute(command)
        self.conection.commit()

    def insertProduto(self, nome, valorCompra, valorVenda):
        #INSERIR DADOS NA TABELA PRODUTO
        command = f'INSERT INTO produto(nome, valor_compra, valor_venda) VALUES("{nome}", {valorCompra}, {valorVenda})'
        
        self.cur.execute(command)
        self.conection.commit()

    def delOS(self, id):
        #DELETAR OS
        command = f'DELETE FROM ordem_servico WHERE id={id}'
        
        self.cur.execute(command)
        self.conection.commit()

    def updateOS(self, id, data_entrada, saida, nome_cliente, telefone, veiculo, desc, laudo_tecnico, forma_pagamento, status, valor_mao_obra, valor_pecas, valor_outros):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET entrada='{data_entrada}', saida='{saida}', cliente='{nome_cliente}', telefone='{telefone}', veiculo='{veiculo}', descricao='{desc}', laudo='{laudo_tecnico}', pagamento='{forma_pagamento}', status='{status}', mao_de_obra={valor_mao_obra}, valor_de_pecas={valor_pecas}, valor_outros={valor_outros} WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updateStatusConcluido(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET status='CONCLUIDO' WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updateStatusAndamento(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET status='EM ANDAMENTO' WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updateStatusEspera(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET status='EM ESPERA' WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updatePagamentoDinheiro(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET pagamento='DINHEIRO' WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updatePagamentoCartao(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET pagamento='CARTÃO' WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updatePagamentoPix(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET pagamento='PIX' WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updatePagamentoOutro(self, id):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET pagamento='OUTRO' WHERE id={id};"

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
    
    def getValor(self, id):
        show = f"SELECT * FROM ordem_servico WHERE id={id}"
        self.cur.execute(show)
        
        #RETORNA O VALOR DA OS PELO ID
        return self.cur.fetchall()

    def getNomeVeiculoOS(self, str):

        show = f"SELECT * FROM ordem_servico WHERE cliente LIKE '%{str}%' OR veiculo LIKE '%{str}%'"
        self.cur.execute(show)

        #RETORNA LISTA DE OS
        return self.cur.fetchall()

    def getAllProduto(self):
        show = "SELECT * FROM produto"
        self.cur.execute(show)

        #RETORNA LISTA DE OS
        return self.cur.fetchall()

    # --- CONTABILIDADE ---
    def getAllMaoObra(self):

        show = f"SELECT sum(mao_de_obra) FROM ordem_servico WHERE status='CONCLUIDO'"
        self.cur.execute(show)

        valor = self.cur.fetchall()[0][0]

        if  valor == None:
            return 0

        #RETORNA O VALOR TOTAL
        return valor

    def getContabilidadeDia(self, data):

        show = f"SELECT sum(mao_de_obra) FROM ordem_servico WHERE saida='{data}' and status='CONCLUIDO'"
        self.cur.execute(show)

        valor = self.cur.fetchall()[0][0]

        if  valor == None:
            return 0

        #RETORNA O VALOR DO DIA
        return valor

    def getContabilidadeMes(self, data):

        show = f"SELECT sum(mao_de_obra) FROM ordem_servico WHERE saida LIKE '%{data}' and status='CONCLUIDO'"
        self.cur.execute(show)

        valor = self.cur.fetchall()[0][0]

        if  valor == None:
            return 0

        #RETORNA O VALOR DO MÊS
        return valor

    def getContabilidadeDinheiro(self):

        show = f"SELECT sum(mao_de_obra) FROM ordem_servico WHERE pagamento='DINHEIRO'"
        self.cur.execute(show)

        valor = self.cur.fetchall()[0][0]

        if  valor == None:
            return 0

        #RETORNA O VALOR DO MÊS
        return valor

    def getContabilidadeCartao(self):

        show = f"SELECT sum(mao_de_obra) FROM ordem_servico WHERE pagamento='CARTÃO'"
        self.cur.execute(show)

        valor = self.cur.fetchall()[0][0]

        if  valor == None:
            return 0

        #RETORNA O VALOR DO MÊS
        return valor

    def getContabilidadePix(self):

        show = f"SELECT sum(mao_de_obra) FROM ordem_servico WHERE pagamento='PIX'"
        self.cur.execute(show)

        valor = self.cur.fetchall()[0][0]

        if  valor == None:
            return 0

        #RETORNA O VALOR DO MÊS
        return valor

    # --- BACKUP ---
    def toJson(self):

        for os in self.getAllOS():
            pass
