# Escreva um programa que leia um número inteiro qualquer e paça para o usuário escolher qual será a base de conversão
# 1 para binário
# 2 para octal
# 3 para hexadecimal
num = int(input('Digite um número: '))
options = int(input('''
Pra converter digite:
1 para binário
2 para octal
3 para hexadecimal
:::: '''))
if options == 1:
    print('O valor convertido é {}'.format(bin(num)))
elif options == 2:
    print('O valor convertido é {}'.format(oct(num)))
elif options == 3:
    print('O valor convertido é {}'.format(hex(num)))
