# Refaça o desafio 09, mostrando a tabuada de um número qeu o usuário escolher, só que agora utilizando um laço for
num = int(input('Digite um número para calcular a tabuada: '))
for count in range(1, 11):
    print('{} x {} = {}'.format(num, count, num * count))
