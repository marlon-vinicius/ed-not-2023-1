"""
    ALGORITMO DE BUSCA BINÁRIA
    Dada um lista, que deve estar PREVIAMENTE ORDENADA,
    e um valor de busca, divide a lista em duas metades
    procurando pelo valor de busca apenas na metade onde
    o valor poderia estar. Novas subdivisões são feitas
    até que se encontre o valor de busca ou que reste
    apenas uma sublista vazia, quando então se conclui
    que o valor de busca não existe na lista.
"""
comps = 0     # Conta o número de comparações
def busca_binaria(lista, val):
    ini = 0               # Inicio da lista
    fim = len(lista) - 1  # Fim da lista

    while ini <= fim:
        meio = (ini + fim) // 2  # Divisão inteira

        # O valor de busca for encontrado.
        # Retorna a posição
        if lista[meio] == val:
            comps += 1
            return meio

        elif val < lista[meio]:
            comps +=2
            fim = meio - 1

        else: # val > lista[meio]:
            comps = +2
            ini = meio + 1
        
    return -1  # Valor não existe na lista