import sys

mom_in_h, mom_in_m = int(input('Insira as horas e minutos da partida (separador :): ').split(':'))
mom_fin_h, mom_fin_m = int(input('Insira as horas e minutos de chegada (separador :): ').split(':'))
seg_desc = int(input('Informa quatos segundos estiveram parados (em seg): '))
lit_us = float(input('informe quantos litros foram gastos (em R$): '))
preç_comb = float(input('Informe quanto custa o litro do combustivel (em L): '))
dist_t = int(input('Informe quantos quilometros foram percorridos (em Km): '))


if mom_in_h < 0 or mom_in_h > 24 or mom_fin_h < 0 or mom_fin_h > 24:
    print('Valor invalido!')
    sys.exit()
elif mom_in_m < 0 or mom_in_m > 60 or mom_fin_m < 0 or mom_fin_m > 60:
    print('Valor invalido!')
    sys.exit()
elif seg_desc < 0 or seg_desc > 60 or lit_us < 0 or preç_comb < 0 or dist_t < 0:
    print('Valor invalido!')
    sys.exit()


temp_med = ((mom_in_h*3600) + (mom_in_m*60)) - ((mom_fin_h*3600) + (mom_fin_m*60))

cust_via = preç_comb * lit_us

vel_glo = dist_t / (temp_med / 3600)
vel_mov = dist_t / ((temp_med - seg_desc) /3600)

efi_kml = dist_t / lit_us
efi_lh = lit_us / ((temp_med - seg_desc) /3600)
efi_rskm = (lit_us * preç_comb) /dist_t

print(f'O tempo de viagem foi {temp_med}s')
print(f'A velocidade media golbal e {vel_glo}Km/h e a velocidade media em movimento e de {vel_mov}Km/h.')
print(f'Foram gastos R${cust_via} com combustivel')
print(f'O carro fez {efi_kml}Km/l, {efi_lh}L/h e {efi_rskm}R$/Km')
