# Declaração Variáveis
numeros = []
resultados = []
listaTemp = []
total = 0
flag = True

# Valida erro input na variável numero
while(flag):
    try:
        numero = int(input("Informe um número: "))
        flag = False
    except:
        print("ERRO. Informe um valor inteiro")
flag = True

for i in range(3):
    # Valida erro input do novo recurso da lista numeros
    while(flag):
        try:
            numeros.append(int(input("Informe o número " + str(i+1) + ": ")))
            flag = False
        except:
            print("Erro. Informe um valor inteiro")
    flag = True

# Analisa se somar cada unidade da lista resulta no número informado pelo usuário
for i in range(3):
    total = 0
    listaTemp = []
    for j in range(numero):
        total += numeros[i]
        listaTemp.append(numeros[i])
        if(total == numero):
            resultados.append(listaTemp)
            break


print(numero)
for i in range(len(resultados)):
    print(resultados[i])