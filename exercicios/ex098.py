# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# A -> de 1 ate 10, de 1 em 1
# B -> de 10 ate 0, de 2 em 2
# C -> Contagem personalizada
from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} em {passo}')

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += passo
        print('Fim!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)

print('Sua contagem: ')
ini = int(input('Inicio: '))
end = int(input('Fim: '))
pas = int(input('Passo: '))

contador(ini, end, pas)



