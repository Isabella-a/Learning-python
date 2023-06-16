# Crie um programa que simule o funcionamento de um caixa eletrônico. Pergunte ao usuário qual será
# o valor a ser sacado (int) e o programa vai informar as cédulas de cada valor que serão entregues
# Cédulas: 50, 20, 10 e 1
saque = int(input('Quanto gostaria de sacar? R$ '))
type_ced = 50
count_ced = 0
while True:
    if saque >= type_ced:
        saque -= type_ced
        count_ced += 1
    else:
        if count_ced > 1:
            print(f'Número de cédulas de R$ {type_ced}: {count_ced}')
        if type_ced == 50:
            type_ced = 20
        elif type_ced == 20:
            type_ced = 10
        elif type_ced == 10:
            type_ced = 1
        count_ced = 0
        if saque == 0:
            break
