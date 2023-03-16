"""
    ALGORITMO DE ORDENAÇÃO MERGE SORT

    No processo de ordenação, esse algoritmo "desmonta"
    a lista original, contendo N elementos, até obter N
    listas ocm apenas um elemento cada uma. Em seguida,
    usando a técnica de mesclagem (merge), "remonta" a 
    lista, dessa vez com os elementos já em ordem.
"""

# Variáveis de estatística
divs = juncs = comps = 0

def merge_sort(lista):

    global divs, juncs, comps
    
    # Para que possa haver divisão da lista, esta
    # deve ter mais de um elemento
    if len(lista) > 1:

        # Encontra a posição do meio da lista, para
        # fazer a divisão em duas metades
        meio = len(lista) // 2

        # Tira uma cópia da primeira metade da lista
        sublista_esq = lista[:meio]
        # Tira uma cópia da segunda metade da lista
        sublista_dir = lista[:meio]
        divs += 1   # Número de divisões

        # Chamamos recursividade a função para que ela
        # continue repartindo cada umas das sublistas em 
        # duas partes menores
        sublista_esq = merge_sort(sublista_esq)
        sublista_dir = merge_sort(sublista_dir)

        # AQUI COMEÇA A MESCLAGEM ORDENADA DAS DUAS SUBLISTAS
        pos_esq = pos_dir = 0
        ordenada = []   # Lista vazia

        # Compara os elementos das sublistas entre si e insere
        # na lista ordenada o menor dentre dois elementos
        while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
            # O menor elemento está na sublista da esquerda
            comps += 1    # Número de comparações
            if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
                # "Desce" o elemento da esquerda para a lista ordenada
                ordenada.append(sublista_esq[pos_esq])
                pos_esq   # Incrementa pos_esq
            # O menor elemento stá na sublista da direita
            else:
                # Desce o elemento da direita para a sublista ordenada
                ordenada.append(sublista_dir[pos_dir])
                pos_dir += 1 # Incrementa pos_dir

        # Verificação da sobra
        sobra = []   # Lista vazia

        # Sobra à esquerda
        if(pos_esq < pos_dir) : sobra = sublista_esq[pos_esq:]
        # Sobra à direita
        else: sobra = sublista_dir[pos_dir:]

        juncs += 1    # Número de junções 

        # O resultado final é a junção (concatenação)
        # da lista ordenada com a sobra
        return ordenada + sobra

    else:
        return lista

#######################################################################

# Teste com vetor de 10 números

nums = [6, 4, 2, 0, 9, 5, 1, 8, 3, 7]

# Reseta as variáveis de estatística
divs = juncs = comps = 0
resultado = merge_sort(nums)
print("Lista original:", nums)
print("Lista ordenada:", resultado)
print(f"Divisões: {divs}, junções: {juncs}, comparações: {comps}")