# Lista de números
nums = [9, 21, 33, 12, 0, 18, 24, 30, 15, 6, 3, 27]

"""
    Função que realiza um busca sequencial em uma lista
    procurnado por val.
    Se val for encontrado, retorna a posição de val.
    Caso contrário, retorna o vlaor -1
"""
def busca_sequencial(lista, val):
    for pos in range(len(lista)):
        # Encontrou val; retorna a posição onde foi encontrado
        if val == lista[pos]: return pos
    # Percorreu a toda a lista e não encontrou val: retorna -1
    return -1

#####################################################################

# TESTES

# Procurando o valor 15
resultado = busca_sequencial(nums, 15)
print(f"Posição do valor 15 na lista: {resultado}")

# Procurando o valor 20
resultado = busca_sequencial(nums, 20)
print(f"Posição do valor 20 na lista: {resultado}")

# Procurando o valor 33
resultado = busca_sequencial(nums, 33)
print(f"Posição do valor 33 na lista: {resultado}")

# TESTES COM NOMES

import sys
sys.dont_write_bytecode = True   # Impede a criação do cache
from time import time

from data.lista_nomes import nomes

# Busca pelo nome MARLON
hora_ini = time()
resultado = busca_sequencial(nomes, "MARLON")
hora_fim = time()
print(f"Posição do nome MARLON na lista: {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000} ms")

# Busca pelo nome CARLOS

hora_ini = time()
resultado = busca_sequencial(nomes, "CARLOS")
hora_fim = time()
print(f"Posição do nome CARLOS na lista: {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000} ms")

# Busca pelo nome YARA

hora_ini = time()
resultado = busca_sequencial(nomes, "YARA")
hora_fim = time()
print(f"Posição do nome YARA na lista: {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000} ms")

# Busca pelo nome ORKUTILSON

hora_ini = time()
resultado = busca_sequencial(nomes, "ORKUTILSON")
hora_fim = time()
print(f"Posição do nome ORKUTILSON na lista: {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000} ms")