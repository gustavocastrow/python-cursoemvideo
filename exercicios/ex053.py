#Desafio 053 -> Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:

frase = str(input('Digite uma frase')).strip().upper() #Lendo a frase // strip -> tira os espaços //upper -> transforma em maiuscula

#Separando a frase em palavras:
palavras = frase.split() # Gerando uma lista com o split.

#Juntando as palavras da frase
junto = ''.join(palavras) # Juntando a lista e eliminando os espaços

inverso = ''

for letra in range(len(junto) - 1, - 1, -1): # Indo da ultima letra até a primeira e voltando uma letra
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase é um palindromo!')

