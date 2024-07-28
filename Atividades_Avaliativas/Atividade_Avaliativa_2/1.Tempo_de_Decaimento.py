import sys
mas_ini = str(input('Insira o valor de massa inicial(em gramas): '))

if not mas_ini.replace('.','').isdigit():
    sys.exit('Insira um numero valido.')

mas_ini = float(mas_ini)
mas_fin = mas_ini
temp_sec = 0
temp_min = 0
temp_hor = 0

while mas_fin > 0.49:
    mas_fin = mas_fin/2
    temp_sec += 50

while temp_sec >= 60:
    temp_sec -= 60
    temp_min += 1
    if temp_min >= 60:
        temp_min -= 60
        temp_hor += 1

print(f'Massa inicial: {mas_ini}, massa final: {mas_fin}, tempo decorrido: {temp_hor}:{temp_min}:{temp_sec}')