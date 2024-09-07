import requests, sys
from datetime import date
 
strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata' 
strURL += '/Moedas?$top=100&$format=json' 
 
dictMoedas = requests.get(strURL).json() 

anoHoje = (date.today()).year
codeMoeda = [c ['simbolo'] for c in dictMoedas['value']] 
nameMoeda = [n ['nomeFormatado']for n in dictMoedas['value']]
while True:
    try:
        anoEntr = int(input('Insira o ano desejado para analise: '))
        moedEntr = str(input('Insira a moeda desejada: ')).upper()
    except:
        sys.exit(f'{sys.exc_info()[0]}')
    else:
        if anoEntr > anoHoje:
            sys.exit('erro na entrada: Ano invalido.')
        if moedEntr not in codeMoeda:
            sys.exit('erro na entrada: Moeda invalida.')
        
        strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/' 
        strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=' 
        strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?' 
        strURL += f'@moeda=%27{moedEntr}%27&@dataInicial=%2701-01-{anoEntr}%27&' 
        strURL += f'@dataFinalCotacao=%2712-31-{anoEntr}%27&$top=100&$format=json' 
 
        dictCotacoes = requests.get(strURL).json()
        dictCotacoesCompra = [t ['cotacaoCompra'] for t in dictCotacoes['value']]
        print(dictCotacoesCompra)