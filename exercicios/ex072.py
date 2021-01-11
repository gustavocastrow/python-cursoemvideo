# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input('Informe um numero entre 0 20: '))
    if numero < 0 or numero > 20:
        print('Tente novamente com um numero entre 0 e 20.')
    else:
        print(f'Voce informou o numero {contagem[numero]}')
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()

    if resposta not in 'S':
        break
print('Programa finalizado...')