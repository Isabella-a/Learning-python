"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em
um dicionário e todos os dicionários numa lista. Mostre:
Quantas pessoas foram cadastradas
Média de idade do grupo
Lista de todas as mulheres
Lista de todas as pessoas com idade acima da média"""
person = {}
people = []
count = 0
sum_age = 0
older_people = []
women = []
while True:
    person.clear()
    person['name'] = str(input('Digite o nome: '))
    person['gender'] = str(input('Digite o sexo: [F/M] ')).lower()[0]
    person['age'] = int(input('Digite a idade: '))
    people.append(person.copy())
    sum_age += person['age']
    keep_going = str(input('Deseja cadastrar mais alguém? [S/N] ')).lower()[0]
    if keep_going == 'n':
        break

for p in people:
    if p['age'] > sum_age/len(people):
        older_people.append(p['name'])
    if p['gender'] == 'f':
        women.append(p['name'])

print(f'Número de pessoas cadastradas: {len(people)}')
print(f'Média de idade do grupo: {sum_age / len(people):.2f}')
print(f'Lista de todas as mulheres: {women}')
print(f'Lista de todas as pessoas com idade acima da média: {older_people}')
