# Crie um programa que leia vários números inteiros pelo teclado. Mostre a média entre todos os valores e qual foi
# o maior e o menor valores lidos. O programa deve perguntar o usuário se quer ou não continuar a digitar valores

num = int(input('Digite um número: '))
continuar = str(input('Gostaria de continuar? [S/N]: ')).strip().lower()
count = 1
sum = num
while continuar == 's':
    num = int(input('Digite outro número: '))
    sum += num
    count += 1
    continuar = str(input('Gostaria de continuar? [S/N]: ')).strip().lower()
print('A soma dos {} números digitados é {} e a média é {}'.format(count, sum, sum / count))
