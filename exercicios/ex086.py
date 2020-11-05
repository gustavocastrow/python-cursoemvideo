#Desafio 86 => Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[ ], [ ], [ ]]
for a in range(0, 3):
    for b in range(0, 3):
        matriz[a].append(int(input(f'Digite um valor para [{a}, {b}]: ')))
print('-='*30)
for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matriz[a][b]:^5}]', end='')
    print('')