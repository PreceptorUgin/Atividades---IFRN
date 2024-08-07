x = int(input('Posição X inicial: '))
y = int(input('Posição Y inicial: '))

mov = str(input('Movimentos: ')).lower()

movs = ''
valid = 0

for m in mov:
    if m == 'u':
        y += 1
        movs += m
        valid += 1
    elif m == 'd':
        y -= 1
        movs += m
        valid += 1
    elif m == 'r':
        x += 1
        movs += m
        valid += 1
    elif m == 'l':
        x -= 1
        movs += m
        valid += 1
    elif m == 'o':
        x -= 1
        y += 1
        movs += m
        valid += 1
    elif m == 'n':
        x += 1
        y += 1
        movs += m
        valid += 1
    elif m == 'e':
        x += 1
        y -= 1
        movs += m
        valid += 1
    elif m == 'w':
        x -= 1
        y -= 1
        movs += m
        valid += 1

if x > 0 and y > 0:
    quadIni = 'I'
elif x < 0 and y > 0:
    quadIni = 'II'
elif x < 0 and y < 0:
    quadIni = 'III'
elif x > 0 and y < 0:
    quadIni = 'IV'
else:
    quadIni = 'Eixo'

xFin, yFin = x, y

if xFin > 0 and yFin > 0:
    quadFin = 'I'
elif xFin < 0 and yFin > 0:
    quadFin = 'II'
elif xFin < 0 and yFin < 0:
    quadFin = 'III'
elif xFin > 0 and yFin < 0:
    quadFin = 'IV'
else:
    quadFin = 'Eixo'

print(f'Posição inicial: ({x}, {y})\nPosição final: ({x}, {y})\nMovimentos válidos: {valid}\nMovimentos: {movs}\nQuadrante inicial: {quadIni}\nQuadrante final: {quadFin}')