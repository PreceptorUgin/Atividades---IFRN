import math
import sys

a = float(input('Insira o comprimento do lado(a) de um triângulo: '))
b = float(input('Insira o comprimento do lado(b) de um triângulo: '))
c = float(input('Insira o comprimento do lado(c) de um triângulo: '))

#Verificador:
if a + b < c or a + c < b or b + c < a:
    print ('Não e triângulo.')
    sys.exit()

#Calculo de ângulos
ang_1 = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
ang_2 = math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))
ang_3 = 180 - ang_1 - ang_2
#A soma dos ângulos tem que dar 180 graus, me deixa.
print('O triângulo possui os respectivos lados: ')
print(f'{round(ang_1, 2)}°')
print(f'{round(ang_2, 2)}°')
print(f'{round(ang_3, 2)}°')
print(70*'-')

#Comparador de tamanhos:
if a == b and b == c:
    print('Triângulo Equilatero,')
elif a == b or b == c or a == c:
    print('Triângulo Isósceles,')
else:
    print('Triângulo Escaleno,')

#Comparador de ângulos:
if ang_1 > 90 or ang_2 > 90 or ang_3 > 90:
    print('Ângulo obtuso.')
elif ang_1 == 90 or ang_2 == 90 or ang_3 == 90:
    print('Ângulo retângular.')
else:
    print('Ângulo agudo.')
