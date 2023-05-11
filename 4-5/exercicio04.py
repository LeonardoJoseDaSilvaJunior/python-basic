inicio = int(input("Insira o horario de inicio: "))
fim    = int(input("Insira o horario de termino: "))
pos = 24-(inicio - fim)
durante =  resultado = fim - inicio
resultado = pos if fim <= inicio else  durante
print(resultado)
