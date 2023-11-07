numeros = []
for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número real: "))
    numeros.append(numero)

media = sum(numeros) / len(numeros)
maior = max(numeros)
menor = min(numeros)
positivos = sum(1 for num in numeros if num > 0)
negativos = sum(1 for num in numeros if num < 0)

print(f"Média dos elementos: {media}")
print(f"Maior elemento: {maior}")
print(f"Menor elemento: {menor}")
print(f"Quantidade de elementos positivos: {positivos}")
print(f"Quantidade de elementos negativos: {negativos}")
