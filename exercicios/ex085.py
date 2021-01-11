#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = list()

lista_pares = list()
lista_impares = list()

for numero in range(0, 7):
    valor = int(input(f'Informe um valor para a posicao {numero}: '))
    lista.append(valor)

    if valor % 2 == 0:
        lista_pares.append(valor)
    elif valor % 2 == 1:
        lista_impares.append(valor)
print(f'Lista digitada: {lista}')
print(f'Lista PARES: {sorted(lista_pares)}')
print(f'Lista IMPARES: {sorted(lista_impares)}')




