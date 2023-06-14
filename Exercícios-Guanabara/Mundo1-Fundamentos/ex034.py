# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a 1250, aumento de 10%
# Inferiores ou iguais aumento de 15%
salary = float(input('Digite seu salário: '))
if salary > 1250:
    print('Seu salário com o aumento é {} reais'.format(salary * 1.1))
else:
    print('Seu salário com o aumento é {} reais'.format(salary * 1.15))
