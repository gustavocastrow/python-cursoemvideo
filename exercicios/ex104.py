# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(valor):
    if valor.isnumeric():
        return print(f'Valor {valor} é numerico.')
    else:
        return print(f'Valor {valor} nao é numerico.')


saida = input('Informe um valor: ')
leiaInt(saida)