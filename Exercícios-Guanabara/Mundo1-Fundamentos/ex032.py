# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
year = int(input('Digite o ano que queira verificar se é bissexto: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto')
