min_ = int(input("Insira quantos minutos permaneceu no estacionamento: "))

hor = min_ // 60
if min_ % 60 > 0:
    hor = hor + 1

val_tot = 0

if hor <= 2:
    val_tot = hor * 8
elif hor <= 4:
    val_tot = 16 + (hor - 2) * 5
elif hor <= 12:
    val_tot = 26 + (hor - 4) * 3
else:
    val_tot = 30

print(f"Valor a pagar: R${val_tot:.2f}")