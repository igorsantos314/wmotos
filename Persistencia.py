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

    def insertVendaProduto(self, list_produtos):

        #SETA O ID
        id = self.getIdVenda()

        for p in list_produtos:
            lucro = self.getLucroId(p[0]) * int(p[3])

            #INSERIR DADOS NA TABELA VENDER PRODUTO
            command = f'INSERT INTO vender_produtos(id_venda, id_produto, nome_produto, subtotal, quantidade, lucro) VALUES({id}, {p[0]}, "{p[1]}", {p[2]}, {p[3]}, {lucro})'

            self.cur.execute(command)
            self.conection.commit()

    def delOS(self, id):
        #DELETAR OS
        command = f'DELETE FROM ordem_servico WHERE id={id}'
        
        self.cur.execute(command)
        self.conection.commit()

    def delProduto(self, id):
        #DELETAR OS
        command = f'DELETE FROM produto WHERE id={id}'
        
        self.cur.execute(command)
        self.conection.commit()

    def updateOS(self, id, data_entrada, saida, nome_cliente, telefone, veiculo, desc, laudo_tecnico, forma_pagamento, status, valor_mao_obra, valor_pecas, valor_outros):
        #ATUALIZAR OS
        command = f"UPDATE ordem_servico SET entrada='{data_entrada}', saida='{saida}', cliente='{nome_cliente}', telefone='{telefone}', veiculo='{veiculo}', descricao='{desc}', laudo='{laudo_tecnico}', pagamento='{forma_pagamento}', status='{status}', mao_de_obra={valor_mao_obra}, valor_de_pecas={valor_pecas}, valor_outros={valor_outros} WHERE id={id};"

        self.cur.execute(command)
        self.conection.commit()

    def updateProduto(self, id, nome, valor_compra, valor_venda):
        #ATUALIZAR OS
        command = f"UPDATE produto SET nome='{nome}', valor_compra={valor_compra}, valor_venda={valor_venda} WHERE id={id};"

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
    
    def getIdVenda(self):
        show = "SELECT * FROM vender_produtos"

        self.cur.execute(show)

        #RETORNA LISTA DE OS
        prod = self.cur.fetchall()

        if len(prod) == 0:
            return 0
        else:
            #PEGA O ULTIMO ID DE VENDA E SOMA 1
            return prod[-1][0]+1

    def getVendaId(self, id):
        show = f"SELECT * FROM vender_produtos WHERE id_venda={id}"
        self.cur.execute(show)

        venda = self.cur.fetchall()

        if len(venda) == 0:
            return None
        
        #RETORNA A TUPLA COM OS DADOS DA VENDA
        return venda

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

    def getNomeProduto(self, str):
        show = f"SELECT * FROM produto WHERE nome LIKE '%{str}%'"
        self.cur.execute(show)
        
        #RETORNA LISTA DE OS
        return self.cur.fetchall()

    def getProdutoId(self, id):
        show = f"SELECT * FROM produto WHERE id={id}"
        self.cur.execute(show)
        
        #RETORNA O PRODUTO
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

    def getReceitaMaoObra(self, ano):

        listReceita = []

        #VARRER TODOS OS MESES
        for mes in range(1, 13):
            
            #PEGAR O VALOR DE MAO DE OBRA DE CADA MES
            show = f"SELECT sum(mao_de_obra) from ordem_servico WHERE saida like '%/{mes}/{ano}'"

            self.cur.execute(show)
            service = self.cur.fetchall()

            if service[0][0] != None:
                listReceita.append(service[0][0])
            else:
                listReceita.append(0)

        return listReceita

    def getReceitaPecas(self, ano):

        listReceita = []

        #VARRER TODOS OS MESES
        for mes in range(1, 13):
            
            #PEGAR O VALOR DE PECAS DE CADA MES
            show = f"SELECT sum(valor_de_pecas) from ordem_servico WHERE saida like '%/{mes}/{ano}'"

            self.cur.execute(show)
            pecas = self.cur.fetchall()
            
            if pecas[0][0] != None:
                listReceita.append(pecas[0][0])
            else:
                listReceita.append(0)

        return listReceita

    def getReceitaOutros(self, ano):

        listReceita = []

        #VARRER TODOS OS MESES
        for mes in range(1, 13):
            
            #PEGAR O VALOR DE OUTROS DE CADA MES
            show = f"SELECT sum(valor_outros) from ordem_servico WHERE saida like '%/{mes}/{ano}'"

            self.cur.execute(show)
            outros = self.cur.fetchall()
            
            if outros[0][0] != None:
                listReceita.append(outros[0][0])
            else:
                listReceita.append(0)

        return listReceita

    def getLucroProd(self):
        show = f"SELECT sum(lucro) FROM vender_produtos"
        self.cur.execute(show)
        
        return self.cur.fetchall()[0][0]

    def getReceitaProd(self):
        show = f"SELECT sum(subtotal*quantidade) FROM vender_produtos"
        self.cur.execute(show)

        return self.cur.fetchall()[0][0]

    def getLucroId(self, id):
        show = f"SELECT valor_venda-valor_compra FROM produto WHERE id={id}"
        self.cur.execute(show)

        return self.cur.fetchall()[0][0]

#print(bd().getReceitaProd())
#print(bd().getLucroProd())
"""print(bd().getReceitaMaoObra(2021))
print(bd().getReceitaPecas(2021))
print(bd().getReceitaOutros(2021))"""