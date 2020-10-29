#Desafio 069 -> Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
# deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.
contador_idade = 0
contador_homem = 0
contador_mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

    if idade >= 18:
        contador_idade += 1

    if sexo == 'M':
        contador_homem += 1

    if idade < 20 and sexo == 'F':
        contador_mulher += 1
print(f'Pessoas com mais de 18 anos {contador_idade}')
print(f'Homens cadastrados: {contador_homem}')
print(f'Mulheres abaixo dos 20: {contador_mulher}')



