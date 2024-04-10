dia_inicial = int(input("Dia inicial: "))
mes_inicial = int(input("Mês inicial: "))
dia_final = int(input("Dia final: "))
mes_final = int(input("Mês final: "))

if (mes_inicial < mes_final) or (mes_inicial == mes_final and dia_inicial <= dia_final):
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dias_decorridos_inicial = sum(dias_por_mes[:mes_inicial]) + dia_inicial
    dias_decorridos_final = sum(dias_por_mes[:mes_final]) + dia_final
    dias_passados = dias_decorridos_final - dias_decorridos_inicial
    print("Dias decorridos entre as datas:", dias_passados, "dias")
else:
    print("A data inicial é maior que a data final.")