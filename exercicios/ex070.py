#Desafio 070 -> Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
# vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total_gasto = 0
mais_mil = 0
menor_preco = 0
contador = 0
barato = ' '

while True:
    nome = str(input('Informe o nome do produto: '))
    preco = int(input('Informe o preço do produto: '))
    total_gasto += preco
    contador += 1
    resposta = ' '

    if preco > 1000:
        mais_mil += 1

    if contador == 1:
        menor_preco = preco
        barato = nome
    else:
        if preco < menor_preco:
            menor_preco = preco
            barato = nome

    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'Total gasto: R$ {total_gasto:.2f}')
print(f'Total produtos acima de R$ 1.000: {mais_mil}')
print(f'O produto mais barato foi {barato} e custa: {menor_preco:.2f}')