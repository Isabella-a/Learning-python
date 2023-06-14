"""Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso"""

num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
option = 0
while option != 5:
    option = int(input("""Digite a operação que deseja realizar:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa: """))
    if option == 1:
        print('{} + {} = {}'.format(num, num2, num + num2))
    elif option == 2:
        print('{} x {} = {}'.format(num, num2, num * num2))
    elif option == 3:
        if num > num2:
            print('O maior valor é: {}'.format(num))
        elif num < num2:
            print('O maior valor é: {}'.format(num2))
        else:
            print('Os números são iguais')
    elif option == 4:
        num = int(input('Digite um novo número: '))
        num2 = int(input('Digite outro número: '))
    elif option == 4:
        print('Programa finalizado')
    else:
        print('Opção inválida!')
print()
