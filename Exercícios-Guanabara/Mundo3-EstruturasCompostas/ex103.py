"""Faça um programa que receba dois parâmetros opcionais: o nome do jogador e quantos gols ele marcou
O programa deve mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente"""


def ficha(name, gol):
    if len(name) == 0:
        name = '*não informado*'
    if not gol.isnumeric():
        g = 0
    print(f'O jogador {name} fez {g} gols')


name_player = str(input('Digite o nome do jogador: ')).strip()
gol = input('Digite o número de gols: ')
ficha(name_player, gol)
