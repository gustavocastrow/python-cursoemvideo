#Desafio 045 -> Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior_peso = 0
menor_peso = 0

for pessoa in range(1, 6):
    peso = float(input('Informe seu peso: '))

    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'Maior peso: {maior_peso:.2f} KG')
print(f'Menor peso: {menor_peso:.2f} KG ')
