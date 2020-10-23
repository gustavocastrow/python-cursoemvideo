#Desafio 051 -> Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.

primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão da PA: '))

#Calculando o décimo termo
decimo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo + razao, razao):
    print(f'{c}', end='->')
