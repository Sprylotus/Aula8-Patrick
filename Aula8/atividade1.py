import os

def limpa_tela():
    os.system('cls')    


import random


def decoracao():
    print(12*'=')


def ale():
    n1 = random.randint(1, 1000)
    n2 = random.randint(1, 1000)
    return n1, n2


def soma(n1, n2):
    mais = n1 + n2
    return mais


def sub(n1, n2):
    menos = n1 - n2
    return menos


def div(n1, n2):
    divi = float(n1 / n2)
    return divi


def multi(n1, n2):
    mult = n1 * n2
    return mult


limpa_tela()
decoracao()
print('CALCULADORA')

n1, n2 = ale()

mais = soma(n1, n2)
print(f'{n1} e {n2}. A soma é {mais}')

menos = sub(n1, n2)
print(f'{n1} e {n2}. A subtração é {menos}')

divi = div(n1, n2)
print(f'{n1} e {n2}. A divisão é {divi}')

mult = multi(n1, n2)
print(f'{n1} e {n2}. A multiplicação é {mult}')