'''
    Escreva um programa que calcule a seguinte soma :  

    soma = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
'''

import sys

num = int(input('Informe um número.'))

if num <= 0:
    print('Número invalido, insira um número maior que 0')
    sys.exit()

som = 0
dividendo = 1

for divisor in range(1, 51):
    som += (dividendo/divisor)
    dividendo += 2

print(som)
