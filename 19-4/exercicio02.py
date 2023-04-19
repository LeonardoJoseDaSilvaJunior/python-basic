listaNomes = []
quantidade_alunos = int(input("insira a quantidade de alunos: "))

for i in range (0,quantidade_alunos):
    listaNomes.append(input("Insira o nome do alunos: "))
print(" ")
for x in range (quantidade_alunos):

    print(listaNomes[x] ," Posição :" , x)