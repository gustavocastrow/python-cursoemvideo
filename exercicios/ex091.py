#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
# em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
# número no dado.

from random import randint
from operator import itemgetter

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

ranking = list()

for key, value in jogo.items():
    print(f'O jogador {key} tirou o numero: {value}')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
#ITEMGETTER ordena os elementos, 1 para pegar o valor do randint.

#Tratando o resultado para lista
for index, value in enumerate(ranking):
    print(f'{index+1} lugar: {value[0]} com {value[1]}')



