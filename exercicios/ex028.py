#Desafio 028 -> Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o
# usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.

from random import randint
computador = randint(0,5) #Gera o número eleatório

print('Vou pensar em um número entre 0 e 5... tente adivinhar')
jogador = int(input('Em qual número voce pensou...? '))

if jogador == computador:
    print('Parabés voce acertou!')
else:
    print(f'Ganhei! eu pensei no número {computador} e não no {jogador}')
