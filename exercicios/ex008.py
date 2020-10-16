#Desafio 008 -> Faca um programa que leia um valor em metros e exiba convertido em centimetros e milimentros

metros = float(input('Metros: '))
cm = metros * 100
mm = metros * 1000

print(f'{metros:.2f}m em cm: {cm:.2f}cm \n {metros:.2f}m em mm: {mm:.2f}mm')