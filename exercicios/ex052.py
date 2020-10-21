#Desafio 052 -> Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um numero: '))

for c in range(1, num + 1):
    if num % c == 0:
        print(f'O numero {num} e divisivel por {c} ')
