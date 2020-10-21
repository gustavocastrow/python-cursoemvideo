#Desafio 056 -> Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
media_idade = 0
maior_homem = 0
nome_velho = ''
totmulher20 = 0
for pessoa in range (1,5):
    print(f'------- {pessoa} PESSOA --------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip()

    if pessoa == 1 and sexo in 'Mm':
        maior_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_homem:
        maior_homem = idade
        nome_velho = nome
    soma_idade += idade
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1


media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade:.2f}.')
print(f'O homem mais velho tem {maior_homem} e se chama {nome_velho}')
print(f'Ao todo são {totmulher20} com menos de 20 anos.')
