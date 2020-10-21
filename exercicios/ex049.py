#Desafio 049 -> Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando
# um laço for.

numero = int(input('Informe um número para fazer a tabuada: '))

for tabuada in range(0, 11):
    print(f'{numero} X {tabuada} = {numero * tabuada}')
