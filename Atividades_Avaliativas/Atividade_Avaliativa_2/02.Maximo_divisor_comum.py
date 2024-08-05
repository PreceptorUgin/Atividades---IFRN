import sys

#Declaração de variaveis.
num_1 = int(input('Insira o primeiro número: '))
num_2 = int(input('Insira o segundo número: '))

nu_1 = num_1
nu_2 = num_2
mdc = 0
num_aux = 0

#Checagem dos input's.
if not str(num_1).isnumeric() or not str(num_2).isnumeric():
    sys.exit('Insira numeros validos.')
elif num_1 < 0 or num_2 < 0:
    sys.exit('Insira números positivos.')

#Algoritimo euclidiano.
while True:
    if num_1 == 0:
        mdc = num_2
        break
    elif num_2 == 0:
        mdc = num_1
        break

    num_aux = num_1 % num_2
    num_1 = num_2
    num_2 = num_aux

print(50*'-')
print(f'Máximo Divisor Comum(MDC) entre, {nu_1} é {nu_2}, séra {mdc}')