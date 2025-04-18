gabarito = ['A', 'C', 'B', 'A', 'E', 'D', 'D', 'C', 'A', 'A']
lista_alunos = [['Aluno 01', 'B', 'D', 'E', 'E', 'C', 'D', 'A', 'B', 'C', 'D'],
    ['Aluno 02', 'C', 'D', 'A', 'B', 'D', 'A', 'A', 'C', 'B', 'E'],
    ['Aluno 03', 'A', 'A', 'B', 'D', 'C', 'E', 'E', 'A', 'A', 'C'],
    ['Aluno 04', 'B', 'B', 'C', 'C', 'D', 'E', 'D', 'D', 'E', 'E'],
    ['Aluno 05', 'B', 'B', 'D', 'A', 'A', 'E', 'B', 'D', 'E', 'C'],
    ['Aluno 06', 'C', 'C', 'D', 'E', 'B', 'B', 'C', 'D', 'E', 'A'],
    ['Aluno 07', 'B', 'A', 'A', 'B', 'B', 'C', 'D', 'E', 'A', 'B'],
    ['Aluno 08', 'D', 'E', 'A', 'B', 'B', 'C', 'C', 'D', 'A', 'A'],
    ['Aluno 09', 'A', 'A', 'A', 'C', 'B', 'D', 'D', 'E', 'D', 'C'],
    ['Aluno 10', 'B', 'B', 'D', 'E', 'C', 'D', 'C', 'E', 'B', 'A']]

for alunos in lista_alunos:
    nomeAluno = alunos[0]
    resp = alunos[1:]
    acrts = sum(1 for resp, g in zip(resp, gabarito) if resp == g)
    alunos.append(acrts)

lista_alunos.sort(key=lambda x: x[-1], reverse=True)

print(f'Gabarito:, {gabarito}\n')

for alunos in lista_alunos:
    nomeAluno = alunos[0]
    resp = alunos[1:-1]
    acrts = alunos[-1]
    print(f'{nomeAluno}:\nRespostas: {resp}\n  Nota: {acrts} acertos\n')