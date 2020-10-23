#Desafio 062 -> Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 0
total = 0
termos_mais = 10

while termos_mais != 0:
    total = total + termos_mais
    while contador <= total:
        print(f'{termo} ->')
        termo += razao
        contador += 1
    print('Pause')
    termos_mais = int(input('Quantos termos você quer mostrar a mais?: '))
print(f'Progressão finalizada com {total} termos')