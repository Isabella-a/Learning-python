# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo
city = str(input('Digite o nome de uma cidade: ')).strip()
print(city[:5].lower() == 'santo')
