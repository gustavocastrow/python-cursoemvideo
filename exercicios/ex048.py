#Desafio 046 -> Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram
# no intervalo de 1 até 500

soma = 0
total_numeros = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        total_numeros = total_numeros + 1
print(f'Soma: {soma} // Total numeros: {total_numeros}')
