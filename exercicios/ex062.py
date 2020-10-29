#Desafio 062 -> Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Qual a razão?: '))
termo = primeiro
contador = 1
total_termos = 0
mais = 10

while mais != 0:
    total_termos += mais
    while contador <= total_termos:
        print(f'{termo}')
        termo += razao
        contador += 1
    print('Pausa...')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Proressão finalizada com {total_termos} termos.')