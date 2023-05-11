A = []
count = 0
for i in range(10):
    A.append(float(input(f"insira o {i+1}º numero: ")))
n = float(input("insira o numero que está procurando: "))
for x in range (10):
    if A[x] == n:
        count += 1
print(count)

