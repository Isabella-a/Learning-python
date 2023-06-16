""" Crie um programa que leia 4 valores pelo teclado e guarde numa tupla. Mostre:
Quantas vezes apareceu o 9
Em que posição foi digitado o primeiro valor 3
Quais foram os números pares"""
numbers = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite outro número: ')))
print(f'Você digitou o 9 {numbers.count(9)} vezes')
if 3 in numbers:
    print(f'O número 3 aparece na {numbers.index(3) + 1} posição')
print(f'')
