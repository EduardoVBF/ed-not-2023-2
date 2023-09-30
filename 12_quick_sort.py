def quick_sort(lista, ini = 0, fim = None):
    """
    ALGORITMO DE ORDENAÇÃO QUICK SORTgit 

    Escolhe um dos elementos da lista para ser o pivô (na nossa implementação, será o último elemento) e, na
    primeira passada, divide a lista, a partir da posição final do pivô, em um sublista à esquerda, contendo
    apenas valores menores que o pivô, e outra sublista à direita, que contém apenas valores maiores que o pivô.
    Em seguida, recursivamente, repete o processo em cada uma das sublistas, até que toda a lista esteja ordenada.
    """

    # Quando não soubermos o valor da variável "fim", atribuímos a ela o valor da última posição da lista.
    if fim is None: fim = len(lista) -1

    print(f"ini = {ini}, fim = {fim}")

    # Para que o algoritmo trabalhe, é necessário que a faixa delimitada pelas variáveis "ini" e "fim" tenham,
    # pelo menos, dois elementos. Caso contrário, saímos da função sem fazer nada.

    if fim <= ini: return
    
    # Inicialização das variáveis
    pivot = fim
    div = ini - 1

    # Percorre a lista da posição "ini" até a posição "fim" - 1;
    for pos in range(ini, fim):
        # Se o elemento na posição "pos" for MENOR que o elemento da posição "pivot", executa algumas ações
        if lista[pos] < lista[pivot]:
            div += 1 # Chega o "div" uma posião para frente

            # Efetua a troca entre os elementos das posições "pos" e "div", desde que essas variáveis tenham
            # valor distinto entre si.
            if pos != div and lista[pos] < lista[div]:
                lista[pos], lista[div] = lista[div], lista[pos]

    # Depois que "pos" chega em sua posição final, "div" deve ser incrementado uma última vez
    div += 1

    # Caso os valores das posições "pivot" e "div" sejam diferentes entre si, efetua a troca mútua dos elementos
    # nessas posições, caso o primeiro seja menor que o segundo.
    if pivot != div and lista[pivot] < lista[div]:
        lista[pivot], lista[div] = lista[div], lista[pivot]

    # NESTE PONTO, O ELEMENTO DA POSIÇÃO "div" ESTÁ EM SEU LOCAL CORRETO

    # Chamamos recursivamente a função para ordenar a sublista à esquerda da posição "div"
    quick_sort(lista, ini, div -1)

    # A mesma coisa porém para a sublista à direita da "div"
    quick_sort(lista, div + 1, fim)

    #######################################################################################

    nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

    quick_sort(nums)
    print(nums)

