#Desafio 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.>

r1 = float(input('RETA 1: '))
r2 = float(input('RETA 1: '))
r3 = float(input('RETA 1: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo')
else:
    print('Não forma triangulo: ')