""" Faça um programa que leia 5 números e cadastre-os numa lista.
Crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
Mostre o conteúdo das 3 listas"""
list = []
impar = []
par = []
for count in range(0, 5):
    num = int(input('Digite um número: '))
    list.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'Lista completa: {list}')
print(f'Números ímpares: {impar}')
print(f'Números pares: {par}')
