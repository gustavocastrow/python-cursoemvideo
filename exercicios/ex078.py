# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

lista = []
maior = 0
menor = 0

for numero in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posicao {numero}: ')))

    if numero == 0:
        maior = menor = lista[numero]
    else:
        if lista[numero] > maior:
            maior = lista[numero]
        if lista[numero] < menor:
            menor = lista[numero]

print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi: {maior}, na posicao ', end='')

for index, valor in enumerate(lista):
    if valor == maior:
        print(f'{index}')
print()
print(f'O menor valor digitado foi: {menor}, na posicao ', end='')
for index, valor in enumerate(lista):
    if valor == menor:
        print(f'{index}')

print('='*30)
print('Utilizando min() e max()')
print(f'Maior valor: {max(lista)}')
print(f'Menor valor: {min(lista)}')

