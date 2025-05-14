texto = input("Digite um texto para saber a quantidade de vogais: ").lower()

vogais = ["a", "e", "i", "o", "u"]
contador = [0, 0, 0, 0, 0,]

for letras in texto:

    for i in range (5):

        if letras == vogais[i]:
            contador[i] += 1
print(f"Vogais encontradas no texto inserido: ")
for i in range(5):
    if contador[i] > 0:
        print(f"{vogais[i]} = {contador[i]}")
