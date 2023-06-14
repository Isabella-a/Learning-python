# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto
gender = str(input('Digite seu sexo -> F ou M: ')).strip()
while gender not in 'MmFf':
    gender = str(input('Informe com as letras F ou M: '))
print('Obrigada!')
