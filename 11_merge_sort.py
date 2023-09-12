def merge_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO MERGE SORT

    No processo de ordenação, esse algoritmo "desmonta" a lista original, contendo N elementos,
    até obter N listas com apenas 1 elemento cada uma. Em seguida, usando a técnica de 
    mesclagem (merging), "remonta" a lista, desta vez com os elementos ordenados.
    """

    # Parte1 : DIVISÃO DA LISTA ORIGINAL EM LISTAS MENORES

    #Para que possa haver divisão da lista, ela deve ter mais que 1 elemento.
    if len(lista) > 1:
        # Encontra a posição do meio da lista, para fazer a divisão ao meio
        meio = len(lista) // 2

        # Tira uma cópia da primeira metade da lista
        sublista_esq = lista[:meio]
        sublista_dir = lista[meio:]

        # Chamammos recursivamente a própria função para que ela
        # continue repartindo cada sublista em duas partes menores
        sublista_esq = merge_sort(sublista_esq)
        sublista_dir = merge_sort(sublista_dir)

        # Parte 2: REMONTAGEM DA LISTA ORDENADAMENTE

        pos_esq = pos_dir = 0
        ordenada = []  # Lista vazia

        # Compara os elementos das sublistas entre si e insere na lista ordenada
        # a menor dentre dois elementos
        while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
            # O menor elemento está na sublista da esquerda
            if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
                # "Desce" o elemento da esquerda para a lista ordenada
                ordenada.append(sublista_esq[pos_esq])
                pos_esq += 1  # Incremento a posição da esquerda

            # O menor elemento está a sublista da direita
            else:
                # "Desce" o elemento da direita para a lista ordenada
                ordenada.append(sublista_dir[pos_dir])
                pos_dir += 1  # Incremento a posição da direita

        # Verificação da sobra
        sobra = []

        # Sobra à esquerda
        if (pos_esq < pos_dir): sobra = sublista_esq[pos_esq:]
        # Sobra à direita
        else: sobra = sublista_dir[pos_dir:]

        # O resultado final é a junção (concatenação) da lista ordenada com a sobra
        return ordenada + sobra