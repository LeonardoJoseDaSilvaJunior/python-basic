listaNomes = []
quantidade_alunos = int(input("insira a quantidade de alunos: "))

for i in range (0,quantidade_alunos):
    listaNomes.append(input("Insira o nome do alunos: "))
for x in range (quantidade_alunos):
    print(listaNomes[x] ," Posição :" , x)
    
nome = input("insira o nome do aluno: ")
print("\nLISTA DE ALUNOS\n")
for x in range(quantidade_alunos):
    if listaNomes[x] == nome:
        print(listaNomes[x], " Posição :", x)

