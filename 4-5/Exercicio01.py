while True:
    opcao = int(input("\n[1] Calcular area do triangulo digite\n[2] Calcular a área do retangulo\n[0]sair do programa\n"))
    if opcao == 1:
        altura = float(input("Area do triangulo: "))
        base = float(input("Area do triangulo :"))
        triangulo = (base * altura)/2
        print(f"Area do triangulo: {triangulo}")
    elif opcao == 2:
        altura = float(input("Area do retangulo: "))
        base = float(input("Area do restangulo :"))
        retangulo = base*altura
        print(f"Area do Retangulo: {retangulo}")
    elif opcao == 0:
        print("Programa finalisado!!")
        break
    else:
        print("Opção invalida")


