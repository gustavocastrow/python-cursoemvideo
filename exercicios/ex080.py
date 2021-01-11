# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for cont in range(0, 5):
    num = int(input('Digite um valor: '))

    if cont == 0 or num > lista[-1]: #Se o numero for o primeiro valor, faz o append OU se for maior tambem faz o append.
        lista.append(num)
        print('Adicionado ao final da lista')
    else: #Descobrindo a posicao para adicionar

        pos = 0
        while pos < len(lista):
            if num <= lista[pos]: #Verifica se em cada posicao se o numero inserido e menor ou igual a ele.
                lista.insert(pos, num)
                print(f'Adicionado na posicao {pos}')
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {lista}')