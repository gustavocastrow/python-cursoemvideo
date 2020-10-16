#Desafio 011 -> Faça um programa que leia a LARGURA e ALTURA de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m2

altura = int(input('Altura: '))
largura = int(input('Largura: '))

m_quadrado = altura * largura
tinta = m_quadrado / 2

print(f'Para pintar {m_quadrado}m^2 será necessário {tinta:.2f}L')