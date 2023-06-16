from random import randint
# Ajude um jogador da mega sena a criar palpites. Perguntes quantos jogos serão gerados e gere 6
# números aleatórios. Armazene numa lista composta
list = []
finalList = []
num_plays = int(input('Quantos jogos gostaria de sortear? '))
count2 = 0
while count2 <= num_plays:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in list:
            list.append(num)
            count += 1
        if count == 6:
            break
    finalList.append(list[:])
    list.clear()
    count2 += 1
print(f'Números sorteados: {finalList}')
