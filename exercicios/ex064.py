#Desafio 065 ->  Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
# usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre eles (desconsiderando o flag).
numero = 0
cont = 0
soma = 0
numero = int(input('Digite um numero: [999 para parar]'))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um numero: [999 para parar]'))
print(f'Voce digitou {cont} numeros e a soma deles foi {soma}')