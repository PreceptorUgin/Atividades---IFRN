import sys

lstMask = []
try:
    ipAddr = str(input("Insira o endereço de rede: "))
    nMask = int(input("Insira o numero de mascaras que serao usadas no calculo: "))
except Exception as e:
    sys.exit(f"Erro {e}")
    raise

lstOct = ipAddr.split('.')
if len(lstOct) != 4:
    sys.exit('Endereço IP invalido.')

lstOct = [int(i) for i in lstOct]

for n in range(1, nMask+1):
    try:
        Masks = int(input(f"Digite a {n}º mascara(CIDR): "))
    except Exception as e:
        sys.exit(f"Erro {e}")
        raise

    if Masks >= 32 or Masks <= 0:
        n -= 1
        print('Valor inserido invalido, insira valores entre 1 e 31')
    else:
        lstMask.append(Masks)

print(lstMask, lstOct)