"""Crie um programa que vai funcionar semelhante a função input, só que fazendo a validação para aceitar apenas
um valor numérico"""

"""Reescrena a função leiaInt() do desafio 104, incluindo a possibilidade da digitação de um
número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade"""

def leiaInt(text):
    while True:
        try:
            n = int(input(text))
        except (ValueError, TypeError):
            print('Erro! Digite um número inteiro')
            continue
        else:
            return n


num = leiaInt('Digite um número: ')
print(f'Valor digitado: {num}')
