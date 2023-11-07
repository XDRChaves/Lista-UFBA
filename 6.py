clientes = []

while True:
    nome = input("Digite o nome completo do cliente (ou 'fim' para encerrar): ")
    if nome == 'fim':
        break
    rg = input("Digite o RG do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    cliente = {
        'Nome': nome,
        'RG': rg,
        'CPF': cpf,
        'Telefone': telefone
    }
    
    clientes.append(cliente)

for cliente in clientes:
    print(f"Nome: {cliente['Nome']}, RG: {cliente['RG']}, CPF: {cliente['CPF']}, Telefone: {cliente['Telefone']}")
