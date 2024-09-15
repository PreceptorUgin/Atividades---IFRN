from bingoFunc import *

def menu():
    cartelas = {}

    while True:
        print('\n1. Gerar Cartelas\n2. Salvar Cartelas\n3. Ler Cartelas\n4. Imprimir Cartelas\n5. Sair')
        mChoice = input('Escolha: ').strip()
        
        if mChoice == '1':
            nCartelas = int(input('Quantidade: '))
            sucesso, resultado = gerarCartelas(nCartelas)
            if sucesso:
                cartelas = resultado
                print(f'Geradas: {len(cartelas)}')
            else:
                print(f'Erro: {resultado}')

        elif mChoice == '2':
            sucesso, mensagem = salvarCartelas(cartelas)
            print(mensagem)
        elif mChoice == '3':
            sucesso, resultado = lerCartelas()
            if sucesso:
                cartelas = resultado
                print('Lidas.')
            else:
                print(f'Erro: {resultado}')

        elif mChoice == '4':
            if not cartelas:
                print('Nenhuma cartela.')
                continue
            id_c = input('Número da cartela: ').strip()
            sucesso, resultado = imprimirCartelas(id_c, cartelas)
            if sucesso:
                print(f'Cartela {id_c}:\n{resultado}')
            else:
                print(f'Erro: {resultado}')

        elif mChoice == '5':
            print('Saindo...')
            break
        else:
            print('Opção inválida.')

if __name__ == '__main__':
    menu()