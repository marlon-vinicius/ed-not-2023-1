#LISTAS EM PYTHON
#Listas são uma forma de armazenar mais de um valor
#em uma unica variável. Os valores podem ser de tipos diferentes.

#Uma lista de números
valores = [2, 3, 5, 7, 9, 11, "batata", "tomate", True]

#OPERAÇÕES SOBRE LISTAS

#1) PERCURSO: siginifica percorrer a lista do primeiro
# até o último elemento, fazendo algo com cada um
# deles. No caso a seguir, vamos exibir cada um dos
# elementos separadamentes usando print().
for val in valores:
    print(val)

print("*" * 80) #Imprime * 80 vezes

# 2) INSERÇÃO DE UM NOVO ELEMENTO NO *FIM* DA LISTA: append()
valores.append("cebola")
print(valores)

valores.append(29)
print(valores)

# 3)INSERINDO UM NOVO ELEMENTO EM UMA POSIÇÃO ESPECIFICADA: insert()
# Parâmetros:
# 1º: posição para inserir(contagem inicial em 0)
# 2º: valor a ser inserido
valores.insert(4,"chuchu") #Insere "chuchu" na 5º posição
print(valores)

valores.insert(0, "abobrinha") #Insere "abobrinha" na 1º posição
print(valores)

print ("-" * 80)

# 4)ACESSANDO UM VALOR EM UMA POSIÇÃO ESPECÍFICA
print('Elemento na SÉTIMA posição:', valores[6])
print('Elemento na TERCEIRA posição:', valores[2])
print('Elemento na PRIMEIRA posição:', valores[0])
print('Elemento na ÚLTIMA posição:', valores[-1])
print('Elemento na PENULTIMA posição:', valores[-2])

print ('-' * 80)

# 5) SUBSTITUINDO VALORES EXISTENTES
print("ANTES:", valores)

# Substituindo ovalor na posição 10
valores[10] = "cenoura"
# Substituindo o valor da posição 0
valores[0] = "beterraba"
# Substituindo o valor da ultima posição
valores[-1] = "alho"

print("DEPOIS:",valores)

# 6) DETERMINANDO QUANTOS ELEMENTOS HÁ NA LISTA: len()
print("Número de elementos na lista:", len(valores))

# Imprimindo o último elemento da lista com ajuda de len ()
print("Último valor da lista:", valores[len(valores) - 1])
print(valores)

print("-" * 80)

# 7) REMOVENDO O ÚLTIMO ELEMENTO DA LISTA: pop()
print("ANTES:")
ultimo = valores.pop()
print("Valor removido da lista:", ultimo)
print("DEPOIS:", valores)

print("-" * 80)

# 8) REMOVENDO UM ELEMENTO POR SUA POSIÇÃO: pop() com parâmetro
print("ANTES:", valores)
pos9 = valores.pop(9)     #Remove o elemento da posição 9
print("Valor removido da posição 9:", pos9)
pos0 = valores.pop(0)     #Remove o primeiro elemento(posição 0)
print("Valor removido da posição 0:", pos0)
print("DEPOIS:", valores)

print("-" * 80)

# 9)REMOVENDO UM ELEMENTO PELO SEU VALOR: remove()
print("ANTES:", valores)
valores.remove("batata")   #Remove o valor "batata"
valores.remove(5)    #Remove o vlaor 5
print("DEPOIS:", valores)

print("-" * 80)

# Acrescendo mais alguns elementos na lista
valores.append(15)
valores.append(13)
valores.append("milho")
valores.append(17)
valores.append("mandioca")
valores.append(19)

print("-" * 80)

# 10)FATIANDO UMA LISTA
print(valores)

# Cria um sublista que contém os elementos de 1 até
# a posição 7 (posição 8 não entra)
sublista2_7 = valores[2:8]
print("Sublista de 2 a 7:", sublista2_7)

# Cria uma sublista que contém os elementos do ínicio
# até a posição 5 (posição 6 não entra)
sublista0_5 = valores[6]
print("Sublista de 0 a 5:", sublista0_5)

# Cria uma sublista que contém os elementos da posição 10
# até o fim da lista
sublista10_fim = valores[10:]
print("Sublista de 10 até o final:", sublista10_fim)