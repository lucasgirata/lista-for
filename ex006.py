
numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
dentroDoIntervalo = 0
foraDoIntervalo = 0

for i in range(10):
    numeros[i] = int(input("Insira um número: "))

    if 10 <= numeros[i] <= 20:
        dentroDoIntervalo += 1
    else:
        foraDoIntervalo += 1

print(numeros)
print(f"Números dentro do intervalo de 10 a 20: {dentroDoIntervalo}")
print(f"Números fora do intervalo de 10 a 20: {foraDoIntervalo}")