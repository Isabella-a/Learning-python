from random import randint
from operator import itemgetter
# Crie um programa onde 4 jogadores jogem um dado e tenham resultados aleatórios. Guarde os resultados
# num dicionário. Coloque esse resultado em orgem crescente
plays = {
    'player1': randint(1, 6),
    'player2': randint(1, 6),
    'player3': randint(1, 6),
    'player4': randint(1, 6)
}
sorted_plays = sorted(plays.items(), key=itemgetter(1), reverse=True)
print(sorted_plays)
