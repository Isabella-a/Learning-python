import math
# from math import sqrt

# Exemplo da aula 8
'''num = int(input('Digite um número: '))
sqr = math.sqrt(num)
print('A raiz quadrada é {}'.format(math.floor(sqr)))'''

# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porçao inteira (usar math)
num = float(input('Digite um número decimal: '))
print('A porção inteira do valor digitado é {}'.format(math.trunc(num)))
# print('A porção inteira do valor digitado é {}'.format(int(num)))
