# > FUNÇÕES

# 1. O que são funções e por que utiliza-las?

# funções que já utilizamos anteriormente 

"""print() # - Imprime uma mensagem (int, floatn, str) no console (terminal, cmd)
input() # - Retorna um dado informado pelo úsuario (entrada padrão) e pode ser uam string
len ()  # - Recebe uma lista  e retorna o tamanho dessa lista
max()   # - Retorna o maior valor da lista"""

#2. Criação de funções

# Função inicial

from __future__ import print_function


def saudacao():
    print('Seja bem-vindo(a)')
    print('Olá, é um prazer ter você fazendo parte desse curso')

saudacao()
saudacao()
saudacao()

# Função com parâmetros

def saudacao(nome, curso):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}')

saudacao('leonardo', 'python')
saudacao('gabriela', 'php')

# Função com parâmetro default

def saudacao(nome, curso = 'python'):
    print(f'Seja bem-vendo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}')

saudacao('leonardo')


# Funções com retorno

def soma (num1, num2):
    return num1 + num2


resultado = soma(5, 7)

print('O resultado da soma é: ', resultado)


def calculadora (num1, num2, operacao = '+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(10, 20, '-')

print(resultado)