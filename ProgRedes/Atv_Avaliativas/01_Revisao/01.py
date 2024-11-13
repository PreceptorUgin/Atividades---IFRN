import sys

def obterEndereco():
    try:
        ipAddr = str(input("Insira o endereço de rede: "))
        lstOct = ipAddr.split('.')

        if len(lstOct) != 4 or not all(octeto.isdigit() and 0 <= int(octeto) <= 255 for octeto in lstOct):
            sys.exit("Endereço IP inválido.")
        
        return [int(octeto) for octeto in lstOct]
    
    except Exception as e:
        sys.exit(f"Erro ao inserir o endereço IP: {e}")

def obterMascaras(mask_count):
    lst_mask = []
    for n in range(1, mask_count):
        try:
            mask = int(input(f"Digite a {n}ª máscara (CIDR entre 1 e 31): "))
            if mask < 1 or mask > 31:
                print("Valor inválido. Insira uma máscara CIDR entre 1 e 31.")
            else:
                lst_mask.append(mask)
        except ValueError:
            print("Entrada inválida. Insira um número inteiro para a máscara.")
    return lst_mask

def transforme(ipAddr):
    binMini = ''.join(f'{octeto:08b}' for octeto in ipAddr)
    decimal = int(binMini, 2)
    return decimal

# Programa Principal
try:
    ip_addr = obterEndereco()
    nMask = int(input("Insira o número de máscaras que serão usadas no cálculo: "))
    lstMask = obterMascaras(nMask+1)

except Exception as e:
    sys.exit(f"Ocorreu um erro: {e}")

ip_decimal = transforme(ip_addr)

