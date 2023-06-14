# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou o empréstimo será negado
house = float(input('Digite o valor da casa: '))
salary = float(input('Digite seu salário: '))
years_to_pay = int(input('Deseja pagar em quantos anos? '))
prestacao = house / (years_to_pay * 12)
print('O valor da prestação é: {:.2f}'.format(prestacao))
if prestacao > salary * 0.3:
    print('Empréstimo negado!')
