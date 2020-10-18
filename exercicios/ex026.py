#Desafio 026 -> Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que
# posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print(f"A letra A aparece {frase.count('A')}")
print(f"A primeira letra A apareceu na posição {frase.find('A')}")
print(f"A primeira letra A apareceu na posição {frase.rfind('A')}")
