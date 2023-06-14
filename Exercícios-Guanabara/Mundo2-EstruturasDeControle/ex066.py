# Crie um programa que leia vários números inteiros pelo teclado. Pára quando o usuário digitar 999.
# mostre quantos números foram digitados e qual foi a soma entre eles
num = 0
count = 0
sum = 0
while num != 999:
    num = int(input('Digite um número e para parar digite 999: '))
    count += 1
    sum += num
sum = sum - 999
print(f'Você digitou {count} números e a soma é {sum}')
