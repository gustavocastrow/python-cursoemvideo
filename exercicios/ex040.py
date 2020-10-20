#Desafio 040 ->
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe sua segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print(f'Média {media} abaixo de 5 -> R E P R O V A D O')
elif media >= 5.0 and media <= 6.9:
    print(f'Média {media} entre 5.0 e 6.9 -> R E C U P E R A Ç Ã O')
else:
    print(f'Média {media} superior ou igual a 7 -> A P R O V A D O')