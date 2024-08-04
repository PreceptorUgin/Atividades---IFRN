import sys
#Declaração de variaveis.
val = int(input('Informe um numéro positivo: '))
val_aux = val
cont = 0

#verificador.
if val < 0:
    sys.exit('Insira um numero positivo.')

#Contador de digitos>
while val_aux > 0:
    cont += 1
    val_aux //= 10

#Saida
print(50*'-')
print(f'O número de digitos em {val}, é {cont}')