#Desafio 044 ->
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto (1)
# à vista no cartão: 5% de desconto (2)
# em até 2x no cartão: preço formal (3)
# 3x ou mais no cartão: 20% de juros (4)


valor_pago = float(input('Valor a ser pago: '))
pagamento = int(input('''Informe a condição de pagamento:
[1] - A vista dinheiro/cheque -> 10% desconto
[2] - A vista cartão -> 5% desconto
[3] - Em até 2x no cartão -> Preco normal
[4] - 3x ou mais no cartão -> 20% juros
'''))

if pagamento == 1:
    desconto = valor_pago * 0.10
    preco_final = valor_pago - desconto
    print(f'Valor R$ {valor_pago:.2f}, forma de pagamento: {pagamento}, valor final R$ {preco_final:.2f}')
elif pagamento == 2:
    desconto = valor_pago * 0.05
    preco_final = valor_pago - desconto
    print(f'Valor R$ {valor_pago:.2f}, forma de pagamento: {pagamento}, valor final R$ {preco_final:.2f}')
elif pagamento == 3:
    print(f'Primeira parcela: {valor_pago / 2} -> segunda parcela {valor_pago / 2} valor final -> {valor_pago}')
else:
    juros = valor_pago * 0.20
    preco_final = valor_pago + juros
    print(f'Valor R$ {valor_pago:.2f}, forma de pagamento: {pagamento}, valor final R$ {preco_final:.2f}')
