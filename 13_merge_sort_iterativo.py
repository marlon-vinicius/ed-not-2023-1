# Variáveis de estatísticas
divs = juncs = comps = 0

def merge_sort(lista):
    """
        Função que implementa o algoritmo Merge Sort de forma ITERATIVA
    """

    global divs, juncs, comps

    # Inicia com o menor tamanho de partição de 2^0 = 1
    tam_part = 1
    n = len(lista)
    
    # O tamanho da sublista cresce em potências de 2
    while (tam_part < n):
        # Inicia sempre pela esquerda
        esq = 0
        while (esq < n):
            dir = min(esq + (tam_part * 2 - 1), n - 1)
            meio = (esq + dir) // 2

            # print(f"esq: {esq}, dir: {dir}, meio: {meio}")

            # A mescla final deve considerar sublistas
            # não mescladas se o tamannho da lista original
            # não for potência de 2
            comps +=1
            if (tam_part > n // 2):
                meio = dir  - (n % tam_part)
            
            tam_esq = meio - esq + 1
            tam_dir = dir - meio
            lista_esq = [0] * tam_esq   # Vetor auxiliar
            lista_dir = [0] * tam_dir   # Vetor auxiliar
            for pos_esq in range(0, tam_esq):
                lista_esq[pos_esq] = lista[esq + pos_esq]
            for pos_esq in range(0, tam_dir):
                lista_dir[pos_esq] = lista[meio + pos_esq + 1]

            pos_esq, pos_dir, i = 0, 0, esq
            while pos_esq < tam_esq and pos_dir < tam_dir:
                comps += 1
                if lista_esq[pos_esq] > lista_dir[pos_dir]:
                    lista[i] = lista_dir[pos_dir]
                    pos_dir += 1
                else:
                    lista[i] = lista_esq[pos_esq]
                    pos_esq += 1
                i += 1

            while pos_esq < tam_esq:
                lista[i] = lista_esq[pos_esq]
                pos_esq += 1
                i += 1

            while pos_dir < tam_dir:
                lista[i] = lista_dir[pos_dir]
                pos_dir += 1
                i += 1

            esq += tam_part * 2
            juncs += 1
        # Incrementa a sublista em potências de 2
        tam_part *= 2
        divs += 1
    return lista

#####################################################################

 # nums = [7, 3, 6, 8, 1, 4, 9, 0, 5, 2]

# divs = juncs = comps = 0    # Reseta as variáveis de estatísticas
# print("Lista original:", nums)
# nums_ord = merge_sort(nums)
# print("Lista ordenada:", nums_ord)
# print(f"Divisões: {divs}, junções: {juncs}, comparações: {comps}")

#####################################################################

from time import time
import sys
import tracemalloc
sys.dont_write_bytecode = True      # Impede a criação do cache

from data.emp100mil import empresas

divs = juncs = comps = 0

tracemalloc.start()		# Inicia a medição de memória
hora_ini = time()
resultado = merge_sort(empresas)
hora_fim = time()

# Captura as informações de gasto de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print("Nomes ordenados: ", resultado)
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"Divisões: {divs}, junções: {juncs}, comparações: {comps}")