# > LISTAS

# ANTES
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com listas
notas = [7.9, 9.7, 8.2]

# Criando listas
lista = []
lista = list()
lista = [26, 'Leonardo', 3,14159, False]
lista_de_listas = [10,[1, 2, 3]]


# Indexação e slices (fatiamento)

lista = [10, 'Leonardo', 3.14159, True]

print (lista[0])
print (lista[1])
print (lista[2])
print (lista[3])

# -1 = ultimo elemento da lista, -2 penultimo e etc..
print(lista[-1])

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]
# começa no índice 0 e vai até(:) o menor que 3
print(lista[0:3])
print(lista[3:6])
print(lista[3:]) # Caso o termino não seja definido, ele irá até o final
print(lista[2:6:2]) # Caso acrescente mais um número ele será utilizado para pular os índices nesse caso 30 e 25


# > Interações com for

# 1. Utilizando os proprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os índices

print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(lista[i])


# > MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

# append: adiciona  elementos no final da lista

print('Antes do append: ', lista)

lista.append(3)

print('depois do append: ', lista)

# insert: Você escolhe qual o elemento e a posição desejada

lista.insert(2, 10) # 2 é o índice/local no qual eu quero adicionar o elemento e o 10 é o elemento

print('depois do Insert: ', lista)


# extend: adciona elementos da lista no final da lista primaria 

lista2 = [1, 2, 3]

lista.extend(lista2)
print('depois do extend: ', lista)# Ele concatena as listas


# pop: Remove o lemento que vc expecificar e caso n expecifique, ele removerá o ultimo elemento 

lista.pop()

print('lista após o pop: ', lista)# ultimo número eliminado

lista.pop(0)
print('lista após o pop: ', lista)# Removeu o elemento do índice 0

# remove: remove um elemento expecífico(independe da posição)

lista.remove(3)

print('depois do remove: ', lista)# Ele remove o primeiro número que ele encontrar (da esquerda pra direita)

# count: conta quantas vezes um elemento se repete na lista

print('quantidade de 2 na lista: ', lista.count(2))

# index: Mostra o Índice/posição do elemento expecificado

print('Índice do elemento 12: ', lista.index(12))

# sort: ordena a lista, de forma crescente ou decrescente

lista.sort()# Crescente
print('Ordem crescente: ',lista)
lista.sort(reverse=True)# Decrescente
print('Ordem decrescente: ',lista)

# Funções para listas

# len: Mostra a quantidade de elementos na lista

print('Quantidade de elementos exitentes na lista:', len(lista))

# sum:  soma

print('Soma de todos os dados da lista: ', sum(lista))

# max: maior valor da lista

print('Maior elemento da lista: ', max(lista))

# min : menor valor da lista
print('Menor elemento da lista: ', min(lista))
