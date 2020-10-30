#Tuplas -> variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura,
# acessíveis por chaves individuais.

# 3 tipos de variaveis compostas -> Tuplas(), Listas[], Dicionarios{}
#len(tupla) -> retorna quantos elementos tem a tupla.


# TUPLAS SÃO IMUTAVEIS, PORTANTO NÃO DA PRA SUBSTITUIR VALORES DE DENTRO DA TUPLA

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print('1 FOR ==============================')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('2 FOR ==============================')
for cont in range(0, len(lanche)):
    print(f'Comi {lanche[cont]} na poisção {cont}')
print('3 FOR ==============================')
for pos, food in enumerate(lanche):
    print(f'Vou comer {food} na posição {pos}')

print(len(lanche))
print(sorted(lanche)) #Mostra em ordem, porém não mudou a ordem apenas mostrou ordenado.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))
print(c.index(8))

# Tuplas aceitam varios tipos de dados, string, number, int, float, boolean

#del(x) -> apaga a tupla

