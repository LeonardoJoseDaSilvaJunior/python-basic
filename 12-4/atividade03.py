dentro = 0
fora = 0
for i in range (10,20):
    n = float(input("Insert a nummber: "))
    if (n>=10 and n<=20):
        dentro +=1
    else:
        fora+=1
print(f"\nnumber of values out of range:  {dentro}\nnumber of values in range : {fora}")
