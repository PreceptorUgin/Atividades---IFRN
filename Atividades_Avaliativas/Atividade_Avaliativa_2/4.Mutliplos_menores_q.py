#Declaração de variavel.
mult = 0
som = 0
aux_1 = 0 
aux_2 = 0

for i in range(1, 1000000):
    som = 0
    if (i%2) == 0 or (i%5) == 0:
        while aux_2 > 0:
            aux_2 = i
            aux_1 = aux_2 % 10
            som += aux_1**5
            aux_2 = aux_2//10
            print((aux_1),(aux_2),(som))
        if i == som:
            print((i))

