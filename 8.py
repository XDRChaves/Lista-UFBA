numeros_pares = []
numeros_impares = []

while True:
    numero = int(input("Digite um número inteiro (ou '0' para encerrar): ")
    if numero == 0:
        break
    if numero % 2 == 0:
        numeros_pares.append(numero)
        if len(numeros_pares) == 5:
            print("Lista de números pares:", numeros_pares)
            numeros_pares = []
    else:
        numeros_impares.append(numero)
        if len(numeros_impares) == 5:
            print("Lista de números ímpares:", numeros_impares)
            numeros_impares = []

if len(numeros_pares) > 0:
    print("Lista de números pares:", numeros_pares)
if len(numeros_impares) > 0:
    print("Lista de números ímpares:", numeros_impares)
