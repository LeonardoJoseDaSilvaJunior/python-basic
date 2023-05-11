media = 0
medias = []
repeat = " "
while repeat != "n":
    nota = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    media = (nota + nota2)/2
    medias.append(media)
    if media >= 7:
        print("Aprovado")
        print(f"Media: {media}")
    elif media >= 4:
        print("Recuperação")
    else:
        print("Reprovado")
    repeat = input("Você deseja inserir mais notas? ")

for x in medias:
    print(x)
