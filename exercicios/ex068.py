#Desafio 68 -> Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
# perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:
    jogador = int(input('Informe um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
       tipo = str(input('Par ou Impar')).strip().upper()[0]
    print(f'Você jogou: {jogador} e o computador jogou {computador}. Total de {total}')
    print(f'Deu par' if total % 2 == 0 else 'Deu impar.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Voce perdeu')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente?')
print(f'Você venceu {v} vezes.')
