num = int(input('Digite a quantidade de fatores primos: '))
qnt = int(input('Digite o número de números consecutivos: '))

cont = 0
aux = 2
temp = aux
f_prim = 0

while cont < qnt:
    temp = aux
    f_prim = 0

    while (temp % 2) == 0:
        f_prim += 1
        temp //= 2
    fator = 3

    while (fator * fator) <= temp:
        while (temp % fator) == 0:
            f_prim += 1
            temp //= fator
        fator += 2

    if temp > 1:  
        f_prim += 1

    if f_prim == num:
        print(aux)
    
    aux += 1

print(f'Os primeiros {qnt} números consecutivos com exatamente {num} fatores primos são: {cont}')