'''
    Escreva um programa que solicite um valor n inteiro e positivo 
    e que calcula a seguinte soma:  

    S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

    O programa deve escrever cada termo gerado e o valor final 
    de S.
'''
import sys

num = int(input('infomre um número: '))

if num <= 0:
    print('Número invalido, insira um número maior que 0')
    sys.exit()

som = 0
for div in range(1,num+1):
    term = 1/div
    som += 1/div

    print(f'termo {div}= 1/{div} = {term}')

print(f'A soma é {som}')
