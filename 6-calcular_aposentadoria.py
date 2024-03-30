from datetime import datetime, timedelta
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
    id_apose = dat_nasc + timedelta(days=65*365)
    temp_contr_min = 35 * 365
elif sexo.lower() == "feminino":
    id_apose = dat_nasc + timedelta(days=62*365)
    temp_contr_min = 30 * 365

apose_contr = dat_ini_contr + timedelta(days=temp_contr_min)

dat_apose = max(id_apose, apose_contr)

print("Data de aposentadoria:", dat_apose.strftime("%d/%m/%Y"))
