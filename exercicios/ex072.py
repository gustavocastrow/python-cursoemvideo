#Desafio 72 -> Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze'
            'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Informe um número de 0 até 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente...')

print(f'Você digitou o número {contagem[numero]}')
print(len(contagem))



