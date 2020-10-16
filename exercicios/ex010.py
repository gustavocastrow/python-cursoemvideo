#Desafio 010 -> Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar
# considere -> U$$ 1,00 = R$ 3,27

dinheiro = float(input('Informe quantos R$ voce tem: '))
conversao = dinheiro / 3.27

print(f'R$ {dinheiro} da para comprar U$ {conversao:.2f}')