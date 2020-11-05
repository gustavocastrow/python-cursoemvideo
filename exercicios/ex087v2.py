matriz = [[ ], [ ], [ ]]

#Preenchendo a Matriz...
soma_par = maior = soma_colunas = 0
for linha in range(0,3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'Informe um valor para [{linha}, {coluna}] ')))
print(matriz)

#Formantando e mostrando a Matriz em tela.
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end='')
        #Verificando se o numero da matriz e par e fazendo a soma dos mesmos
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
    print('')

#Mostrando todos os numeros PARES:
print(f'Soma dos valores pares: {soma_par}')

#Soma dos valores da terceira coluna => [x, 2], [x, 2], [x, 2]
#Coluna FIXA // Linha VARIAVEL

for linha in range(0, 3):
    soma_colunas += matriz[linha][2]
print(f'A soma dos valores da terceira coluna: {soma_colunas}')

#O maior valor da segunda linha
#Coluna VARIAVEL // Linha FIXA

for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da SEGUNDO LINHA foi: {maior}')
