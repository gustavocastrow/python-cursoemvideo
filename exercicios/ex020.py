#Desafio 020 ->  O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

aluno1 = str(input('Aluno 01: '))
aluno2 = str(input('Aluno 02: '))
aluno3 = str(input('Aluno 03: '))
aluno4 = str(input('Aluno 04: '))

array_alunos = [aluno4, aluno3, aluno2, aluno1]
random.shuffle(array_alunos)
print(array_alunos)
# Embaralhar os alunos