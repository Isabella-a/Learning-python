import uteis
"""Crie um módulo que tenha as funções incorporadas: aumentar(), diminuir(), dobro() e metade()
Faça também um programa que importe esse módulo e use algumas dessas funções"""

"""Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores
como um valor monetário formatado"""

"""Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda()"""

price = float(input('Digite o preço: R$ '))
tax = int(input('Digite a porcentagem que gostaria de aumentar ou diminuir: '))
print(f'A metade de {uteis.currency(price)} é {uteis.half(price, True)}')
print(f'O dobro de {uteis.currency(price)} é {uteis.double(price, True)}')
print(f'Aumentando {tax}% do preço: {uteis.increase(price, tax, True)}')
print(f'Diminuindo {tax}% do preço: {uteis.decrease(price, tax, True)}')
