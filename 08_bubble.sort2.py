comps = trocas = passd = 0

def bubble_sort(lista):
    """
    ALGORITIMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    trocando entre si dois elementos adjacentes sempre que
    o segundo for MENOR que o primeiro. Efetua tantas
    passadas quanto necessárias, até que, na última delas,
    nenhuma troca tenha sido realizada.

    ESTÁ VERSÃO TEM UMA PEQUENA OTIMIZAÇÃO QUE VAI DIMINUINDO 
    A QUANTIDADE DE COMPARAÇÕES A CADA PASSADA
    """

    # Usando as variaveis globais
    global comps, trocas, passd
    comps = trocas = passd = 0

    # Loop etrno, não sabemos de antemão quantas passadas
    # serão necessárias
    while True:
        # Inicio de uma nova passada
        passd += 1

        # Controla se houve troca na passada
        trocou = False

        # Percurso da lista, do primeiro ao PENÚLTIMO elemento
        # com acesso a cada posição NA PRIMEIRA PASSADA
        # Nas demais passadas, o percurso vai diminindo uma posição
        for pos in range(len(lista) - passd):
          
          # Se o valor que está na frente na lista (pos + 1)
          # for MENOR do que aquele que está atrás (pos),
          # faz uma TROCA
          if lista[pos + 1] < lista[pos]:
             lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
             trocou = True # Houve troca na passada
             trocas += 1

          # 0 if representa uma comparação
          comps +=1
    
        if not trocou:         # Não houve troca na passada
           break               # Interrompe o loop eterno
        
##########################################################################

nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

# Melhor caso
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 9, 9]

# Pior caso
# nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("ANTES:", nums)
bubble_sort(nums)
print("DEPOIS:", nums)
print(F"Comparações: {comps}, trocas: {trocas}, passadas: {passd}")

############################################################################
# TESTE COM O ARQUIVO DE 1M+ NOMES

# import sys
# sys.dont_write_bytecode = True #impede criação da cache

# from data.nomes_desord import nomes
# from time import time

# nomes100000 = nomes[:100000]

# hora_ini = time()
# bubble_sort (nomes100000)
# hora_fim = time()
# print(nomes100000) # Lista após ordenação
# print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n')