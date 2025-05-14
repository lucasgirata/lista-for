
idades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
contador = 0

for idade in idades:
    idade = int(input("Insira a idade: "))
    contador += idade

print(f"Média das 10 idades informadas: {contador / 10}")
