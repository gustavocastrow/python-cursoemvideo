#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma DECRESCENTE.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    numero = int(input('Informe um numero: '))
    lista.append(numero)

    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()

    if resposta in 'N':
        break
print(f'A lista informada foi: {lista}')
print(f'(A): Foram digitados {len(lista)} numeros')

lista.sort(reverse=True)
print(f'(B): Lista ordenada em ordem DECRESCENTE: {lista}')

if 5 in lista:
    print(f'O valor 5 faz parte da lista {lista}')
else:
    print('O valor 5 nao faz parte da lista {lista}')