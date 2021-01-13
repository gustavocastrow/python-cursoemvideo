# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear() #Limpando os dados de cada jogar durante o loop.
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
    partidas.clear()

    for cont in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {cont}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy()) #Por ser um dicionario temos que usar ".copy()" não podemos utilizar "[:]"

    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas SIM ou NAO')
    if resp == 'N':
            break

print('-=' * 30)
#Cabeçalho
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)

for key, value in enumerate(time):
    print(f'{key:>4} ', end='')
    for d in value.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostra dados de qual jogar?: [999 sair] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Nao existe jogador com codigo da {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOT {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i} fez {g} gols')
