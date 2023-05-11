vetor = []
soma = 0
acima_Media = 0
for i in range (0,10):
    vetor.append(int(input(f"insira o {i+1}° número: ")))
    soma += vetor[i]
maior = vetor [0]
menor = vetor [0]
media = soma/ 10

for x in vetor:
    if x > maior:
        maior = x
    elif x < menor:
        menor = x
    if x % 2 ==0 and x > 0:
        print(f"Numero par : {x}")
    if media < x:
        acima_Media += 1

print(f"maior = {maior} | Menor = {menor}")
print(f"Media : {soma} /10 = {media}")
print(f"Acima da Media = {acima_Media}")

