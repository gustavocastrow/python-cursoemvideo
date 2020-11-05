#Desafio 81 -> Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Informe um numero: ')))
    resposta = str(input('Deseja continuar? [S/N]')).strip().upper()

    if resposta == 'N':
        break

print(f'A => Foram digitados {len(lista)} numeros.')

print(f'Os numeros digitados formaram a seguinte lista: {lista}')

lista.sort(reverse=True)
print(f'B => Lista de valores de forma decrescente: {lista}')

if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 nao faz parte da lista')