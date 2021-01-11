# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

tabela = ('Corinthians', 'São Paulo', 'Santos', 'Palmeiras', 'Flamengo', 'Vasco', 'Fluminense', 'Botafogo', 'Cruzeiro',
          'Atlético-MG', 'Chapecoense', 'Grêmio', 'Inter', 'Fortaleza', 'Ceara')

# Os 5 primeiros colocados
print(f'Os 5 primeiros colocados sao: {tabela[:5]}')

# Os 4 ultimos colocados
print(f'Os 4 ultimos colocados sao: {tabela[-4:]}')

# Times em ordem alfabética
print(f'Ordem alfabética: {sorted(tabela)}')

# Em que posição está o time da Chapecoense?
print(f'A chapecoense esta na posicao: {tabela.index("Chapecoense")+1}')
