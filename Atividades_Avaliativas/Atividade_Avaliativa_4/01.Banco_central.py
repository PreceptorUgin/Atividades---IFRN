import requests, sys
from datetime import date
 
strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata' 
strURL += '/Moedas?$top=100&$format=json' 
 
dictMoedas = requests.get(strURL).json() 
 
strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/' 
strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=' 
strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?' 
strURL += '@moeda=%27USD%27&@dataInicial=%2701-01-2023%27&' 
strURL += '@dataFinalCotacao=%2712-31-2023%27&$top=100&$format=json' 
 
dictCotacoes = requests.get(strURL).json()

print ('\n')
anoEntr = int(input('Insira o ano desejado para analise: '))
anoHoje = (date.today()).year
if anoEntr > anoHoje:
    sys.exit('erro na entrada.')

moedEntr = str(input('Insira a moeda desejada: '))
count = 0
for i in range(len(dictMoedas['value'])):
    if moedEntr == (dictMoedas['value'][i]['simbolo']):
       count += 1

if count == 0:
    sys.exit('Moeda não encontrada no banco de dados.')
