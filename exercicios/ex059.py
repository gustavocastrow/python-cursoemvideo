#Desafio 059 -> Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0

while opcao != 5:
    print('''   [1] - Somar
        [2] - Multiplicar
        [3] - Maior
        [4] - Novos números
        [5] - Sair do programa''')
    opcao = int(input('Qual é a sua opção?'))
    if opcao == 1:
        soma = n1 + n1
        print(f'A opção selecionada foi {opcao}, portanto {n1} + {n2} = {soma}')

    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'A opção selecionada foi {opcao}, portanto {n1} x {n2} = {soma}')

    elif opcao == 3:
        if n1 > n2:
            print(f'A opção selecionada foi {opcao}, portanto {n1} é maior que {n2} ')
        else:
            print(f'A opção selecionada foi {opcao}, portanto {n2} é maior que {n1} ')
    elif opcao == 4:
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Primeiro Valor: '))

    elif opcao == 5:
        print('Fim do programa! Volte sempre!')
    else:
        print('Opção inválida, tente novamente!')

