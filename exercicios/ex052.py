#Desafio 052 -> Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Informe um número: '))
contador = 0
for c in range(1, num+1):
    if num % c == 0:
        contador = contador + 1
print(f'O número {num} é divisivel {contador} vezes')

if contador == 2:
    print(f'O número {num} é primo, pois ele é divisivel apenas {contador} vezes')
else:
    print(f'O número {num} não é primo, pois ele é divisivel {contador} vezes')