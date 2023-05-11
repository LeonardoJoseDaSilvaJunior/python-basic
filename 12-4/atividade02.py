neg =0
for i in range (0,10):
  numeros = float(input("Insert any number: "))
  if(numeros<0):
      neg +=1
print(f"\namount of negative numbers: {neg}")
