remake = "y"
while remake == "y":
    while True:
        n1 = float(input("Insira a primeria nota (0 a 10): "))
        if n1 >= 0 and n1 <=10: break
    while True:
        n2 = float(input("Insira a segunda nota (0 a 10): "))
        if n2 >= 0 and n2 <=10: break
    media = (n1 + n2) / 2
    print(f"Sua media foi {media}")
    remake = input("redo calculation? [Y] yes [N] no")
    while remake != "y" and remake != "Y" and remake != "n" and remake != "N":
        print("insert an corrcet letter [Y] or [n]")
        remake = input("redo calculation? [Y] yes [N] no")
else: print("End")