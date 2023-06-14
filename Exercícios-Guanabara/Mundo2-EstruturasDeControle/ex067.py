# Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado
# O programa será interrompido quando o número solicidado for negativo
num = 1
while num > 0:
    num = int(input('Digite um número para cálculo da taboada (digite um número negativo para sair): '))
    if num < 0:
        break
    for n in range(1, 11):
        print(f'{num} x {n} = {num * n}')
