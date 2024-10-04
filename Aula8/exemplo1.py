import os

os.system('cls')


def dobro_triplo(num):
    dobro = num * 2
    triplo = num * 3
    return dobro, triplo

# Parte Principal
num = float(input('Informe o número: '))
x2, x3 = dobro_triplo(num)
print(f'O dobro é {x2} e o triplo é {x3}')

