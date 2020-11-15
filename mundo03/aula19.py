#Aula 19 => Dictio
#Append -> adicione um elemento a lista
#Estrutura de dados semelhantes a list e tuplas, porem com indices literais
#Tuplas ()
#Listas []
#Dic {}

dados = {
    'nome': 'Pedro',
    'idade': 24
}

#Indice nome e indice idade

print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'M'
print(dados)

del dados['idade']
print(dados)

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(filme)
print(filme.values()) #Retorna o valor do objeto (Star Wars, 1977, George Lucas)
print(filme.keys()) #Retona as chaves do objeto (Titulo, Ano, Diretor)
print(filme.items()) #Retorna valor do objeto e keys

for key, value in filme.items():
    print(f'O {key} é {value}')


locadora = [
    {#0
        'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
    },
    {#1
        'titulo': 'Avengers',
        'ano': 2012,
        'diretor': 'Jass Whedon'
    },
    {#2
        'titulo': 'Matrix',
        'ano': 1999,
        'diretor': 'Wachowski'
    }
]

print(locadora[0]['ano'])


