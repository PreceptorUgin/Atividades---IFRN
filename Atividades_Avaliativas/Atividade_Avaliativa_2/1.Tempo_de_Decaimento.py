import sys
mas_ini = int(input('Insira o valor de massa inicial(em gramas): '))

if not str(mas_ini).replace('.','').isdigit():
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

print(50*'-')
print(f'Massa inicial: {mas_ini},\nMassa final: {mas_fin},\nTempo decorrido: {temp_hor}:{temp_min}:{temp_sec}')