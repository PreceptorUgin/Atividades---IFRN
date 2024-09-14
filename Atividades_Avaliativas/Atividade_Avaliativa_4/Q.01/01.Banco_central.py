import requests, sys, json, os
from datetime import date

dirArqu = os.path.abspath(__file__)
dirArqu = os.path.dirname(dirArqu)

strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata' 
strURL += '/Moedas?$top=100&$format=json' 
try: 
    dictMoedas = requests.get(strURL).json()
except Exception as ex:
    sys.exit(f'Erro ao buscar moedas: {type(ex).__name__}')

anoHoje = (date.today()).year
codeMoeda = [c['simbolo'] for c in dictMoedas['value']]

while True:
    for i in range(len(codeMoeda)):
        print(f'|{codeMoeda[i]}')
    try:
        moedEntr = str(input('Insira o codigo da moeda desejada: ')).upper()
        anoEntr = int(input('Insira o ano desejado para analise: '))
    except ValueError as ex:
        sys.exit(f'Erro na entrada de dados: {type(ex).__name__}')
    
    if anoEntr > anoHoje:
        sys.exit('Erro na entrada: Ano invalido.')
    if moedEntr not in codeMoeda:
        sys.exit('Erro na entrada: Moeda invalida.')
    
    strURL  =  'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
    strURL +=  'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
    strURL +=  '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
    strURL += f'@moeda=%27{moedEntr}%27&@dataInicial=%2701-01-{anoEntr}%27&'
    strURL += f'@dataFinalCotacao=%2712-31-{anoEntr}%27&$top=100&$format=json'
    
    try:
        dictCotacoes = requests.get(strURL).json()
    except Exception as ex:
        sys.exit(f'Erro ao buscar cotacoes: {type(ex).__name__}')
    
    dictCotacoesCompra = [t['cotacaoCompra'] for t in dictCotacoes['value']]
    dictCotacoesVenda = [t['cotacaoVenda'] for t in dictCotacoes['value']]
    
    dictMeses = {}
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    for mes in range(1, 13):
        mediaCompra = 0
        mediaVenda = 0
        divi = 0
        for cotacao in dictCotacoes['value']:
            mesCotacao = int(cotacao['dataHoraCotacao'][5:7])
            if mesCotacao == mes and cotacao['tipoBoletim'] == 'Fechamento':
                mediaCompra += cotacao['cotacaoCompra']
                mediaVenda += cotacao['cotacaoVenda']
                divi += 1
        if divi > 0:
            mediaCompra /= divi
            mediaVenda /= divi
        dictMeses[meses[mes-1]] = {'mediaCompra': round(mediaCompra, 5), 
                                   'mediaVenda': round(mediaVenda, 5)}
    auxArq = json.dumps(dictMeses, indent=2 , ensure_ascii=False)
    arqSaida = open(dirArqu + f'\\medias_cotacoes_{moedEntr}_{anoEntr}.json','w', encoding='utf-8')
    arqSaida.write(auxArq)
    arqSaida.close()
    print('\nArquivos salvos com sucesso!\n')