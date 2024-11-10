cond = ''
lst_alu = list()

while True:
    if cond == 'n':
        break
    else:
        matr = str(input('Insira a matricula: '))
        nom = str(input('Nome completo: '))
        ida = int(input('Insira sua idade: '))
        lst_alu.append([matr, nom, ida])
        while True:
            cond = input('Cadrastar novo aluo?(s/n): ').lower()
            if cond == 's':
                break
            elif cond == 'n':
                break
            else :
                print('insira uma resposta valida.')

lst_alu.sort(key=lambda aluno:aluno[1])
print(lst_alu)
