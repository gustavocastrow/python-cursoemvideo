#Desafio 032 -> Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# Se resto da divisão por 4 for 0 = bissexto

ano = int(input('informe o ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')