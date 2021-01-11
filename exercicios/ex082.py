#Desafio 82 => Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
# extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
# mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []

while True:
    numero = int(input('Informe um numero: '))
    lista.append(numero)

    resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    if resposta in 'N':
        break

for index, valor in enumerate(numero):
    if valor % 2 == 0:
        lista_par.append(valor)
    elif valor % 2 == 1:
        lista_impar.append(valor)

print(f'A lista informada foi: {lista}')
print(f'A lista PAR: {lista_par}')
print(f'A lista IMPAR: {lista_impar}')




