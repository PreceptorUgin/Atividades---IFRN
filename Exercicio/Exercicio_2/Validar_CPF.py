import sys

cpf = str(input('Insira seu CPF: '))

if not cpf.isnumeric():
    sys.exit('Insira apenas numeros.')
elif len(cpf) != 11:
    sys.exit('Insira onze caracteres.')

i = 0
d1 = 0
while i < len(cpf)-2:
    d1 += (int(cpf[i])*((len(cpf)-1)-i))
    i += 1
    print(d1)

d1 = d1%11
print(d1)