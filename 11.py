lista = []

while True:
    codigo = int(input("Digite um código (0 para encerrar, 1 para mostrar direta, 2 para mostrar inversa): ")
    if codigo == 0:
        break
    elif codigo == 1:
        print("Lista na ordem direta:", lista)
    elif codigo == 2:
        print("Lista na ordem inversa:", lista[::-1])
    else:
        print("Código inválido.")
    
    if codigo in (1, 2):
        for i in range(15):
            numero = float(input(f"Digite o {i + 1}º número real: "))
            lista.append(numero)
