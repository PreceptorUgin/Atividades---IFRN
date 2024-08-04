#Declaração de variaveis.
num = int(input('Insira um numero: '))
n_aux = num
aux = str(num)
cont = 0
n = 0

#Contador de digitos
while n_aux > 0:
    n_aux //= 10
    cont += 1

#Calculador
for i in range(cont):
    n += int(aux[i])**cont

#Verificador/Saida.
if n == num:
    print(f'{num}, É um número de Armstrong.')
else:
    print(f'{num}, Não e um número de Armstrong.')