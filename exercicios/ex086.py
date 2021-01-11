# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#FOR 01: Alimentacao dos dados
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Informe um valor [{linha}, {coluna}]: '))
print('===' * 30)

#FOR 02: Formatacao dos dados
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha] [coluna]}]', end='')
    print()


