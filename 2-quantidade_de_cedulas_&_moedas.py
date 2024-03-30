import sys

val = float(input('Insira uma valor decimal positivo: '))

#Varieaveis das cedulas.
cedula_100, cedula_50, cedula_20, cedula_10, cedula_5, cedula_2 = 0, 0, 0, 0, 0, 0

#Variaveis das moedas.
moeda_1, moeda_50, moeda_25, moeda_10, moeda_05, moeda_01 = 0, 0, 0, 0, 0, 0

if val < 0 :
    print('Valor inserido invalido')
    sys.exit()

val = round(val, 2)
#Cedulas
cedula_100 = int(val // 100)
val = val % 100

cedula_50 = int(val // 50)
val = val % 50
    
cedula_20 = int(val // 20)
val = val % 20
    
cedula_10 = int(val // 10)
val = val % 10
    
cedula_5 = int(val // 5)
val = val % 5
    
cedula_2 = int(val // 2)
val = val % 2

print(f'Existem, ') 
print(f'   {cedula_100} cedulas de R$ 100,00')
print(f'   {cedula_50} cedulas de R$ 50,00')
print(f'   {cedula_20} cedulas de R$ 20,00')
print(f'   {cedula_10} cedulas de R$ 10,00')
print(f'   {cedula_5} cedulas de R$ 5,00')
print(f'   {cedula_2} cedulas de R$ 2,00')
    
#Moedas
moeda_1 = int(val // 1)
val = val % 1

moeda_50 = int(val // 0.50)
val = val % 0.50

moeda_25 = int(val // 0.25)
val = val % 0.25
    
moeda_10 = int(val // 0.10)
val = val % 0.10 

moeda_05 = int(val // 0.05)
val = val % 0.05

moeda_01 = round(val * 100)

print (50*'-')
print(f'e, {moeda_1} moedas de R$ 1,00')
print(f'   {moeda_50} moedas de R$ 0,50')
print(f'   {moeda_25} moedas de R$ 0,25')
print(f'   {moeda_10} moedas de R$ 0,10')
print(f'   {moeda_05} moedas de R$ 0,5')
print(f'   {moeda_01} moedas de R$ 0,1')
