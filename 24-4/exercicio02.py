lista_Alunos = ["Leo","Almir","Maykuel","Johnson","Messias"]
notas = []
media = 0
acimaMedia = 0
for x in range (len(lista_Alunos)):
    notas.append(float(input(f"Insira a nota de '{lista_Alunos[x]}': ")))
    media += notas[x]
media = media / len(notas)

for x in range (5):
    if notas[x] >= media:
        acimaMedia+=1

print(f"Media da turma {media}\nQuantidade de alunos acima da media: {acimaMedia}")
