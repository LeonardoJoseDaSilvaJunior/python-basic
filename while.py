numero_sorteado = 15

numero_escolhido = int(input('infrome um número entre 1 e 20: '))

while numero_escolhido != numero_sorteado:
    print('Você errou o número tente novamente...')

    numero_escolhido = int(input('infrome um número entre 1 e 20: '))

print('parabéns! você acertou!')


# Exemplo 02 : Estrtutra com contador

contador = 0
while contador < 5:
    print(contador)

    contador = contador + 1
    
# Exempo 03 While-else

contador02 = 0 
while (contador02 < 5):
      print(contador02)
      contador02 = contador02 + 1
else:
      print("O loop while foi encerrado com sucesso!")


