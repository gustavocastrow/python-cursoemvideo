#Aula 13 -> laços

#for -> for c in range(1,10): faz o contador no intervalo de 1 a 10

list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print (list[index])

for c in range(0, 6):
    print(c)
print('Fim')

n = int(input('Digite um numro: '))

for c in range(0, n+1):
    print(c)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for c in range(inicio, fim+1, passo):
    print(c)

soma = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    soma = soma + n
print(soma)