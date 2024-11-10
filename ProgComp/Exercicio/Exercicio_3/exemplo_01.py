import os

# Obtendo o diretorio onde os arquivos estão
dirArquivos = os.path.abspath(__file__)
dirArquivos = os.path.dirname(dirArquivos)

# --------------------------------------------------------------------------------------------------------------------------------------------
# Abrindo o arquivo no modo somente leitura
arqEntrada = open(dirArquivos + '\\lista_uf_capitais_populacao.txt','r', encoding='utf-8')
lstUF = list()
cabecalhos = arqEntrada.readline()[:-1]
cabecalhos = cabecalhos.split(';')

while True:
    # Lendo o conteúdo do arquivo
    linha = arqEntrada.readline()
    if linha[-1:] == '\n': linha = linha[:-1]
    # Interrompendo a leitura quando chegar ao final do arquivo
    if not linha: break
    # Adicionando a linha lida a uma lista
    lstUF.append(linha.split(';'))
# Fechando o arquivo
arqEntrada.close()
# --------------------------------------------------------------------------------------------------------------------------------------------
'''
*Repetição
lstPop = []
for v in lstUF:
    lstPop.append([v[1],v[0],int(v[2])])

*List Compreension
lstPop = [[v[1],v[0],int(v[2])] for v in lstUF]
'''
#Usando map()
lstPop = list(map(lambda v: [v[1],v[0],int(v[2])], lstUF))

#Ordenando lstPop
lstPop.sort(key = lambda v: v[2], reverse = True)

arqSaida = open(dirArquivos + '\\populacao_2022.txt','w', encoding='utf-8')
arqSaida.write(f'{cabecalhos[1]};{cabecalhos[0]};{cabecalhos[2]}\n')

for v in lstPop:
    arqSaida.write(f'{v[0]};{v[1]};{v[2]}\n')

arqSaida.close()
# Exibindo os dados lidos
print()
