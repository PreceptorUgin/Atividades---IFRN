'''
    Faça um programa que solicite um número inteiro e 
    exiba a seguinte saída (no exemplo o valor informado foi 4):

    0
    0 1
    0 1 2
    0 1 2 3
    0 1 2 3 4
    0 1 2 3
    0 1 2
    0 1
    0

    ATENÇÃO: A saída vai sempre iniciar em 0 
'''
import sys

num = int(input('Digite um número inteiro positivo: '))

if num < 0:
    print('Insira um número positivo.')
    sys.exit()

for lin in range(num + 1):
    for col in range(lin + 1):
        print(col, end=' ')
    print()

for lin in range(num - 1, -1, -1):
    for col in range(lin + 1):
        print(col, end=' ')
    print()