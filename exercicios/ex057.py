#Desafio 057 -> Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.
sexo = str(input('Inform seu sexo: [M/F] ')).strip().upper()[0]
# Tira os espaços, joga para o maisculo, e pega só a primeira letra

while sexo not in 'MmFf':
    sexo = str(input('Dados inválido, pfvr informe seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')

