#Desafio 046 -> Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram
# no intervalo de 1 até 500

soma = 0
contador = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        contador = contador + 1 # Contador soma "+1" ao valor
        soma = soma + i # Acumulador "soma" ao valor
print(f'A soma de todos {contador} valores solicitados é {soma}')

