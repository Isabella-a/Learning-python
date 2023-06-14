"""Faça um programa que leia uma frase pelo teclado e mostra
Quantas vezes aparece a letra A
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez"""

sentese = str(input('Digite uma frase qualquer: ')).strip().lower()
print('A letra A aparere {} vezes.'.format(sentese.count('a')))
print('A primeira letra A apareceu na posição {}'.format(sentese.find('a') + 1))
# Ao colocar o r na frente ele começa a buscar da direita
print('A última letra A apareceu na posição {}'.format(sentese.rfind('a') + 1))
