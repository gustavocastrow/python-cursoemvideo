# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas'
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima
pessoa = dict()
galera = list()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor informe um sexo valido!')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if resp == 'N':
        break


print(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')

media = soma /len(galera)
print(f'A media de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print(f'Lista das pessoas que estao acima da media: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')