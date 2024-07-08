'''
    Fazer um programa que solicite um número e calcule o seu fatorial

    ATENÇÃO: Lembre-se das restrições para se calcular o fatorial
             de um número
'''
import sys

num = int(input("Insira um número: "))

if num < 0 :
    sys.exit()

count = num
fat = 1

while count > 1:
    fat = fat * count
    count -= 1

print(f'O fatorial do número {num} é {fat}')
