# > DICIONÁRIOS

#Criando dicionários

dicionario = {}
dicionario = dict()# a função "dict" cria um dicionário vazio por padrão

dicionario = { 'nome' : 'Leonardo', 'idade': 26, 'altura': 1.70 }

print(dicionario)
print(dicionario['idade'])


# Adicionar elementos em um dicionário

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 2

print(dicionario)


# Iterando sobre o dicionário

for chave in dicionario:
    print(chave, dicionario[chave] )

# testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)
