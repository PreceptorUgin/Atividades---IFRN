#Declaração de variavel.
som = 0
aux_1 = 0 
aux_2 = 1

#Inicio do codigo.
for i in range(1, 1000001):
    #Verificador.
    if (i%2) == 0 or (i%5) == 0:
        #Reset de variaveis.
        som = 0
        aux_2 = i
        #Confirmador.
        while aux_2 > 0:
            aux_1 = aux_2 % 10
            som += aux_1**5
            aux_2 = aux_2//10
        #Teste/Saida.
        if i == som:
            print(som)