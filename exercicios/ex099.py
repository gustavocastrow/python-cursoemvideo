# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# Solucao mais curta: Utilizando a funcao "max()"

def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados...')

    for valor in num:
        print(f'{valor} ', end='')

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(2, 5, 34, 23, 532, 232)