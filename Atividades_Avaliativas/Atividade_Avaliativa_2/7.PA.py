import sys

val_ini = int(input('Insira um número: '))
r_pa = float(input('Insira a razão da PA: '))
elem_pa = int(input('Insira o número de elementos dessa PA: '))
no_pa = int(input('Insira o valor de uma posição desejada nessa PG: '))

fin_no_pa = val_ini + ((no_pa-1)*r_pa)
aux = val_ini
som = val_ini
clas = ''

if elem_pa < 0:
    sys.exit('O número de elementos deve ser positivo')
else:
     print(50*'-')
     print(val_ini)

for i in range(int(elem_pa)):
        aux += r_pa
        som += aux
        print(aux)

if r_pa == 0:
    clas = 'Constante.'
elif r_pa > 0:
    clas = 'Crescente.'
else:
    clas = 'Decrescente.'

print(f'A PA é {clas}\nA soma dos seus elementos é, {som}\nO {no_pa}ºN dessa PA é, {fin_no_pa}')