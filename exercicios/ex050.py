#Desafio 050 ->  Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0
contador = 0
for inteiros in range (1, 7):
    n = int(input('Informe um numero inteiro: '))
    if n % 2 == 0:
        soma += n
        contador += 1
print(f'Voce informou {contador} numeros PARES e a soma foi {soma}')

