#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('CPTS: '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano contratacao: '))
    dados['salario'] = float(input('Salario: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

print(dados)

for key, value in dados.items():
    print(f'{key} tem o valor {value}')