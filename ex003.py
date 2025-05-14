
num = int(input("Insira um valor inteiro de 1 a 10: "))
i = 0

if 1 <= num <= 10:
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

else:
    print("Erro! Tente novamente mais tarde.")