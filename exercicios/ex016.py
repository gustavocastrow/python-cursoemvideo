#Desafio 016 -> Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um número: 6.124, o número 6.124 tem a parte inteira 6.
import math
numero = float(input('Informe um número real: '))
print(math.trunc(numero))