"""
fazer um programa que solicite varios valores numericos,
é a cada valor inserido ele o adicione a uma lista,
que só para de receber os numeros quando 0 for inserido 
é então devera retornar como saida:
quantos numeros foram inseridos,
qual a soma dos valores digitados
é a media aritimetica
é exibira por fim, a lista ordenada de forma crescente.
"""

#declaração de variaveis.
val_at = 1
val_memo = list()

#Input dinamico ate 0 ser digitado.
while val_at != 0:
    val_at = int(input('Insira um numero: '))
    if not str(val_at).replace('-','').isdigit():
        print('insira um numero valido')
    elif val_at == 0:
        print('')
    else:
        val_memo.append(val_at)

#reposicionar para ordem crescente.
val_memo.sort()

print(f'O número de caracteres é: {len(val_memo)}, A soma de todos os caracteres é: {sum(val_memo)}, A media é:{sum(val_memo)/len(val_memo)}, A seuqencia ordenada é: {val_memo}')
