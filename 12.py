a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
n = int(input("Digite o tamanho da lista: "))
lista = []

for i in range(n):
    numero = float(input(f"Digite o {i + 1}º número real: "))
    lista.append(numero)

contagem = sum(1 for num in lista if a <= num <= b)

print(f"Quantidade de elementos no intervalo [{a}, {b}]: {contagem}")
