#Desafio 84 => Faca um programa que leia nome e peso de varias pessoas guardando tudo em uma lista, no final mostre:
# A => Quantas pessoas foram cadastradas
# B => Uma listagem com as pessoas mais pesadas
# C => Uma listagem com as pessoas mais leves.

pessoas = []
lista_pessoas = []
pessoas_leves = []
pessoas_pesadas = []
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    resp = str(input('Deseja continuar?: [S/N] ')).upper()
    lista_pessoas.append(pessoas[:])
    pessoas.clear()

    if resp == 'N':
        break

for pessoa in lista_pessoas:
    if pessoa[1] < 75: # Pessoas consideradas leves: ABAIXO DE 75KG.
        pessoas_leves.append(pessoa[0])
    elif pessoa[1] > 100: # Pessoas consideradas pesadas: ACIMA DE 100KG.
        pessoas_pesadas.append(pessoa[0])

print(f'A => Total pessoas cadastradas: {len(lista_pessoas)}')
print(f'B => Listagem pessoas mais pesadas, acima de 100kg {pessoas_pesadas}')
print(f'C => Listagem pessoas mais leves, abaixo de 75kg {pessoas_leves}')



