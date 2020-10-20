#Desafio 041 ->
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:

# – Até 9 anos: MIRIM
# –Até 14 anos: INFANTIL
# –Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

nascimento = int(input('Ano nascimento: '))
idade = 2020 - nascimento

if idade <= 9:
    print(f'Idade {idade} ==> MIRIM')
elif idade > 9 and idade <= 14:
    print(f'Idade {idade} ==> INFANTIL')
elif idade > 14 and idade <= 19:
    print(f'Idade {idade} ==> JUNIOR')
elif idade > 19 and idade <= 25:
    print(f'Idade {idade} ==> SENIOR')
else:
    print(f'Idade {idade} ==> MASTER')