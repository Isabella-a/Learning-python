# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
meter = float(input('Digite o tamanho em metros: '))
print('O valor convertido para centimetros é {}cm e em milímetros é {}mm'.format((meter * 100), (meter * 10000)))
