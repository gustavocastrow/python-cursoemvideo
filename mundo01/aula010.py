#Condições parte 01.
#Condições simples e condições compostas.

#Simplificada -> print('carro novo' if tempo <=3 else 'carro velho')

nome = str(input('Qual seu nome?: '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print(f'Seu nome é tão normal!')
print(f'Bom dia {nome}!')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

if m >= 6.0:
    print('Aprovado')
else:
    print('Reprovado')