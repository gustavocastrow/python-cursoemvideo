#Desafio 075 -> Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('N1: ')),
       int(input('N2: ')),
       int(input('N3: ')),
       int(input('N4: ')))
print(num)


# Quantas vezes apareceu o valor 9:
print(f'O valor 9 apareceu {num.count(9)}')

# Em que posição foi digitado o valor 3

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posicao')
else:
    print(f'O valor 3 nao foi digitado em nenhuma posicao.')


# Quais foram os numeros pares
for numero in num:
    if numero % 2 == 0:
        print(f'Os valores pares digitados foram {numero}')
