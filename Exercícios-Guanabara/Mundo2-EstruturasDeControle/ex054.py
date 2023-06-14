from datetime import date
# Crie um programa que leia o ano de nascimento de sete pessoas. Mostre quantas pessoas não atingiram a maioridade
# e quantas já são maiores
current_date = date.today().year
minor = 0
not_minor = 0
for count in range(1, 8):
    year_birth = int(input('Digite o ano de nascimento da {}˚ pessoa: '.format(count)))
    age = current_date - year_birth
    if age >= 18:
        not_minor += 1
    else:
        minor += 1
print('{} pessoas são maiores de idade.'.format(not_minor))
print('{} pessoas são menores de idade.'.format(minor))
