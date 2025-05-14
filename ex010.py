vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
contador = [0] * 8

qntdRepeticaomaior = 0
numMaisRepetido = 0

for i in range(10):
    k = vetor[i]
    contador[k] += 1

for i in range(8):
    if contador[i] > qntdRepeticaomaior:
        qntdRepeticaomaior = contador[i]
        numMaisRepetido = i

print(f"Números do vetor: {vetor}")
print(f"Contador de repetições em ordem de 0 a 7: {contador}")
print(f"Número que mais se repete: {numMaisRepetido}")