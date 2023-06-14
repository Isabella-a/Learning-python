import random
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido

student1 = input('Digite o nome do primeiro aluno: ')
student2 = input('Digite o nome do segundo aluno: ')
student3 = input('Digite o nome do terceiro aluno: ')
student4 = input('Digite o nome do quarto aluno: ')
class_student = [student1, student2, student3, student4]
student = random.choice(class_student)
print('O aluno sorteado foi {}'.format(student))
