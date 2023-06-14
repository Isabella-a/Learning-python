# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no
# intervalo de 1 até 500
sum = 0
count = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        count += 1
        sum += num
print('A soma dos {} números é: {}'.format(count, sum))
