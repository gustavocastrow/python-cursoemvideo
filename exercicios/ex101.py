# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import datetime

data_atual = datetime.now().year

def voto(ano_nascimento):
        idade = data_atual - ano_nascimento

        if idade >= 18 and idade <= 65:
            return print(f'Voce possui {idade} anos, portanto o voto é OBRIGATORIO.')
        elif idade >= 16 or idade > 65:
            return print(f'Voce possui {idade} anos, portanto o voto é OPCIONAL')
        else:
            return print(f'Voce possui {idade} anos, portanto o voto é NEGADO')


ano = int(input('Informe seu ano de nascimento '))
voto(ano)