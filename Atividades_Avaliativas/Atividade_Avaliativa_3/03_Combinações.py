import  random, sys

lstSize = int(input('Insira o tamanho da lista: '))
lstVal = set() 

if lstSize < 7 or lstSize > 60:
    sys.exit('Insira um número entre 7 e 60.')

while len(lstVal) < lstSize:
    aux = random.randint(1, 61)
    lstVal.add(aux)

