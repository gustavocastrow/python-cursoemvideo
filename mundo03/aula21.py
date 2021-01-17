
#Docstrings: Documentacao feia dentro da funcao para explica-la usando """ """
#Argumentos opcionais: parametro=0
#Escopos de variaveis: Variaveis fora de funcoes: escopo global, variaveis dentro de funcoes: variavel local
#Retorno de resultados:
#Interactive Help: "help()"

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(1, 123, 5)
r2 = somar(32, 12)
r3 = somar(4)

soma = somar(r1, r2, r3)

print(f'Meus calculos deram {r1}, {r2}, {r3}')
print(f'A soma de {r1} + {r2} + {r3} é {soma}')

def funcao():
    n1 = 4
    print(f'N1 local vale {n1}')
funcao()


n1 = 2
print(f'N1 Global vale: {n1}')

def fatorial(num = 1):
    f = 1
    for contador in range(num, 0, -1):
        f *= contador
    return f

n = int(input('Informe um numero: '))
print(f'O fatorial de {n} é {fatorial(n)}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Informe um numero: '))
print(par(num))
