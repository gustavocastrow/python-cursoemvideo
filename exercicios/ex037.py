#Desafio 037 ->
#  Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
#  conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Informe um número inteiro qualquer: '))
print('''Informe uma base para conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{numero} convertido para binario: {bin(numero)}')
elif opcao == 2:
    print(f'{numero} convertido para octal: {oct(numero)}')
elif opcao == 3:
    print(f'{numero} convertido para hexadecimal: {hex(numero)}')
else:
    print(f'{numero} inválido, informe um número de 1 a 3')