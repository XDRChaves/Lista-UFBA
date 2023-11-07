numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

pares = sum(1 for num in numeros if num % 2 == 0)

print(f"Quantidade de números pares na lista: {pares}")
