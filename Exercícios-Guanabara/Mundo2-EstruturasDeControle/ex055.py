# Faça um programa que leia o peso de cinco pessoas e mostre qual foi o maior e o menor peso
heaviest = 0
lighter = 0
for count in range(1, 6):
    weight = float(input('Digite o peso da {}˚ pessoa: '.format(count)))
    if count == 1:
        heaviest = weight
        lighter = weight
    else:
        if weight > heaviest:
            heaviest = weight
        if weight < lighter:
            lighter = weight
print('O maior peso é: {}'.format(heaviest))
print('O menor peso é: {}'.format(lighter))
