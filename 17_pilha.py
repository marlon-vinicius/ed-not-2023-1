"""
    Programa simples que inverte uma palavra e verifica se ela
    é um PALÍNDROMO, uma palavra que pode ser lida de trás para 
    a frente, assim com da frente para trás.
    Para isso, usaremos uma estrutura de pilha baseada em uma
    lista do Python.
"""

palavra = input('Informe a palavra a ser verificada:')

pilha = []     # Lista vazia que será usada como pilha

# 1) Pega cada letra da palavra e insere no final (topo) da pilha
for letra in palavra:
    pilha.append(letra)
    print(pilha)

print('*' * 50)

inverso = ""

# 2) Vamos retirar as letras da pilha, uma a uma, DO FIM PARA O INÍCIO.
# A operação se repete enquanto a pilha não estiver vazia.
# Cada letra retirada é acrescentada à variável inverso.
while len(pilha) > 0:
    letra = pilha.pop()     # Retira o último elemento da pilha
    inverso += letra        # Acrescenta a letra ao inverso
    print(f"Pilha: {pilha}; inverso {inverso}")

print('*' * 50)

print("Palvra original: ", palavra)
print("palavra invertida: ",inverso)

if palavra == inverso:
    print("*** É UM PALÍNDROMO ***")
else:
    print("--- não é um palíndromo ---")