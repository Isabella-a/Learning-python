"""Faça um programa que receba 3 parâmetros: início, fim e passo.
Seu programa tem que realizar 3 contagens através da função criada:
De 1 até 10, de 1 em 1
De 10 até 0, de 2 em 2
Uma contagem personalizada"""
def contagem(i, f, p):
    count = i
    if i < f:
        while count <= f:
            print(f'{count} ', end='')
            count += p
    else:
        while count >= f:
            print(f'{count} ', end='')
            count -= p


contagem(1, 10, 1)
print()
contagem(10, 1, 2)
