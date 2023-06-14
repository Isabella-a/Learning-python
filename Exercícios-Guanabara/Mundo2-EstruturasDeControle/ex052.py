# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
count_primo = 0
num = int(input('Digite um número: '))
for count in range(1, num + 1):
    if num % count == 0:
        count_primo += 1
if count_primo >= 3:
    print('Não é um número primo!')
else:
    print('É um número primo!')
