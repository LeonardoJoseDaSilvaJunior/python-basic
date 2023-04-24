numbers = []
reverse = []
for x in range (20):
    numbers.append(float(input("Insira numeros: ")))
for x in range (20-1,0,-1):
    reverse.append(numbers[x])
print(reverse)