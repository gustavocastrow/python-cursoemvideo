#Desafio 079 -> Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

numeros = list()

while True:
    numero = int(input('Informe um valor: '))
    if numero not in numeros: #Verifica se o numero digitado ja esta contido na List
        numeros.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado!')

    resposta = str((input('Deseja continuar?: [S/N] '))).upper().strip()

    if resposta in 'N': #Verifica se a resposta de continuar e SIM ou NAO.
        break
print(f'Voce informou a lista: {numeros}')
print(f'List ordenada: {sorted(numeros)}')

