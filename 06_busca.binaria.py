comps = 0

def busca_binaria(lista, val):
    """
    ALGORITMO DE BUSCA BINÁRIA
    Dados uma lista, que deve estar PREVIAMENTE ORDENADA,
    e um vaor de busca, divide a lista em duas partes,
    procurando pelo valor de busca apenas na metade onde
    o valor poderia estar. Novas subdivisões são feitas
    até que se encontre o valor de busca ou que reste
    apenas uma sublista vazia, quando então se conclui
    que o valor de busca não existe na lista.
    """
    global comps #Use a variável comps do escopo global
    comps = 0

    ini = 0  #inicio da lista
    fim = len(lista) -1   #fim da lista

    while ini <= fim:
        #calculando o meio da lista
        meio = (ini + fim)//2 #divisão inteira

        # Verifica se o valor que está no meio da lista
        # é igual ao valor de busca. Em caso afirmativo,
        # retornamos a posição do meio, pois o valor de
        # busca foi encontrado.
        if val == lista[meio]:
            comps += 1
            return meio
        
        # Senão, se o valor de busca é MENOR do que o valor 
        # do meio, reinicia a busca na metade esquerda da lista
        elif val < lista[meio]:
            comps += 2
            fim = meio-1

        # Por fim, se o valor de busca é MAIOR que o valor
        # do meio, reinicia a busca na metade da direita da (sub)lista.
        else:
            comps += 2
            ini = meio+1

        # SE chegarmos até este ponto, o valor de busca NAO EXISTE na lista
    return -1

#################################33

# Para a busca binparia, a lista PRECISA estar ordenada
nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 47]

print(nums)

pos11 = busca_binaria(nums, 11)
print(f"valor 11 encontrado na posiçao {pos11}")

pos41 = busca_binaria(nums, 41)
print(f"valor 11 encontrado na posiçao {pos41}")

pos8 = busca_binaria(nums, 8)
print(f"valor 11 encontrado na posiçao {pos8}")

print("-" *40)

#Fazendo a busca em um arquivo do 1M+ nomes

#importando a lista de nomes
import sys
sys.dont_write_bytecode = True #impede criação da cache

from data.nomes import nomes
from time import time

# Buscando o nome EDSON PEREIRA
hora_ini = time()
pos1 = busca_binaria(nomes, 'EDSON PEREIRA')
hora_fim = time()
print(f"EDSON PEREIRA encontrado na posição {pos1}, comparações: {comps}")
print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n')

# Buscando o nome MARIA FERREIRA
hora_ini = time()
pos2 = busca_binaria(nomes, 'MARIA FERREIRA')
hora_fim = time()
print(f"MARIA FERREIRA encontrada na posição {pos2}, comparações: {comps}")
print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n')

# Buscando o nome VALDIR SILVA
hora_ini = time()
pos3 = busca_binaria(nomes, 'VALDIR SILVA')
hora_fim = time()
print(f"VALDIR SILVA encontrado na posição {pos3}, comparações: {comps}")
print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n')

# Buscando o nome GILCICLEIDE GARCIA
hora_ini = time()
pos4 = busca_binaria(nomes, 'GILCICLEIDE GARCIA')
hora_fim = time()
print(f"GILCICLEIDE GARCIA encontrada na posição {pos4}, comparações: {comps}")
print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n')
