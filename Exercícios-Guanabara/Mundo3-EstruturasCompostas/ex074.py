from random import randint
# Crie um programa que gere 5 números aleatórios e os coloque numa tupla
# Mostre  a listagem de números gerados e indique o menor e maior valor gerados
numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'O números gerados foram: {numbers}')
print(f'O maior número é {max(numbers)}')
print(f'O menor número é {min(numbers)}')
