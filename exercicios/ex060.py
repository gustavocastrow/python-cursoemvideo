#Desafio 060 -> Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

from math import factorial
print('Utilizando a biblioteca math + factorial')
n1 = int(input('Digite um número para calcular seu fatorial'))

f = factorial(n1)
print(f'O fatorial de {n1} é {f} ')

print('=================================')

print('Fazendo na mão')

numero = int(input('Digite um numero: '))
contador = numero
fatorial = 1
while contador > 0:
    print(f'{contador}')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= fatorial
    contador -= 1
print(fatorial)
