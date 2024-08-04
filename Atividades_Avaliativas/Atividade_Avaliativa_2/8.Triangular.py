import sys

#Variaveis.
num = int(input('Insira um numero inteiro positivo: '))
n = 0
aux = 0

#Ecessão para números negativos.
if num < 0:
    print(50*'-')
    sys.exit('Insira um numero positivo.')

#Inicio
while True:
    #Teste
    aux = (n * (n + 1)) // 2
    #Verificador
    if aux == num:
        print(50*'-')
        print(f'O número {num} é triangular.')
        break
    elif aux >num:
        print(50*'-')
        print(f'O número {num} não é triangular')
        break
    else:
        n += 1