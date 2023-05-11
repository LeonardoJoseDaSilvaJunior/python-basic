firstNumber = float(input("Insert the first number: "))
while True:
    secondNumber = float(input("Insert the second nummber: "))
    if (secondNumber == 0):
        continue;
    else:
        break
total = firstNumber/secondNumber
print(total)