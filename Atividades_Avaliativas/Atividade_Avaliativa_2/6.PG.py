import sys

val_ini = int(input('Insira um número: '))
r_pg = float(input('Insira a razão da P.G.: '))
elem_pg = int(input('Insira o número de elementos dessa P.G.: '))
no_pg = int(input('Insira o valor de uma posição desejada nessa PG: '))

fin_no_pg = val_ini*(r_pg**(no_pg-1))
aux = val_ini
som = val_ini
clas = ''

if int(r_pg) == 0:
    sys.exit('O número 0 não é permitido como a razão.')
elif elem_pg < 0:
    sys.exit('O número de elementos deve ser positivo')
else:
     print(50*'-')
     print(val_ini)

for i in range(int(elem_pg)):
        aux *= r_pg
        som += aux
        print(aux)

if r_pg == 1:
    clas = 'Constante.'
elif r_pg > 1 and val_ini > 0:
    clas = 'Crescente.'
elif r_pg > 1 and val_ini < 0:
    clas = 'Decrescente.'
else:
    clas = 'Oscilante.'

print(f'A PG é {clas}')
print(f'O {no_pg}ºN dessa PG é, {fin_no_pg}')