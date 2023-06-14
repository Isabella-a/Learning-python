# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
# a multa deve custar R$ 7,00 por cada km acima do limite
velocity = float(input('Qual a velocidade que o carro chegou? '))
if velocity > 80:
    multa = (velocity - 80) * 7
    print('Recebeu uma multa no valor de {:.2f} reais'.format(multa))
print('Você está dentro da velocidade permitida')
