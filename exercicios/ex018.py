#Desafio 018 -> Faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente
import math
angulo = float(input('Informe o valor do angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'SENO: {seno:.2f} \nCOSSENO: {cosseno:.2f} \nTANGENTE: {tangente:.2f}')