estado = dict() #{}
brasil = list() #[]

for contador in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa'))
    estado['sigla'] = str(input('Sigla do Estado'))

    brasil.append(estado.copy())

for estado in brasil: #FOR DA LISTA
    for key, value in estado.items():
        print(f'O campo {key} tem valor {value}')
