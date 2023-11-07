import math

n = int(input("Digite o tamanho dos vetores: "))

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(n):
    elemento1 = float(input(f"Digite o elemento {i + 1} do primeiro vetor: "))
    elemento2 = float(input(f"Digite o elemento {i + 1} do segundo vetor: "))
    elemento3 = float(input(f"Digite o elemento {i + 1} do terceiro vetor: "))
    
    vetor1.append(elemento1)
    vetor2.append(elemento2)
    vetor3.append(elemento3)

norma_vetor1 = math.sqrt(sum(element**2 for element in vetor1))
norma_vetor2 = math.sqrt(sum(element**2 for element in vetor2))
norma_vetor3 = math.sqrt(sum(element**2 for element in vetor3))

maior_norma = max(norma_vetor1, norma_vetor2, norma_vetor3)

vetor_soma = [vetor1[i] + vetor2[i] + vetor3[i] for i in range(n)]

print(f"A norma do primeiro vetor é {norma_vetor1}")
print(f"A norma do segundo vetor é {norma_vetor2}")
print(f"A norma do terceiro vetor é {norma_vetor3}")
print(f"O vetor com maior norma é: {'Primeiro' if maior_norma == norma_vetor1 else 'Segundo' if maior_norma == norma_vetor2 else 'Terceiro'}")
print(f"Vetor soma dos três vetores: {vetor_soma}")
