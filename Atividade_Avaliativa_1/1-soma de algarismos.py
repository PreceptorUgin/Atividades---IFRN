import sys

num = int(input('Insira um número de ate 4 digitos: '))

if num > 9999 or num < 0:
    print('O número inserido é inválido')
    sys.exit()

soma = 0
det_0 = num
soma = soma + (det_0 % 10)
det_0 = det_0 // 10
soma = soma + (det_0 % 10)
det_0 = det_0 // 10
soma = soma + (det_0 % 10)
det_0 = det_0 // 10
soma = soma + (det_0 % 10)

print (f'a soma dos algorismos do número {num} é: {soma}')