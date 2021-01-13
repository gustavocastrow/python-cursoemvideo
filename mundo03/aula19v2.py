estado = dict()
brasil = list()

for contador in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))

    brasil.append(estado.copy()) #Para exibir os dados corretor sem repeticao
print(brasil)

for estado in brasil:
    for key, value in estado.items():
        print(f'O campo {key} tem valor {value}')
