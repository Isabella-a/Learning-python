# Crie um programa que tenha uma tupla com várias palavras (não usar acentos)
# Mostre para cada palavra quais são suas vogais
words = ('mundo', 'viajar', 'comida', 'experiencia', 'paises', 'intercabio')
for word in words:
    print(f'\nA palavra {word} possui:', end=' ')
    for letter in word:
        if letter in 'aeiou':
            print(f'{letter}', end=' ')
