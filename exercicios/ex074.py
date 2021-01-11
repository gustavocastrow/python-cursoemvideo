# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11))

print(numeros)
print(f'Maior valor da tupla: {max(numeros)}')
print(f'Menor valor da tupla: {min(numeros)}')