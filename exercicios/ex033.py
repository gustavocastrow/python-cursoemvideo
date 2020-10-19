#Desafio 033 -> Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))

#Verificando MENOR:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Verificando MAIOR:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')