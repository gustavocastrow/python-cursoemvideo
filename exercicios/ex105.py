# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# A maior nota
# A menor nota
# A media da turma
# A situacao (opc)


def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'Boa'
        elif r['media'] >= 5:
            r['situacao'] = 'Razoavel'
        else:
            r['situacao'] = 'Ruim'

    return r

resposta = notas(5.5, 2.5, 9.3, 8.2, sit=True)
print(resposta)