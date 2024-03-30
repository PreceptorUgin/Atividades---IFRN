from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys

sexo = input("Informe o sexo (masculino/feminino): ")
dat_nasc = input("Informe a data de nascimento (DD/MM/AAAA): ")
dat_ini_contr = input("Informe a data de início da contribuição (DD/MM/AAAA): ")

dat_nasc = datetime.strptime(dat_nasc, "%d/%m/%Y")
dat_ini_contr = datetime.strptime(dat_ini_contr, "%d/%m/%Y")

if sexo.lower() != "masculino" and sexo.lower() != "feminino":
    print("Sexo inválido.")
    sys.exit()
elif sexo.lower() == "masculino":
    id_apose = dat_nasc + relativedelta(years=65)
    temp_contr_min = 35
elif sexo.lower() == "feminino":
    id_apose = dat_nasc + relativedelta(years=62)
    temp_contr_min = 30

apose_contr = dat_ini_contr + relativedelta(years=temp_contr_min)

dat_apose = max(id_apose, apose_contr)

print("Data de aposentadoria:", dat_apose.strftime("%d/%m/%Y"))
