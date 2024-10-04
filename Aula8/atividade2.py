import os

os.system('cls')


def multa():
    multa = excedente * M
    return multa


PP = 100
M = 4 

peso = float(input('Informe o peso do pescado: '))
excedente = peso - PP
valor = multa()

if peso > PP:
    print(f'Excendente foi ultraprassado, pescador deverá pagar {valor} reais')
    
else:
    print('Excedente não foi ultrapassado')