# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado
km = int(input('Digite a quantidade de quilômetros rodados: '))
days = int(input('Digite o número de dias que alugou o carro: '))
total = (days * 60) + (0.15 * km)
print('De acordo com os dados fornecidos o valor total é de R${}'.format(total))
