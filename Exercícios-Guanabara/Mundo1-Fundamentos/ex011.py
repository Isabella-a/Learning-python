# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados
width = float(input('Digite a largura da parede: '))
heigth = float(input('Digite a altura da parede: '))
area = width * heigth
ink = area / 2
print('De acordo com as medidas fornecidas a área é {} e será necessário {}l de tinta'.format(area, ink))
