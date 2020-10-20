#Desafio 039 ->
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.

ano_nascimento = int(input('Ano nascimento: '))
sexo = str(input('Informe seu sexo: '))
idade = 2020 - ano_nascimento

if sexo == 'm':
    if idade == 18:
        print('Hora de se alistar')
    elif idade > 18:
        prazo = idade - 18
        print(f'Você passou do prazo em {prazo} anos.')
    else:
        print(f'Você tem {idade}, alistamento só com 18.')
else:
    print('Você é mulher, nao precisa se alistar')