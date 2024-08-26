import random, sys

valInt1 = int(input('Insira o número de listas: '))
valInt2 = int(input('Insira o número de elementos das listas: '))

if valInt1 < 1 or valInt2 < 1:
    sys.exit('Insira números positivos maiores que 0.')

matrOrig = [[random.randint(1, 1001) for _ in range(valInt2)] for _ in range(valInt1)]
matrTran = [[matrOrig[i][v] for i in range(valInt1)] for v in range(valInt2)]

print(f'Matriz Original, {matrOrig}\nMatriz Transposta, {matrTran}')