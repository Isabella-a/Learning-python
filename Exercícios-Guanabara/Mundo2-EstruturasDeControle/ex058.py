import random
# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
num = random.randint(0, 10)
print('Acabei de gerar um número aleatoriamente, tente adivinhar!')
check = False
count = 1
while not check:
    guess = int(input('Tente adivinhar: '))
    if num == guess:
        check = True
        print('Acertou!')
    else:
        count += 1
print('Você adivinhou depois de {} tentativas'.format(count))
