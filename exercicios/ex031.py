#Desafio 031 -> Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia_viagem = int(input('Informe a distância da viagem(km): '))

if distancia_viagem <= 200:
    passagem = distancia_viagem * 0.50
    print(f'Uma viagem de {distancia_viagem} km vai custar R$ {passagem:.2f}')
else:
    passagem = distancia_viagem * 0.45
    print(f'Uma viagem de {distancia_viagem} km vai custar R$ {passagem:.2f}')

# forma simplificada -> passagem = distancia_viagem * 0.50 if distancia_viagem <= 200 else distancia_viagem * 0.45

