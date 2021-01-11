#Aprimore o desafio anterior, mostrando no final:
#A-> A soma de todos os valores pares digitados
#B-> A soma dos valores da terceira coluna
#C-> O maior valor da segunda linha

matriz = [[ ], [ ], [ ]]
spar = maior = scol = 0

#Preenchendo a matriz:
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))
print('-='*30)

#Mostrando a Matriz na tela
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha] [coluna]}]', end='')
        #Somando os numeros par
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print('')
    print('='*30)


#A -> Mostrando a soma de todos os valores digitados
print(f'A-> A soma dos valores pares é {spar}')

#B -> A soma dos valores da terceira coluna ([X], [2]) Coluna sempre fixa e Linha sempre variavel
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'B-> A soma dos valores da terceira coluna é: {scol}')

#C -> O maior valor da segunda linha, LINHA fixa COLUNA variavel
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'C-> O maior valor da segunda linha é: {maior} ')

