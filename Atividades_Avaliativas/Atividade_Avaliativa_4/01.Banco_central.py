import requests, sys
from datetime import date

try: 
    strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata' 
    strURL += '/Moedas?$top=100&$format=json' 
 
    dictMoedas = requests.get(strURL).json()
except:
        sys.exit(f'{sys.exc_info()[0]}')

anoHoje = (date.today()).year
codeMoeda = [c ['simbolo'] for c in dictMoedas['value']] 
while True:
    print(f"\n{'-'*10} Moedas validas {'-'*10}")
    for i in range(len(codeMoeda)):
        print(f'|{codeMoeda[i]}')
    try:
        moedEntr = str(input('Insira o codigo da moeda desejada: ')).upper()
        anoEntr = int(input('Insira o ano desejado para analise: '))
    except:
        sys.exit(f'{sys.exc_info()[0]}')

    if anoEntr > anoHoje:
        sys.exit('erro na entrada: Ano invalido.')
    if moedEntr not in codeMoeda:
        sys.exit('erro na entrada: Moeda invalida.')
        
    try:
        strURL  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/' 
        strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=' 
        strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?' 
        strURL += f'@moeda=%27{moedEntr}%27&@dataInicial=%2701-01-{anoEntr}%27&' 
        strURL += f'@dataFinalCotacao=%2712-31-{anoEntr}%27&$top=100&$format=json' 
    except:
        sys.exit(f'{sys.exc_info()[0]}')
        
    dictCotacoes = requests.get(strURL).json()
    dictCotacoesCompra = [t ['cotacaoCompra'] for t in dictCotacoes['value']]
    dictCotacoesVenda = [t ['cotacaoVenda'] for t in dictCotacoes['value']]
    try:
        mediaCompra = sum(dictCotacoesCompra)/len(dictCotacoesCompra)
        mediaVenda = sum(dictCotacoesVenda)/len(dictCotacoesVenda)
    except:
        sys.exit(f'{sys.exc_info()[0]}')

    for i in range(len(dictCotacoes['value'])):
        if (dictCotacoes['value'][i]['tipoBoletim']) == 'Fechamento':
            if (dictCotacoes['value'][i]['dataHoraCotacao'][6:7]) == str(i):

    dCotacaoMeses = {'Janeiro': {'mediaCompra': ,'mediaVenda': },
                    'Fevereiro': {'mediaCompra': ,'mediaVenda': },
                    'Março': {'mediaCompra': ,'mediaVenda': },
                    'Abril': {'mediaCompra': ,'mediaVenda': },
                    'Maio': {'mediaCompra': ,'mediaVenda': },
                    'Junho': {'mediaCompra': ,'mediaVenda': },
                    'Julho': {'mediaCompra': ,'mediaVenda': },
                    'Agosto': {'mediaCompra': ,'mediaVenda': },
                    'Setembro': {'mediaCompra': ,'mediaVenda': },
                    'Outubro': {'mediaCompra': ,'mediaVenda': },
                    'Novembro': {'mediaCompra': ,'mediaVenda': },
                    'Dezembro': {'mediaCompra': ,'mediaVenda': }}
    print(mediaVenda, mediaCompra)
