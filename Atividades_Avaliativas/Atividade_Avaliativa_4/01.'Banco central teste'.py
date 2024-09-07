import requests 
 
strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata' 
strURL += '/Moedas?$top=100&$format=json' 
 
dictMoedas = requests.get(strURL).json() 
 
strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/' 
strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=' 
strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?' 
strURL += '@moeda=%27USD%27&@dataInicial=%2701-01-2023%27&' 
strURL += '@dataFinalCotacao=%2712-31-2023%27&$top=100&$format=json' 
 
dictCotacoes = requests.get(strURL).json()
aux = list()



print(aux)
'''
"Teste de saida; obs.:Queria entender os arquivos com os quais eu ia trabalhar."
print(f'\n{dictMoedas}\n')
print(f'{dictCotacoes}\n')
for i in range(len(dictCotacoes['value'])):
    if (dictCotacoes['value'][i]['tipoBoletim']) == 'Fechamento':
        aux.append(dictCotacoes['value'][i]['dataHoraCotacao'][5:7])
for j in range(len(dictCotacoes['value'])):
    print(dictCotacoes['value'][j])
for i in range(len(dictMoedas['value'])):
    print(dictMoedas['value'][i])
print('\n')


'''