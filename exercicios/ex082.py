#Desafio 82 => Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
# extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
# mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []
while True:
    num = int(input('Informe um numero: '))
    lista.append(num)
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()

    if resposta == 'N':
        break

    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(f'Lista total: {lista}')
print(f'Lista pares: {lista_par}')
print(f'Lista impares: {lista_impar}')