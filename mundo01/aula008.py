#  utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de
#  funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos,
#  oferecidos no Pypi.

# import nome_modulo/biblioteca -> importa todas as funcionalidades de um módulo
# from nome_modulo import nome_funcionalidade -> importa apenas as funcionalidades que eu escolher

#import math  // from math import sqrt
#math.ceil -> arrendondamento pra cima
#math.floor -> arrendondamento pra baixo
#math.trunc -> eliminar da virgula pra frente
#math.pow -> potencia
#math.sqrt -> raiz quadrada
#math.factorial -> fatorial
from math import sqrt
import random
numero = int(input('Digite um numero: '))
raiz = sqrt(numero)
print(raiz)


num = random.randint(0, 100)
print(num)
