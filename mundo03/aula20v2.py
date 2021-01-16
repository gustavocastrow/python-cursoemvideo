def soma(a, b):
    s = a + b
    print(s)


soma(5, 2)


def contador(*num): #"*" empacotamento de parametros, ira pegar todos parametros digitado e sera colacado na varivel num
    tamanho = len(num)
    print(f'Recebi os valores {num} e sao do tamanho de {tamanho}')
    print('Fim!')


contador(2, 1, 5)
contador(4, 2)
contador(5, 5, 3, 5, 12, 53)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 3, 21, 53, 51, 90]
dobra(valores)
print(valores)
