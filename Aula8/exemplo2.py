import os

os.system('cls')


# Biblioteca para números aleatórios
import random

# num = random.randint(1, 10)

def ale(inicio, final, quantidade):
    
    return [random.randint(inicio,final) for _ in range(quantidade)]

inicio = int(input('Informe o primeiro valor: '))
final = int(input('Informe o final: '))
quantidade = int(input('Quantos números você quer gerar? '))

resp = ale(inicio, final, quantidade)

print(resp)