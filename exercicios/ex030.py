#Desafio 030 -> Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número: '))
resultado = numero % 2 # numero resto da divisão por 2
# numero par = 0 -> o resto da divisão de qualquer número par por 2 é 0
# numero impar = 1 -> o resto da divisão de qualquer número impar por 2 é 1
if resultado == 0:
    print(f'O numero {numero} é par!')
else:
    print(f'O numero {numero} é impar! ')