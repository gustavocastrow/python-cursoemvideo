#Desafio 056 -> Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
mulheres = 0

for pessoa in range(1, 5):
    print(f'<------ {pessoa}° Pessoa ------> ')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade

    if pessoa == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome

    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo == 'F' and idade < 20:
        mulheres = mulheres + 1


mediaidade = somaidade /4

print(f'O homem mais velho se chama {nomevelho} e tem  {maioridadehomem} anos.')
print(f'A média de idade do grupo é {mediaidade} anos.')
print(f'Existe  {mulheres} mulheres no grupo com menos de 20 anos..')




