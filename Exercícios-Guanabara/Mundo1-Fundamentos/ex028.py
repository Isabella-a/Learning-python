from random import randint
# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador
# o programa deverá escrever na tela se o usuário venceu ou perdeu
print('Vou sortear de forma aleatória um número entre 0 e 5, tente advinhar que número será.')
num = randint(1, 5)
guess_num = int(input('Qual número acha que foi sorteado? '))
if num == guess_num:
    print('Acertou')
else:
    print('Errou')
print('O número era: {}'.format(num))
