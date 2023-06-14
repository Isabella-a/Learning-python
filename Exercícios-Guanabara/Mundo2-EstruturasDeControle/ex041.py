"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento do atleta e mostre sua
categoria de acordo com a idade:
Até 9 anos: mirim
Até 14 anos: infantil
Até 19 anos: júnior
Até 20 anos: sênior
Acima: master"""
birth_year = int(input('Digite sua idade: '))
if birth_year <= 9:
    print('Mirim')
elif 9 < birth_year <= 14:
    print('Infantil')
elif 14 < birth_year <= 19:
    print('Júnior')
elif 19 < birth_year <= 20:
    print('Sênior')
elif birth_year > 20:
    print('master')
