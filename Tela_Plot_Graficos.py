from pylab import *
from Persistencia import bd
from numpy import arange
from matplotlib.pyplot import * 

class plotGraphs:
    
    def __init__(self):
        #OBJETO DE BANCO DE DADOS
        self.bancoDados = bd()

    def gerarGraficoFinanceiro(self, receita, manutencao, gastos, lucro):
        pos = arange(4) + .5

        valores = (receita, manutencao, gastos, lucro)
        topicos = ('RECEITA', 'MANUT.', 'GASTOS', 'LUCRO')

        #GERAR GRAFICO
        barh(pos, valores, align='center', color='DarkMagenta')
        yticks(pos, topicos)

        #INFORMAÇÕES
        title('VISÃO DE NEGÓCIO')
        xlabel('Valor em R$')
        ylabel('Metricas')

        #LINHAS CORTANDO O GRÁFICOs
        grid(True)

        #EXIBIR GRAFICO
        show()

    def gerarGraficosReceitaMeses(self, receitas):
        pos = arange(12) + .5

        valores = tuple(receitas)
        topicos = tuple(self.bancoDados.months.__reversed__())

        #GERAR GRAFICO
        barh(pos, valores, align='center', color='DarkMagenta')
        yticks(pos, topicos)

        #INFORMAÇÕES
        title('RECEITA DE TODOS OS MESES')
        xlabel('Valor em R$')
        ylabel('Meses')

        #LINHAS CORTANDO O GRÁFICO
        grid(True)

        #EXIBIR GRAFICO
        show()

    def generateGraphYear(self, ano, mao_obra, pecas, outros):
        
        #DADOS DA AMOSTRAGEM
        months = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
        
        barWidth = 0.30
        matplotlib.pyplot.figure(figsize=(10,5))

        #POSICAO DAS BARRAS
        r1 = np.arange(len(mao_obra))
        r2 = [(x + barWidth) for x in r1]
        r3 = [(x + barWidth) for x in r2]

        #CRIANDO BARRAS
        matplotlib.pyplot.bar(r1, mao_obra, color='#00864B', width=barWidth, label='MÃO DE OBRA')
        matplotlib.pyplot.bar(r2, pecas, color='#CBBE00', width=barWidth, label='VENDA DE PEÇAS')
        matplotlib.pyplot.bar(r3, outros, color='#A3218E', width=barWidth, label='OUTROS')
        
        #ADICIONANDO LEGENDAS AS BARRAS
        matplotlib.pyplot.xlabel('MESES')
        matplotlib.pyplot.xticks([r + barWidth for r in range(len(mao_obra))], months)
        matplotlib.pyplot.ylabel('VALOR R$')

        matplotlib.pyplot.title(f'GRÁFICO DA RECEITA DO ANO DE {ano}')

        #CRIANDO E EXIBINDO O GRAFICO
        matplotlib.pyplot.legend()
        matplotlib.pyplot.show()

#plotGraphs().generateGraphYear([0, 0, 0, 60.0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 20.0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 10.0, 0, 0, 0, 0, 0, 0, 0, 0])
