n = int(input("insira o tamanho do vetor: "))
a = []
b = []
c = []
for i in range (n):
    a.append(float(input("insira um numero ")))
    b.append(float(input("insira um numero ")))
for y in range (n):
    c.append(a[i]+b[i])
    print("{0} + {1} = {2}".format(a[y],b[y],c[y]))
print(c)
