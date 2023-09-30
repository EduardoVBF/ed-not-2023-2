"""
    1) Identifique o algoritmo abaixo.
    2) Registre em comentário o propósito de cada uma das variáveis (de a a f).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""    
# 1) 
# O algoritmo abaixo é uma BUSCA BINÁRIA

# 2)
# a - Função (busca binaria)
# b - Lista
# c - Valor buscado
# d - Início da lista
# e - Fim da lista
# f - Meio da lista

# 3)
# O erro está no primeiro if (linha 25), ao igualar o e com o f, pois quando valor buscado(c) é igual ao meio da
# lista (b[f]), retorna o meio (f) como resposta(linha 26).
def a(b, c):
    d = 0
    e = len(b) - 1
    while d <= e: 
        f = (d + e) // 2
        #if c == b[f]: e = f       #ERRO#
        if c == b[f]: return f     #CORREÇÃO#
        elif c < b[f]: e = f - 1
        else: d = f + 1
    return -1

# TESTE
b = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 47]
print(b)
pos= a(b, 23)
print(f"Valor encontrado na posição {pos}")