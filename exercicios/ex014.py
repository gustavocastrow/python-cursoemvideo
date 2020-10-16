#Desafio 014 ->
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = int(input('Informe a temperatura em Celsius: '))
fahrenheit = (temp * 9/5) + 32

print(f'{temp}C é igual a {fahrenheit}F')