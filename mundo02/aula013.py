#Aula 13 -> laços

#for -> for c in range(1,10): faz o contador no intervalo de 1 a 10
for c in range (1, 6):
    print('oI')
print('FIM')

numero = int(input('Informe um número: '))
for num in range(0, numero+1):
    print(num)

inicio = int(input('Inicio: '))
final = int(input('Final: '))
passo = int(input('Passo'))

for x in range(inicio, final+1, passo):
    print(x)

soma = 0
for a in range(0, 5):
    n = int(input('Valor: '))
    soma += n
print(soma)