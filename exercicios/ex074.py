#Desafio 74 -> Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11))

for numero in numeros:
    print(numero)


print(f'O maior numero gerado foi: {max(numeros)}')
print(f'O menor numero gerado foi: {min(numeros)}')

