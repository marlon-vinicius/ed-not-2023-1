from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()
print(lista)

# Insere o primeiro elemento
lista.insert(0,"Macarrão")
print(lista)

# Insere no fim
lista.insert(1, "Molho de tomate")
print(lista)

# Insere em uma posição intermediária
lista.insert(1, "Óleo de soja")
print(lista)

# Insere no inicio usando o método de atalho
lista.insert_back("Queijo ralado")

# Insere no início usando método de atalho
lista.insert_front("Carne moída")

# Mais uma inserção em posição intermediária
lista.insert(3, "Sal")
print(lista)