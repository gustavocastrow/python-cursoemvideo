#Variaveis compostas -> TUPLAS

#Tuplas () => Variaveis compostas e IMUTAVEIS que permitem armazenar varios valores de tipos diferentes em uma mesma estrutura,
# acessivel por chaves individuais

#Listas []
#Dicionarios {}


# TUPLAS SÃO IMUTAVEIS, PORTANTO NÃO DA PRA SUBSTITUIR VALORES DE DENTRO DA TUPLA

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')

print('1 FOR =============')

#Enumerate -> Retorna o dado e a posicao.
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')

#sorted -> mostra em ordem
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(a)
print(b)
print(c)

print(len(c))

print(c.count(5))
print(c.index(8)) #Retorna a posicao do parametro

pessoa = ('Gustavo', 25, 'M', 85) #Aceita dados de tipos diferentes
del(pessoa) #Apaga a tupla