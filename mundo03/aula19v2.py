pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}

print(f'O {pessoas["nome"]} do sexo {pessoas["sexo"]} tem {pessoas["idade"]} anos')

print('Key')
for key in pessoas.keys():
    print(key)

print('Value')
for value in pessoas.values():
    print(value)

print('Items (key and value')
for key, value in pessoas.items():
    print(f'{key} = {value}')


print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())


print('==================================================================================')

brasil = []
estado1 = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ'
}

estado2 = {
    'uf': 'Sao Paulo',
    'sigla': 'SP'
}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)