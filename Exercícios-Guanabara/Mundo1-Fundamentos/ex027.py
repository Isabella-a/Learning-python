# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
name = str(input('Digite seu nome: ')).strip()
name = name.split()
print('Primeiro nome: {} \n último nome: {}'.format(name[0], name[len(name) - 1]))
