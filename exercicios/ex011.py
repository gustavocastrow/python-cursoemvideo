#Desafio 011 -> Faça um programa que leia a LARGURA e ALTURA de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m2

altura = float(input('Altura: '))
largura = float(input('Largura: '))

area = altura * largura
tinta = area / 2

print(f'Para pintar {area}m^2 será necessário {tinta:.2f}L')