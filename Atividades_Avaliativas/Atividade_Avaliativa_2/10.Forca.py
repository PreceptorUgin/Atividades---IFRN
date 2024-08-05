#Declaração de Variaveis/Palavra chave.
p_chave = 'CHAVE'
entr = ''
cont = 0

#Forca.
while True:
    entr = str(input(': '))
    if entr == p_chave:
        print(50*'-')
        print('CERTA RESPOSTA!')
        break
    else:
        for i in range(len(p_chave)):
            if entr[i] == p_chave:
                print(50*'-')
                print(f'Letra certa {entr[i]} em {i}')

    #Limite de Tentativas.
    if cont == 6:
        print('Tentativas esgotadas.')
        break
    else:
        cont += 1