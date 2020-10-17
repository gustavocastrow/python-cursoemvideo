#Desafio 019 -> Um professor quer sortear um dos seus quatro alunos para apagar o quadro, Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome escolhido
import random
aluno1 = str(input('Aluno 01: '))
aluno2 = str(input('Aluno 02: '))
aluno3 = str(input('Aluno 03: '))
aluno4 = str(input('Aluno 04: '))

sorteio = [aluno1, aluno2, aluno3, aluno4]
print(random.choice(sorteio))