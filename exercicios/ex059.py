#Desafio 059 -> Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('N1: '))
n2 = int(input('N2: '))
print('Qual operação você deseja fazer?')
opcao = 0

while opcao != 5:
    opcao = int(input(' [1] SOMAR \n [2] MULTIPLICAR \n [3] Maior \n [4] NOVOS NÚMEROS \n [5] SAIR. '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é: {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'A multi entre {n1} e {n2} é: {mult}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é  {n1}')
        elif n2 > n1:
            print(f'O maior número é: {n2}')
    elif opcao == 4:
        n1 = int(input('Informe os novos números: '))
        n2 = int(input('Informe os novos números: '))
    elif opcao == 5:
        print('Fim do programa!')
    else:
        print('Opção inválida!')

