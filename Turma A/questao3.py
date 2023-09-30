"""
    1) Identifique o algoritmo abaixo.
    2) Registre em comentário o propósito de cada uma das variáveis (de a a d).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""
# 1) 
# O algoritmo abaixo é uma BUBBLE SORT

# 2)
# a - Função (bubble sort)
# b - Lista
# c - Verificador de troca
# d - Posição no laço for

# 3)
# O erro está na linha executada se o primeiro if for válido (linha 23), a variável c não deve ser usada como parâmetro de
# posição da lista, a posição correta a ser trocada com o elemento seguinte é a posição de d (linha 24).
def a(b):
    while True:
        c = False
        for d in range(len(b) - 1):
            if b[d + 1] < b[d]:
                #b[d + 1], b[c] = b[c], b[d + 1]  #ERRO#
                b[d + 1], b[d] = b[d], b[d + 1]   #CORREÇÃO
                c = True
        if not c:
            break

#TESTE
# b = [9, 0, 1, 8, 3, 7, 5, 6, 4, 2]
# print("ANTES:", b)
# a(b)
# print("DEPOIS:", b)