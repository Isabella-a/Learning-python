# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsidere espaços
sentence = str(input('Digite uma frase: ')).strip().lower()
separate = sentence.split()
join = ''.join(separate)
invert = ''
# vai começar no final mas como começa no 0 tem que subtrair 1,
# vai até a posição 0 (então tem que subtrair pq não pega o último
# e como vai do final para o início, precisa ir subtraindo 1 até chegar na primeira letra
for letter in range(len(join) - 1, -1, -1):
    invert += join[letter]
if invert == sentence:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
