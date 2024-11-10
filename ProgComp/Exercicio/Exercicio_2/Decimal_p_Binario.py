import sys

val = str(input('Insira um valor inteiro: '))

if not val.isnumeric():
    sys.exit('Insira apenas numeros')
elif int(val) < 0:
    sys.exit('Insira um valor positivo')

val = int(val)
bi = 0
val_fin = ''

while val != 0:
    bi = val%2
    val_fin = str(bi) + val_fin
    val = val//2

print(val_fin)