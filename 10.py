gabarito = input("Digite o gabarito da prova com 20 questões: ")
alunos = []

for i in range(50):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    respostas = input(f"Digite as respostas do aluno {i + 1}: ")
    acertos = sum(1 for a, g in zip(respostas, gabarito) if a == g)
    nota_final = acertos * 0.5
    resultado = "APROVADO" if nota_final >= 6 else "REPROVADO"
    alunos.append((nome, nota_final, resultado))

for nome, nota_final, resultado in alunos:
    print(f"Nome: {nome}, Nota Final: {nota_final}, Resultado: {resultado}")
