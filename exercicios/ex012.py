#Desafio 012 -> Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com desconto de 5%

preco = float(input('Informe o valor do produto: R$ '))
desconto = preco * 0.05
preco_final = preco - desconto

print(f'Valor produto: R$ {preco:.2f}, \n Desconto: R$ {desconto:.2f}, \n Preço Final: R$ {preco_final:.2f}')