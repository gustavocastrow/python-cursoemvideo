#Aula 19: Dicionarios (Variaveis compostas)
#Dicionarios tem a possibilidade de ter indices literais
#Tupla()
#Listas[]
#Dicionarios{}

dados = dict()
dados = {
    'nome': 'Pedro',
    'idade': 25
}

print(dados['nome'])
print(dados['idade'])


#No dicionario "append" nao funciona
dados['sexo'] = 'M'
print(dados)

#Remover elementos
del dados['idade']
print(dados)

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(filme.values()) # Star Wars, 1977, George Lucas
print(filme.keys())   # Titulo, Ano, Diretor
print(filme.items())  # Titulo, Star Wars, Ano, 1977, Diretor, George Lucas

for key, value in filme.items():
    print(f'O {key} é {value}')

pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 25
}
pessoas['peso'] = 86.5
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())

for key, value in pessoas.items():
    print(f'Key: {key}, Value:{value}')

#Dicionario dentro de uma lista

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
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

