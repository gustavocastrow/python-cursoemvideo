
#For -> Consegue dizer um intervalo(range) "for i range (1,10), precisa saber o limite (range)
#While (enquanto) -> Quando eu não sei o intervalo

#Sei o Limite = While e For
#Não sei o Limite = While
#Condição de parada = While

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} pares e {impar} impares')
