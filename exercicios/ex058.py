#Desafio 058 -> Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

from random import randint
computador = randint(0, 10) #Gera o número eleatório
print('Acabei de pensar em um número entre 0 e 10....')
palpite = 0
acertou = False

while not acertou:
    jogador = int(input('Qual seu palpite?: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS... tente mais uma vez')
        elif jogador > computador:
                print('Tente mais uma vez')
print()
print(f'ACERTOU COM {palpite}')



