#Desafio 015 ->  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de
# dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorridos = int(input('Informe os kms percorridos: '))
dias = int(input('Informe o número de dias que ficou com o carro: '))
valor = (dias * 60) + (km_percorridos * 0.15)

print(f'Voce rodou {km_percorridos}km em {dias} dias, preco final R$ {valor}')