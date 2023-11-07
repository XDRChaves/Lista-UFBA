lista = []
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    lista.append(numero)

numero_verificar = int(input("Digite um número para verificar na lista: "))

if numero_verificar in lista:
    print(f"O número {numero_verificar} está na lista.")
else:
    print(f"O número {numero_verificar} não está na lista.")
