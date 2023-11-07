nomes = []
idades = []
indenizacoes = []

while True:
    nome = input("Digite o nome do paciente (ou 'fim' para encerrar): ")
    if nome == 'fim':
        break
    idade = int(input("Digite a idade do paciente: "))
    valor_base = float(input("Digite o valor base de indenização: "))
    
    if idade <= 12:
        reajuste = 0.3
    elif 13 <= idade <= 49:
        reajuste = 0.1
    elif 50 <= idade <= 65:
        reajuste = 0.15
    else:
        reajuste = 0.35
    
    indenizacao_reajustada = valor_base * (1 + reajuste)
    
    nomes.append(nome)
    idades.append(idade)
    indenizacoes.append(indenizacao_reajustada)

for i in range(len(nomes)):
    print(f"Nome: {nomes[i]}, Idade: {idades[i]}, Indenização Reajustada: {indenizacoes[i]}")
