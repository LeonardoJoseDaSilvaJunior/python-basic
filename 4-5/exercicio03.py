while True:
    n = float(input("Primeiro numero: "))
    n2 = float(input("Segundo numero: "))
    print(f"{n} | {n2}") if n > n2 else print(f"{n2} | {n}")
    operacao = int(input("Digite [1] para fazer novamente: "))
    if operacao != 1:
        break