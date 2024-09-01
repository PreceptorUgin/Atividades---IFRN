from  datetime import date
anoEntr = int(input('Insira o ano desejado para analise: '))
anoHoje = (date.today()).year
if anoEntr > anoHoje:
    print('yup')