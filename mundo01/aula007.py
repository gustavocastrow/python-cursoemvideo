# Operadores Aritméticos

# + Adição ( 5 + 2 == 7 )
# - Subtração ( 5 - 2 == 3)
# * Multiplicação ( 5 * 2 == 10)
# / Divisão ( 5 / 2 == 2.5)  -> float
# ** Potência ( 5 ** 2 == 25)
# // Divisão inteira ( 5 // 2 == 2)
# % Resto da divisão ( 5 % 2 == 1)

# ORDEM DE PRECEDÊNCIA

#1. (...)
#2. **
#3. *, /, //, % -> Resolve qual aparecer primeiro
#4. +, -

#Ex -> "5+2*3 == 11" -> * -> +
#Ex2 -> "3*5+4**2 == 31"
#Ex3 -> "3*(5+4)**2 == 243"

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
div_inteira = n1 // n2
expo = n1 ** 2
print(f'A soma vale {soma}, \n o produto é {multiplicacao}, \n a divisão é {divisao:.2f}, \n divisão inteira é {div_inteira}')


