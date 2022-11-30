# > ESTRUTURAS CONDICIONAIS
# : = então
idade = 20

if idade >= 18:
    print('você é maior de idade.')   
else: 
        print('você é menor de idade.')


"""
    imagine que queira imprimmir "Aprovado(a)", caso o estudante tenha uma média
    superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7
"""
"""
elif = else if
"""

"""media = float(input('informe a media do estudante: '))
if media >= 7:
    print('Você foi provado(a)')
elif media >= 5:
    print('Recuperação')
else:
    print('Você foi Reprovado(a)')"""


media = 10
presenca = 100
if media >= 7 and presenca >= 70:
    print('Aprovado(a)')
    print('Parabéns')
else:
    print('Reprovado(a)')
    print('Tente novamente')


