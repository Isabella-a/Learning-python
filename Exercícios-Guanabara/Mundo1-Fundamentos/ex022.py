""" Crie um programa que leia o nome completo de uma pessoa e mostre:
O nemo com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo sem considerar espaços
Quantas letras tem o primerio nomme"""

name = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com todas as letras maiúsculas: {}'.format(name.upper()))
print('Seu nome com todas as letras minúsculas: {}'.format(name.lower()))
print('Seu nome tem {} letras.'.format(len(name) - name.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(name.find(' ')))
