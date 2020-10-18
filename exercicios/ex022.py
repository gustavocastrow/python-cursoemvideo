#Desafio 022 -> Crie um programa que leia o nome completo de uma pessoa e mostre
# -> O nome com todas as letras maiúsculas
# -> O nome com todas as letras minúsculas
# -> Quantas letras tem ao todo sem considerar os espaços
# -> Quantas letras tem o primeiro nome.

nome = str(input('Informe seu nome completo: ')).strip() # -> já elimina os espaços antes e depois
print(f'Seu nome em maiusculo é {nome.upper()}')
print(f'Seu nome em minusculos é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")}')
