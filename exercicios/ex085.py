#Desafio 85 => Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num = [[], []]

for numero in range(1, 8):
    valor = int(input(f'Informe o {numero}o: '))

    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 == 1:
        num[1].append(valor)

print(f'Os valores sao: {num}')
print(f'Valores PARES em ordem: {sorted(num[0])}')
print(f'Valores IMPARES em ordem: {sorted(num[1])}')
