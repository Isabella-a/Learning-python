# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
# Mostre: média de idade, nome do homem mais velho, quantas mulheres tem menos de 20 anos
sum_age = 0
sum_minor_w = 0
oldest_man = 0
name_oldest = ''
for count in range(1, 5):
    name = str(input('Digite o nome da {}˚ pessoa: '.format(count)))
    age = int(input('Digite a idade da {}˚ pessoa: '.format(count)))
    gender = str(input('Digite F para femino e M para masculino da {}˚ pessoa: '.format(count))).strip().lower()
    sum_age += age
    if gender == 'm' and oldest_man < age:
        oldest_man = age
        name_oldest = name
    if gender == 'f' and age < 20:
        sum_minor_w += 1
print('A média de idade é de {} anos'.format(sum_age / 4))
print('O homem mais velho chama {} e tem {} anos.'.format(name_oldest, oldest_man))
if sum_minor_w == 0:
    print('Todas as mulheres tem mais de 20 anos')
else:
    print('{} mulher(es) tem menos de 20 anos.'.format(sum_minor_w))
