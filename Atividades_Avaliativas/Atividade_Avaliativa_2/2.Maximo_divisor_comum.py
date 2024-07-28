import sys
num_1 = input('Insira o primeiro número: ')
num_2 = input('Insira o segundo número: ')

mdc = 0

if not str(num_1).isnumeric() or not str(num_2).isnumeric():
    sys.exit('Insira numeros validos.')
elif int(num_1) < 0 or int(num_2) < 0:
    sys.exit('Insira números positivos.')
elif num_1 == 0:
    mdc = num_2
elif num_2 == 0:
    md = num_1

