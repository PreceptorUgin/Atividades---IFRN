'''
    Faça um programa que exiba a Sequência de Fibonacci. 
    O programa deverá solicitar um número que será a quantidade
    de elementos da Sequência de Fibonacci.

    ATENÇÃO: Considere que a Sequência de Fibonacci irá iniciar em 1 
'''
import sys

n = int(input('Digite o número de elementos da Sequência de Fibonacci: '))

if n <= 0:
    print('Por favor, insira um número positivo maior que zero.')
    sys.exit()

n_count = n
val_fib = 0
fib1, fib2 = 0, 1

if n == 1:
    val_fib = fib1
elif n == 2:
    val_fib = fib2

while n_count > 2:
    val_fib = fib1 + fib2
    fib1 = fib2
    fib2 = val_fib
    n_count -= 1

print(f'O {n}º número da sequência de Fibonaci é {val_fib}.')