#Desafio 027 -> Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
# nome separadamente.

n = str(input('Informe seu nome completo: ')).strip()
nome = n.split()


print(f'Primeiro nome: {nome[0]}')
print(f'Ultimo nome: {nome[len(nome)-1]}')