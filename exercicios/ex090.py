# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.

aluno = dict()

#Pegando os inputs e ja colocando no dict

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['status'] = 'Aprovado!'
elif 5 <= aluno['media'] < 7:
    aluno['status'] = 'Recuperacao'
else:
    aluno['status'] = 'Reprovado!'

for key, value in aluno.items():
    print(f'{key} é igual a {value}')


#print(f'O aluno {aluno["nome"]} teve a media de {aluno["media"]} portando ele esta {aluno["status"]}')