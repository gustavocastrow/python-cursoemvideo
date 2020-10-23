#Desafio 054 ->  Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
contador_maior = 0
contador_menor = 0

for pessoa in range(1, 8):
    ano_nascimento = int(input(f'Informe o ano que nasceu a {pessoa} ° pessoa: '))
    if atual - ano_nascimento < 18:
        contador_menor = contador_menor + 1
    else:
        contador_maior = contador_maior + 1

print(f'Existem {contador_menor} menores de idade')
print(f'Existem {contador_maior} maiores de idade')