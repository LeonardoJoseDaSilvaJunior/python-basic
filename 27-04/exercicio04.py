peoples = []
for x in range (5):
    peoples.append(input("insert your name: "))
print()
for person in range (5):
    print(peoples[person], end=" ")
print()
for y in range (4,-1,-1):
    print(peoples[y],end=" ")