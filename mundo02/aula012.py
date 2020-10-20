nome = str(print('Qual seu nome: '))

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem normal')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminimo')
else:
    print('Seu nome é bem normal!')