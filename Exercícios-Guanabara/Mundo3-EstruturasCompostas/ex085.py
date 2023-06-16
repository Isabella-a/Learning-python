# Crie um programa onde a pessoa digite 7 valores. Cadastre em uma lista única que mantenha separado os valores pares
# dos ímpares. Mostre em ordem crescente
par = []
impar = []
for n in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'O números pares digitados em ordem crescente são: {sorted(par)}')
print(f'O números impares digitados em ordem crescente são: {sorted(impar)}')
