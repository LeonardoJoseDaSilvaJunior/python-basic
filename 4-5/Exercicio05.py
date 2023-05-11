macas = int(input("Insira a quantidade de maças: "))
total = macas*1.30 if macas < 12 else macas*1
print(f"\nQuantidade de maças: {macas}\nPreço: R$ {total:.2f}")