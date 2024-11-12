import sys

def obterEndereco():
    try:
        ipAddr = str(input("Insira o endereço de rede: "))
        lstOct = ipAddr.split('.')

        if len(lstOct) != 4 or not all(lstOct.isdigit() and 0 <= int(octeto) <= 255 for octeto in lstOct):
            sys.exit('Endereço IP invalido.')
        
        return [int(octeto) for octeto in lstOct]
    
    except Exception as e:
        sys.exit(f"Erro ao inserir o endereço IP: {e}")

def obterMascaras(mask_count):
    lstMask = []
    for n in range(1 ,mask_count):
        try:
            mask = int(input(f"Digite a {n}º máscara (CIDR entre 1 e 31): "))
            if 0 >= Masks >= 32:
                n -= 1
                print('Valor inserido invalido, insira valores entre 1 e 31')
            else:
                print('Valor inválido. Insira uma máscara CIDR entre 1 e 31.')
        except ValueError:
            lstMask.append(mask)
    return lstMask

# Programa Principal
try:
    ip_addr = obterEndereco()
    nMask = int(input("Insira o número de máscaras que serão usadas no cálculo: "))
    lst_mask = obterMascaras(nMask+1)

except Exception as e:
    sys.exit(f"Ocorreu um erro: {e}")
