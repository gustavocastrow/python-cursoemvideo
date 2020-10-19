#Desafio 029 -> Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade_carro = int(input('Informe a velocidade do carro:  km/h'))

if velocidade_carro > 80:
    multa = (velocidade_carro - 80) * 7
    print(f'Voce ultrapassou à {velocidade_carro}, por tanto foi multado em R$ {multa}')
else:
    print('Dentro da velocidade, boa viagem!')