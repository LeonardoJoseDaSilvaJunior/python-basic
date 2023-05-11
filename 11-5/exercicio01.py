
def cadastro(produto,quantidade,preco):
    return produto,quantidade*preco
nome,total = cadastro("limonada",3,50)
print(f"O produto {nome}, custa R$ {total}")
