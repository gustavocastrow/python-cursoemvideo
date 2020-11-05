#Aula 18 =>
# juntando uma lista na outra.

pessoas = [['Pedro', 25], ['Joao', 29], ['Maria', 19]]

print(f'Pessoas[0][0] {pessoas[0][0]}') #Pedro
print(f'Pessoas[1][1] {pessoas[1][1]}') #29
print(f'Pessoas[2][0] {pessoas[2][0]}') #Maria
print(f'Pessoas[1] {pessoas[1]}')


teste = list()

teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
#Se fizer dois append seguidos ele cria uma ligacao entre as duas listas e oque muda em uma muda em outra
#Portanto e necessario fazer uma copia utilizand [:]

print(galera)
print(teste)

galera2 = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for pessoa in galera2:
    print(pessoa[0])

galera3 = list()
dado = list()
totalmaior = totalmenor = 0
for contador in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:]) #Fazendo uma copia do dado
    dado.clear() #Comando para mostrar os dados caso nao tenha digitado [:]

for pessoa3 in galera3:
    if pessoa3[1] >= 21:
        print(f'{pessoa3[0]} e maior de idade!')
        totalmaior += 1
    else:
        print(f'{pessoa3[0]} e menor de idade! ')
        totalmenor += 1

print(galera3)
print(f'Temos {totalmenor} menores de idade. ')
print(f'Temos {totalmaior} maiores de idade.')