# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f'O terreno tem uma areal total de: {area_terreno}m')

larg = float(input('LARGURA (M): '))
comp = float(input('COMPRIMENTO (M): '))

area(larg, comp)