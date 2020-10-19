#Desafio 034 -> Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe seu salario: '))

if salario <= 1250.00:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f'Salario de {salario:.2f}, portanto aumento de {aumento:.2f}, totalizando {novo_salario:.2f}')
else:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f'Salario de {salario:.2f}, portanto aumento de {aumento:.2f}, totalizando {novo_salario:.2f}')

