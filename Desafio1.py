# Declaração Variáveis
tot = 0

for i in range(1000):
    n1 = ""

    # Pega o valor inverso de i e adiciona à variável n1
    for j in range(len(str(i)) - 1, -1, -1):
        n1 += str(i)[j]

    # Requisitos do desafio
    if str(i)[0] != "0" or n1[0] != "0":
        if (i + int(n1)) % 2 != 0:
            if i + int(n1) < 1000000:
                print(i)
                tot += 1


print(f'Existem {tot}  números reversíveis abaixo de 1000')