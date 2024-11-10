import sys, random

lstSize = int(input("Tamanho da lista: "))
lstVal = [random.randint(0, 100) for _ in range(lstSize)]

if lstSize < 1:
    sys.exit('Insira um número maior que 0.')

media = sum(lstVal)/lstSize

if lstSize%2 == 0:
    ind = round(lstSize/2)
    val1 = lstVal[ind]
    val2 = lstVal[ind-1]
    medi = (val1+val2)/2
else:
    index = lstSize/2
    medi = lstVal[round(index)-1]

somaQuadr = sum((i - media) ** 2 for i in lstVal)
varPop = somaQuadr / lstSize

desvio = varPop**2

print(f'\nLista de valores: {lstVal}\nMedia dos valores: {media}\nMadiana: {medi}\nVariância populacional: {round(varPop, 1)}\nDesvio-padrão populacional: {round(desvio, 1)}')