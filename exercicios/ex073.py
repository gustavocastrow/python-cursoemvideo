#Desafio 73 -> Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

tabela = ('Corinthians', 'São Paulo', 'Santos', 'Palmeiras', 'Flamengo', 'Vasco', 'Fluminense', 'Botafogo', 'Cruzeiro',
          'Atlético-MG', 'Chapecoense', 'Grêmio', 'Inter', 'Fortaleza', 'Ceara')

# Os 5 primeiros.
print(f'Os 5 primeiros são {tabela[:5]}')

# Os ultimos 4 colocados
print(f'Os 4 ultimos são {tabela[-4:]}')

# Times em ordem alfabética.
print(f'Ordem alfabética dos times {sorted(tabela)}')

# Em que posição está o time da Chapecoense.
print(f'A Chapecoense esta em {tabela.index("Chapecoense")+1} posição')