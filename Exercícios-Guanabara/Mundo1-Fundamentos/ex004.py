# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele
var = input('Digite algo: ')
print('O tipo do que digitou é: ', type(var))
print('É um número? ', var.isnumeric())
print('É uma letra? ', var.isalpha())
print('É um número ou letra? ', var.isalnum())
print('Está em caixa alta? ', var.isupper())
print('Está em letras minúsculas? ', var.islower())
