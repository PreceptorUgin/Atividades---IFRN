'''
    Fazer um programa que solicite um número e calcule o seu fatorial

    ATENÇÃO: Lembre-se das restrições para se calcular o fatorial
             de um número
'''
import sys

num = int(input("Insira um número: "))

if num < 0 :
    print('Número invalido, Insira um número maior que zero.')
    sys.exit()

fat = num

for i in range(num-1,1,-1):
    fat *= i

print(f'O fatorial do número {num} é {fat}')
