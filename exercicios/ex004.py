#Desafio 004 -> Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possiveis sobre ele.

leitura_teclado = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(leitura_teclado))
print('So tem espaços?', leitura_teclado.isspace())
print('E um numero?', leitura_teclado.isnumeric())
print('E alfabetico?', leitura_teclado.isalpha())
print('É numerico?', leitura_teclado.isalnum())
print('Está em maisculas?', leitura_teclado.isupper())
print('Está em minusculas?',leitura_teclado.islower())