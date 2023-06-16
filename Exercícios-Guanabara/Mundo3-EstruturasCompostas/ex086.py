# Crie uma matriz de dimensão 3x3 e preencha com valores digitados. Mostre a matriz com a formatação correta
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for n in range(0, 3):
    for n2 in range(0, 3):
        matriz[n][n2] = int(input('Digite um valor: '))
for n in range(0, 3):
    for n2 in range(0, 3):
        print(f'[{matriz[n][n2]}]', end='')
    print()