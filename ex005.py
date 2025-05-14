
numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
par = 0
impar = 0

for i in range(10):
    numeros[i] = int(input("Insira um número: "))

    if numeros[i] % 2 == 0:
        par += 1
    else:
        impar += 1

print(numeros)
print(f"Números pares: {par}")
print(f"Números impares: {impar}")
