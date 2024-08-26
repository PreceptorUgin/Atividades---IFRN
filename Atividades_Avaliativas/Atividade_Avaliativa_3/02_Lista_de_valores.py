import sys

lstSize = int(input('Insira o tamanho da lista: '))
lstVal = []

if lstSize < 1:
    sys.exit('O tamanho da lista tem que ser maior que 0.')

while True:
    lstEntr = int(input('Insira um valor para a lista: '))
    if lstEntr == 0:
        break
    elif len(lstVal) >= lstSize:
        del lstVal[lstSize-1]
    
    lstVal.append(lstEntr)
    lstVal.sort()
    print(lstVal)

print(f'\nSua lista final é, {lstVal}')