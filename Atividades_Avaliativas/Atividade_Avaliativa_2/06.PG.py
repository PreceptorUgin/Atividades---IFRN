import sys

#Declaração de variaveis.
val_ini = int(input('Insira um número: '))
r_pg = float(input('Insira a razão da PG: '))
elem_pg = int(input('Insira o número de elementos dessa PG: '))
no_pg = int(input('Insira o valor de uma posição desejada nessa PG: '))

fin_no_pg = val_ini*(r_pg**(no_pg-1))
aux = val_ini
som = val_ini
clas = ''

#Tratamento dos input's
if int(r_pg) == 0:
    sys.exit('O número 0 não é permitido como a razão de uma PG.')
elif elem_pg < 0:
    sys.exit('O número de elementos deve ser positivo')
elif no_pg < 0:
     sys.exit('A posição não pode receber números negativos.')
else:
     print(50*'-')
     print(val_ini)

#Calculador.
for i in range(int(elem_pg)):
        aux *= r_pg
        som += aux
        print(aux)

#Teste da classificação.
if r_pg == 1:
    clas = 'Constante.'
elif r_pg > 1 and val_ini > 0:
    clas = 'Crescente.'
elif r_pg > 1 and val_ini < 0:
    clas = 'Decrescente.'
else:
    clas = 'Oscilante.'

#Saida.
print(f'A PG é {clas}\nA soma dos seus elementos é, {som}\nO {no_pg}ºN dessa PG é, {fin_no_pg}')