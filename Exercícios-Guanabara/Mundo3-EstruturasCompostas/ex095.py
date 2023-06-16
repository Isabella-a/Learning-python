""" Desafio 93:
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador,
quantas partidas ele jogou, quantidade de gols feitos em cada partida.
Guarde tudo um dicionário e inclua o total de gols feitos durante o compeonato"""

# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
# detalhes de aproveitamento de cada jogador
player = {}
matches = []
team = []
while True:
    player.clear()
    player['nome'] = str(input('Nome: '))
    total = int(input('Quantas partidas ele jogou? '))
    matches.clear()
    for c in range(1, total + 1):
        matches.append(int(input(f'Quantos gols na partida {c}? ')))
    player['gols'] = matches[:]
    player['total'] = sum(matches)
    team.append(player.copy())
    keep_going = str(input('Deseja cadastrar mais jogadores? [S/N]: ')).lower()[0]
    if keep_going in 'n':
        break
print(team)
while True:
    search = int(input('Digite o número do jogador que deseja pesquisar: '))
    if search > len(team):
        print('Não existe esse jogador!')
        break
    else:
        print(team[search])