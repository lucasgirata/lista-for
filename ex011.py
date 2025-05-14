
tamanhoVetores = int(input("Insira o tamanho dos vetores A e B: "))

a = [0] * tamanhoVetores
b = [0] * tamanhoVetores
c = [0] * tamanhoVetores

for i in range(tamanhoVetores):
    a[i] = int(input(f"Insira o valor da posição {i} do vetor A: "))

for i in range(tamanhoVetores):
    b[i] = int(input(f"Insira o valor da posição {i} do vetor B: "))

for i in range(tamanhoVetores):
    c[i] = a[i] + b[i]

print(f"Números do Vetor A: {a}")
print(f"Números do Vetor B: {b} ")
print(f"Soma dos Números de mesma posição dos Vetores armazenados no Vetor C: {c}")
