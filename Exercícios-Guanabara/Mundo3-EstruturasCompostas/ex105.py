"""Faça um programa que pode receber várias notas de alunos e vai retornar um dicionário com as informações:
Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação(opcional)"""

def grades(*n, sit=False):
    """
    Descrição da funcionalidade dessa função
    :param n:
    :param sit:
    :return:
    """
    list = {}
    list['total'] = len(n)
    list['maior'] = max(n)
    list['menor'] = min(n)
    list['média'] = sum(n) / len(n)
    if sit:
        if list['média'] >= 7:
            list['situação'] = 'Ótimo'
        elif list['média'] >= 5:
            list['situação'] = 'Recuperação'
        else:
            list['situação'] = 'Estude muito'
    return list


notas = grades(4, 2, 6, 9, 7, 6, 8, sit=True)
print(notas)
help(grades)
