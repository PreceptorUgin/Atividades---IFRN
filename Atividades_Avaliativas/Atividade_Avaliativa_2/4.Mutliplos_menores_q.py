#Declaração de variavel.
som = 0
aux_1 = 0 
aux_2 = 1

for i in range(1, 1000001):
    if (i%2) == 0 or (i%5) == 0:
        som = 0
        aux_2 = i
        while aux_2 > 0:
            aux_1 = aux_2 % 10
            som += aux_1**5
            aux_2 = aux_2//10
        if i == som:
            print(som)