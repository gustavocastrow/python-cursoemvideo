#Desafio 042 ->
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

r1 = float(input('RETA 1: '))
r2 = float(input('RETA 1: '))
r3 = float(input('RETA 1: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo')
    if r1 == r2 == r3: #todos os lados iguais
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1: #todos lados diferents
        print('ESCALENO!')
    else:
        print('ISOSCELES')
else:
    print('Não forma triangulo: ')