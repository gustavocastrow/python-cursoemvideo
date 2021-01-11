#Variaveis compostas "Listas []"

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

valores = list(range(4, 11))

print(valores)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop() #Remove o ultimo elemento
num.pop(0) #Remove o primeiro elemento (0)
num.remove(2) #Procura do inicio da lista o primeiro elemento que for passado como parametro
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

print(valores)

for chave, valor in enumerate(valores):
    print(f'Na posicao {chave} temos o valor: {valor}')
print('Cheguei ao final da lista')


valores2 = list()
for cont in range(0, 5):
    valores2.append(int(input(f'Informe um valor para a posicao {cont}: ')))
print(valores2)

a = [2, 3, 4, 7]
b = a
b[2] = 8 #A partir do momento que iqualo uma lista a outra o py cria uma ligacao entre elas
print(f'Lista A => {a}')
print(f'Lista B => {b}')

#Fazendo uma copia de uma lista
c = [3, 33 ,5234, 3242]
d = c[:] #D recebe uma copia dos valores de C