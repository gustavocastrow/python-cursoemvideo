#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

num = (int(input('Numero 01: ')), int(input('Numero 02: ')), int(input('Numero 03: ')), int(input('Numero 04: ')))

print(num)

#Quantas vezes apareceu o valor 9?
print(f'O valor 9 apareceu {num.count(9)}')

#Em que posicao foi digitado o valor 3?
if 3 in num:
    print(f'O valor 3 apareceu na posicao {num.index(3)+1}')
else:
    print('O valor 3 nao foi digitado')