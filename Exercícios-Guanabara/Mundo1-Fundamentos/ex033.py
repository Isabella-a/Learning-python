# Faça um programa que leia 3 números e fale qual é o maior e qual é o menor
num1 = int(input('Digite um valor: '))
num2= int(input('Digite outro valor: '))
num3 = int(input('Digite outro valor: '))

if num1 > num2 and num1 > num3:
    print('O maior valor é {}'.format(num1))
elif num2 > num1 and num2 > num3:
    print('O maior valor é {}'.format(num2))
else:
    print('O maior valor é {}'.format(num3))

if num1 < num2 and num1 < num3:
    print('O menor valor é {}'.format(num1))
elif num2 < num1 and num2 < num3:
    print('O menor valor é {}'.format(num2))
else:
    print('O menor valor é {}'.format(num3))
