# Escreva um programa que converta uma temperatura digitada em ˚C e converta para ˚F
temperature_c = float(input('Digite a temperatura em ˚C: '))
temperature_f = ((9 * temperature_c) / 5) + 32
print('Essa temperatura equivale a {}˚F'.format(temperature_f))
