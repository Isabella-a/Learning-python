# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
# Sequência de Fibonacci
terms = int(input('Digite o número de termos que quer mostrar na Sequência de Fibonacci: '))
num1 = 0
num2 = 1
print('{} {}'.format(num1, num2), end='')
count = 3
while count <= terms:
    num3 = num1 + num2
    print(' {}'.format(num3), end='')
    num1 = num2
    num2 = num3
    count += 1
