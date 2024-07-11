'''
    Faça um programa que exiba a Sequência de Fibonacci. 
    O programa deverá solicitar um número que será a quantidade
    de elementos da Sequência de Fibonacci.

    ATENÇÃO: Considere que a Sequência de Fibonacci irá iniciar em 1 
'''
import sys

num = int(input('Digite o número de elementos da Sequência de Fibonacci: '))

if num <= 0:
    print('Por favor, insira um número (positivo diferent que zero).')
    sys.exit()

now = 1
then = 0

for i in range(num):
    print (now, end=",")
    then, now = now, now + then
