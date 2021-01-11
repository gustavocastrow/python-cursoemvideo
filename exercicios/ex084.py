#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A-> Quantas pessoas foram cadastradas
#B-> Uma listagem com as pessoas mais pesadas
#C-> Uma listagem com as pessoas mais leves.

pessoas = list()
dados_pessoas = list()

pessoas_pesadas = list()
pessoas_leves = list()

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))

    dados_pessoas.append(pessoas[:])
    pessoas.clear()

    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()

    if resp in 'N':
        break

for pessoa in dados_pessoas:
    if pessoa[1] > 60:
        pessoas_pesadas.append(pessoa[0])
    elif pessoa[1] < 60:
        pessoas_leves.append(pessoa[0])

print(f'A: Pessoas cadastradas: {len(dados_pessoas)}')
print(f'B: Pessoas pesadas (>60KG): {pessoas_pesadas}')
print(f'C: Pessoas leves: (<60KG): {pessoas_leves}')

