A = []
M = []
for x in range (10):
    A.append(float(input("insira o numero: ")))
x = float(input("Insira o multiplicador : "))
for i in range(0,10):
    M.append(A[i]*x)
print(M,end=" ")