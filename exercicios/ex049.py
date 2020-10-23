#Desafio 049 -> Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando
# um laço for.

tabuada = int(input('Informe um número para a tabuada: '))
for c in range(0, 11):
    mult = c * tabuada
    print(f'{tabuada} X {c} = {mult}')