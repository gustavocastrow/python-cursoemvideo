#Desafio 017 -> Faça um programa que leia o comprimento to cateto oposto e do cateto adjacente de um triangulo retangulo
# calcule e mostre o comprimento da hipotenusa
import math

cateto_oposto = float(input('Informe o cateto oposto: '))
cateto_adjacente = float(input('Informe o cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa é: {hipotenusa:.2f}')