#Listas [] pt 01.
#Listas sao mutaveis.

#Adicionar elementos novos na lista = lista.append('')
#Adicionar elemento em uma posicao espeficia => lista.insert(0, 'novo elemento') -> o novo elemento sera adicionado na
# posicao 0 e todo o resto da lista sera empurraddo para esquerda.
# Apagar elementos => del lista[3]
# Apagar elemento  => lista.pop(3) -> normalmente utilizado para eliminar o ultimo elemento
# Apagar elemento => lista.remove('elemento') -> elimina pelo conteudo
# Elimina o elemento e reposiciona a lista
# if 'piza' in lanche: lanche.remove('piza')
# Declarando uma lista => valores = LIST(range(4, 11)) = [4, 5, ,6 ,7 ,8, 9, 10]
# Ordenando elementos da lista => lista.sort() // ordem reversa => lista.sort(reverse=True)
# Tamanho da lista => len(lista)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7) # Adicionando um elemento ao final da lista
num.sort() # Ordenando os elementos da lista
num.sort(reverse=True) # Invertando a ordem da lista
num.insert(2, 0) # Inserindo o elemento O na posiscao 2
num.pop(2) # Removendo o segundo elemento da lista (comeca do 0-1-2)
num.remove(2) # Remove o primeiro 2 que aparecer na lista caso tenha mais de um 2 precisa utilizar o for
print(num)
print(f'Essa lista tem {len(num)} elementos')

if 5 in num:
    num.remove(5)
else:
    print('Nao encontrei nenhum elemento 5 na lista')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for chaves, valor in enumerate(valores): # Pega a chave e o valor
    print(f'Na posicao {chaves} temos o valor {valor}.')
print('Cheguei ao final da lista')


# Lendo valores do teclado e colocando na lista.

valores2 = list()
for cont in range(0, 5):
    valores2.append(int(input('Digite um valor: ')))
print(valores2)

# Fazendo uma ligacao entre listas, o que mudar em uma sera alterado em outra.
a = [2, 3, 4, 7]
b = a
b[2] = 8

print(f'Lista A {a}')
print(f'Lista B {b}')


# Copia entre uma lista e outra

x = [1, 2, 3, 4]
y = x[:] # Todos os valores de X serao jogados em Y, portando ira criar uma copia
y[2] = 8
print(f'Lista X {x}')
print(f'Lista Y {y}')
