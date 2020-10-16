#Desafio 013 -> Faça um algoritmo que leia o salario de um funcionário e de  15% de aumento

salario = int(input('Informe seu salário: '))
aumento = salario * 0.15
novo_salario = salario + aumento

print(f'Salario antigo: R$ {salario:.2f} \n Total Aumento: R$ {aumento:.2f} \n Salario novo R$ {novo_salario:.2f}')