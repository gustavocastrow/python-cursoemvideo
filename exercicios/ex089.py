# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada
# aluno individualmente.

lista_notas = []

while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    lista_notas.append([nome, [nota1, nota2], media])
    resposta = str(input('Deseja continuar? ')).strip().upper()

    if resposta in 'N':
        break

for index, aluno in enumerate(lista_notas):
        print(f'{index:<4}{aluno[0]:<10}{aluno[2]:<8.1f}')

while True:
    print('=>' * 30)
    opc = int(input('Mostrar notas de qual aluno?: (999 = Sair) '))

    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(lista_notas) -1:
        print(f'Notas de {lista_notas[opc][0]} sao {lista_notas[opc][1]}')
