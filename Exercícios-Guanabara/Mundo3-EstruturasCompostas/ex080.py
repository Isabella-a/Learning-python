# Faça um programa que leia 5 números e cadastre-os numa lista, já na posiçao correta sem usar o sort. Exiba a lista
list = []
for count in range(0, 5):
    num = int(input('Digite um número: '))
    if count == 0 or num > list[-1]:
        list.append(num)
    else:
        after = 0
        while after < len(list):
            if num <= list[after]:
                list.insert(after, num)
                break
            after += 1
print(f'Os valores digitados em ordem crescente são: {list}')
