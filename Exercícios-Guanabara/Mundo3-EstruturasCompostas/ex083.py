""" Faça um programa onde o usuário digite uma expressão qualquer que use parênteses
Analise se a expressão está com os parênteses de forma correta"""
expression = str(input('Digite a expressão desejada: '))
parenthesisOpen = 0
parenthesisClose = 0
for p in expression:
    if p == '(':
        parenthesisOpen += 1
    elif p == ')':
        parenthesisClose += 1
if parenthesisOpen == parenthesisClose:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está faltando algum parêntese')
