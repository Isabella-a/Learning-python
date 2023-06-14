# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas
distance = float(input('Digite a distância em km da sua viagem: '))
if distance < 200:
    print('O valor da passagem é {:.2f} reias'.format(distance * 0.5))
else:
    print('O valor da passagem é {:.2f} reias'.format(distance * 0.45))
