import requests, sys
from datetime import date
strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata' 
strURL += '/Moedas?$top=100&$format=json' 
try: 
    dictMoedas = requests.get(strURL).json()
except:
    sys.exit(f'{sys.exc_info()[0]}')

anoHoje = (date.today()).year
codeMoeda = [c ['simbolo'] for c in dictMoedas['value']]

while True:
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
    
    strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
    strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
    strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
    strURL += f'@moeda=%27{moedEntr}%27&@dataInicial=%2701-01-{anoEntr}%27&'
    strURL += f'@dataFinalCotacao=%2712-31-{anoEntr}%27&$top=100&$format=json'
    
    try:
        dictCotacoes = requests.get(strURL).json()
    except:
        sys.exit(f'{sys.exc_info()[0]}')
    
    dictCotacoesCompra = [t ['cotacaoCompra'] for t in dictCotacoes['value']]
    dictCotacoesVenda = [t ['cotacaoVenda'] for t in dictCotacoes['value']]
    
    dictMeses = {}
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    for m in meses:
        for i in len(dictCotacoes['value']):
            if (dictCotacoes['value'][i]['tipoBoletim']) == 'Fechamento':
                if (dictCotacoes['value'][i]['dataHoraCotacao'][6:7]) == str(i):
                    mediaCompra = 0
                    mediaVenda = 0
                    