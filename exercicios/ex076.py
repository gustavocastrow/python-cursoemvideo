# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.


listagem = ('iPhone 12', 7.899,
            'Apple Watch 6', 5.499,
            'iPad Pro', 9.899,
            'Macbook Pro', 21.899,
            'Apple TV 4K', 1.299,
            'iMac 27 5k', 25.899)

print('-'*30)
print('Listagem de preço')
print('-'*30)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>5}')