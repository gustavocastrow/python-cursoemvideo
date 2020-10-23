#Desafio 060 -> Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
from math import factorial

n1 = int(input('Digite um número para calcular seu fatorial'))

f = factorial(n1)
print(f'O fatorial de {n1} é {f}')


n = int(input('Digite um numero: '))
c = n
f = 1
while c > 0:
    print(f'{c}')
    print('x' if c > 1 else ' = ', end ='')
    f = f * c
    c -= 1
print(f)
