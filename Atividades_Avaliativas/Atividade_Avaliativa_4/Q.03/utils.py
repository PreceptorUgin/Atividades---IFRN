import random
import os

def gerarCartelas(num):
    if not isinstance(num, int) or num <= 0 or num > 10000:
        return (False, 'Numero invalido.')

    cartelas = {}
    ids = set()
    
    def gerar_id():
        while True:
            id_c = f'cart_{random.randint(1, 10001):05d}'
            if id_c not in ids:
                ids.add(id_c)
                return id_c

    def gerar_numeros(start, end):
        return sorted(random.sample(range(start, end + 1), 5))

    while len(cartelas) < num:
        id_c = gerar_id()
        cartela = {
            'B': gerar_numeros(1, 18),
            'I': gerar_numeros(19, 36),
            'N': gerar_numeros(37, 54),
            'G': gerar_numeros(55, 72),
            'O': gerar_numeros(73, 90)
        }
        if id_c not in cartelas:
            cartelas[id_c] = cartela

    return (True, cartelas)

def salvarCartelas(cartelas, arquivo="cartelas.txt"):
    if not cartelas:
        return (False, "Nenhuma cartela.")

    try:
        with open(arquivo, 'w') as f:
            for id_c, c in cartelas.items():
                linha = f"{id_c};"
                for l, nums in c.items():
                    linha += f"{l}={' '.join(map(str, nums))};"
                f.write(linha[:-1] + "\n")
        return (True, "Arquivo salvo.")
    except Exception as e:
        return (False, f"Erro: {str(e)}")

def lerCartelas(arquivo="cartelas.txt"):
    if not os.path.isfile(arquivo):
        return (False, "Arquivo não encontrado.")

    cartelas = {}
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                partes = linha.strip().split(';')
                id_c = partes[0]
                dados = partes[1:]
                cartela = {}
                for dado in dados:
                    letra, numeros = dado[0], dado[2:]
                    cartela[letra] = list(map(int, numeros.split()))
                cartelas[id_c] = cartela
        return (True, cartelas)
    except Exception as e:
        return (False, f"Erro: {str(e)}")

def imprimirCartelas(id_c, cartelas):
    if not cartelas:
        return (False, "Nenhuma cartela.")
    if not isinstance(id_c, str) or id_c not in cartelas:
        return (False, "Número inválido.")

    cartela = cartelas[id_c]
    linha_divisoria = "+-+-+-+-+-+-+-+-+-+"
    cabecalho = "| B | I | N | G | O |"
    conteudo = [
        f"| {' '.join(f'{num:2}' for num in cartela['B'])} |",
        f"| {' '.join(f'{num:2}' for num in cartela['I'])} |",
        f"| {' '.join(f'{num:2}' for num in cartela['N'])} |",
        f"| {' '.join(f'{num:2}' for num in cartela['G'])} |",
        f"| {' '.join(f'{num:2}' for num in cartela['O'])} |"
    ]

    resultado = f"\n{linha_divisoria}\n | Cartela: {id_c} |\n{linha_divisoria}\n{cabecalho}\n{linha_divisoria}\n" + "\n".join(conteudo) + f"\n{linha_divisoria}\n"
    return (True, resultado)