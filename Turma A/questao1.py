"""
    1) Identifique o algoritmo abaixo.
    2) Registre em comentário o propósito de cada uma das variáveis (de v a z).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""
# 1) 
# O algoritmo abaixo é um SELECTION SORT

# 2)
# z - Função (selection sort)
# y - Lista
# x - Contador de posição que caminha no loop for
# w - Posição do menor valor
# v - Contador de posição que caminha no loop for interno

# 3)
# No if, dentro do laço for interno(linha 23), a segunda comparação está sendo feita na posição x, ela deve
# ser feita na posição w(linha 24).
def z(y):
    for x in range(len(y) - 1):
        w = x + 1
        for v in range(x + 2, len(y)):
            #if y[v] < y[x]:  #ERRO#
            if y[v] < y[w]: #CORREÇÃO#
                w = v
        if y[w] < y[x]:
            y[x], y[w] = y[w], y[x]



# TESTE
# y = [9, 0, 1, 8, 3, 7, 5, 6, 4, 2]
# print("ANTES:", y)
# z(y)
# print("DEPOIS:", y)