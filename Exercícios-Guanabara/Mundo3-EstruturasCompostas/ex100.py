from random import randint
"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar()
A primeria função vai sortear 5 números e a segunda função vai somar os valores pares"""
def sorteio(list):
    for c in range(0, 5):
        num = randint(1, 10)
        list.append(num)


def somaPar(list):
    sum = 0
    for c in list:
        if c % 2 == 0:
            sum += c
    print(f'Lista: {list}. \nSoma dos valores pares: {sum}')


num = []
sorteio(num)
somaPar(num)
