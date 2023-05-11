from library.functions import *
validacao = "s"
while validacao in "Ss":

    add_produto = input("Insira o seu produto: ")
    add_preco = float(input("Insira o preco do produto: "))
    produto_Preco(add_produto,add_preco)
    validacao = input("Deseja adcionar mais itens? digite [S] se deseja continuar: ")

print(list_produto)
print(list_preco)