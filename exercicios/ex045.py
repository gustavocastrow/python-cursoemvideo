#Desafio 045 -> Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções 
[0] -> PEDRA
[1] -> PAPEL
[2] -> TESOURA''')
jogador = int(input('Qual sua jogada?'))
print(f'Computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')

if computador == 0: #PEDRA
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #PAPEL
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #TESOURA
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
else:
    print('JOGADA INVÁLIDA')