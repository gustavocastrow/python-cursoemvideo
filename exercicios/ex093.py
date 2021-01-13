#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
#partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
#dicionário, incluindo o total de gols feitos durante o campeonato.


jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))

#Calculando o aproveitamento.
for cont in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {cont}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}')

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for index, value in enumerate(jogador['gols']):
    print(f'  => Na partida {index}, fez {value} gols')
print(f'Foi um total de {jogador["total"]} gols')






