# Declaração Variáveis
tempoChegada = []
totAlunos= 0
flag = True

# Valida erro input na variável minAlunos
while(flag):
    try:
        minAlunos = int(input("Informe o limite de alunos presentes: "))
        flag = False
    except:
        print("Erro. Informe um valor inteiro")
flag = True

for i in range(5):
    # Valida erro input do novo recurso da lista tempoChegada
    while(flag):
        try:
            tempoChegada.append(int(input("Informe o tempo de chegada do aluno " + str(i+1) + ": ")))
            flag = False
        except:
            print("Erro. Informe um valor inteiro")
    flag = True

# Verifica quantos foram os alunos exatos e aplica o valor à variável totAlunos
for i in range(len(tempoChegada)):
    if(tempoChegada[i] <= 0):
        totAlunos += 1


if(totAlunos >= minAlunos):
    print("Aula Normal")
else:
    print("Cancelada")