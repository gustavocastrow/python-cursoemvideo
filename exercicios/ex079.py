# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

numeros = []

while True:
    numero = int(input('Informe um valor: '))

    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso na lista')
    else:
        print('Valor já consta na lista')

    resposta = str(input('Deseja inserir mais numeros?: [S/N]')).upper().strip()

    if resposta in 'N':
        break

print(f'A lista informada foi: {numeros}')
print(f'Ordem crescente: {sorted(numeros)}')

