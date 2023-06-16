"""Crie um programa que leia o nome e o preço de vários produtos.
o programa deverá perguntar se o usuário quer ou não continuar. Mostre no final:
* qual é o total gasto na compra
* quantos produtos custam mais de 1000
* qual é o nome do produto mais barato"""
total = 0
cheaper = 99999
count_expensive = 0
name_cheaper = ''
while True:
    name = str(input('Digite o nome do produto: '))
    price = float(input('Digite o preço: R$ '))
    total += price
    if cheaper > price:
        cheaper = price
        name_cheaper = name
    if price > 1000:
        count_expensive += 1
    stop = str(input('Gostaria de adicionar mais produtos? [S/N]: ')).strip().lower()
    if stop == 'n':
        break
print(f'A soma dos preços de todos os produtos é {total}')
print(f'O nome do produto mais barato é {name_cheaper} e seu valor é R$ {cheaper}')
print(f'{count_expensive} produtos custam mais de R$ 1000,00.')
