#Desafio 066 ->

numero = 0
contador = 0
soma = 0
while numero != 999:
    numero = int(input('Informe um número: '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'Foram digitados {contador}, e a sofma deles é {soma}')