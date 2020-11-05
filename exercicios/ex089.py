#Desafio 89 => Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Deseja continuar?: ')).strip().upper()

    if resposta == 'N':
        break


print('=>' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')

for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:<8.1f}')

while True:
    print('=>' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 Interrompe): '))

    if opc == 999:
        print('Finalizando....')
        break

    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('Obrigado....')