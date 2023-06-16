"""Aprimore o exemplo anterior mostrando:
A soma de todos os valores pares
a soma dos valores da terceira coluna
o maior valor da segunda linha"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_par = 0
third_c = 0
bigger_value = 0
for n in range(0, 3):
    for n2 in range(0, 3):
        matriz[n][n2] = int(input('Digite um valor: '))
for n in range(0, 3):
    for n2 in range(0, 3):
        print(f'[{matriz[n][n2]}]', end='')
        if matriz[n][n2] % 2 == 0:
            sum_par += matriz[n][n2]
    print()
for n in range(0, 3):
    third_c += matriz[n][2]
for n in range(0, 3):
    if matriz[1][n] > bigger_value:
        bigger_value = matriz[1][n]
print(f'A soma dos valores pares é: {sum_par}')
print(f'A soma dos valores da terceira coluna é: {third_c}')
print(f'O maior valor da segunda linha é: {bigger_value}')
