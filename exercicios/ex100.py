# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(lista):
    print('Sorteando 5 valores para a lista...')
    for cont in range(0, 5):
        n = randint(1, 20)
        lista.append(n)
        print(f'{n} ', end='')
    print('Pronto, sorteio finalizado!')

def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somandos os valores PARES da lista {lista}, obtemos o resultado de: {soma}')

lista_vazia = list() #Precisamos de uma lista declarada para ser passada como parametro nas funcoes, caso contrario dara erro.
teste_lista = list()
sorteia(lista_vazia)
soma_par(lista_vazia)

sorteia(teste_lista)
soma_par(teste_lista)
