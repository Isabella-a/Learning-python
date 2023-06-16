# Crie uma tupla totalmente preenchida com uma contagem por extenso de zero a 20
#  Seu programa deverá ler um número no teclado (entre 0 e 20) e mostrá-lo por extenso
list = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
        'treze', 'quartorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número de 0 a 20: '))
print(f'O número por extenso é: {list[num]}')
