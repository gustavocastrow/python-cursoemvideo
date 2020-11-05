#Desafio 84v2: Correcao do prof Guanabara
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        maior = menor = temp[1] #Temp[0] = Nome // Temp[1] = Peso
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:]) #Copia temp - princ
    temp.clear()
    resp = str(input('Continuar? [S/N] '))

    if resp in 'Nn':
        break

print(f'Os dados foram: {princ}')
print(f'Ao todo voce cadastrou {len(princ)} pessoas')
print(f'O maior peso foi {maior} kg')

for pessoa in princ: # Varrendo o principal que tem varias listas e vai jogar cada lista para o "PESSOA"
    if pessoa[1] == maior:
        print(f'{pessoa[0]}')

print(f'O menor peso foi de {menor} kg')
for pessoa in princ:
    if pessoa[1] == menor:
        print(f'{pessoa[0]}')