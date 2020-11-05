#Desafio 88 => Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
lista = []
jogos = []
print('--'*30)
print('          JOGA NA MEGA SENA           ')
print('--'*30)
quant = int(input('Quantos jogos voce quer sortear?: '))
total = 1

while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'Os numeros sorteados foram... {jogos}')
