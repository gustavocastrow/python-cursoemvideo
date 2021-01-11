dados = list()
pessoas = list()

pessoas.append(dados[:]) #[:] Fatiamento completo, gera uma copia dos dados

pessoas = [['Pedro', 25], ['Maria', 19], ['Joao', 32]]
print(pessoas[0][0]) #Pedro
print(pessoas[1][1]) #19
print(pessoas[2][0]) #Joao
print(pessoas[1]) #['Maria', 19]

print('===' * 30)

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #Fazendo uma copia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #Fazendo uma copia
print(galera)
totmai = totmen = 0
galera2 = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera2)

for pessoa in galera2:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')


galera3 = list()
dado = list()

for contador in range(0, 3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade: ')))

    galera3.append(dado[:])
    dado.clear()
print(galera3)
print(dado)

for cadaPessoa in galera3:
    if cadaPessoa[1] >= 21:
        print(f'{cadaPessoa[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{cadaPessoa[0]} é menor de idade')
        totmen += 1
print(f'Temos um total de {totmai} maiores de idade')
print(f'Temos um total de {totmen} menores de idade')
