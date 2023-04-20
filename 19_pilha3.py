from lib.stack import Stack

# expr = "2 + (( 5 * ( 3 / 2 + 1) / 4 ))"
# expr = "(2 + (( 5 * ( 3 / (2 + 1) / 4 ))"
expr = "2 + (( 5 * ( 3 / 2) + 1)) / 4 ))"

print(f"EXPRESSÃO ANALISADA: {expr}")

pilha = Stack()

# Percorre a expressãp em bsuca de parênteses
for pos in range(len(expr)):
    # Empilha a posição quando é encontrado um abre parênteses
    if expr[pos] == "(":
        pilha.push(pos)
        # print(pilha)

    # Desempilha a posição do último abra parênteses empilhado
    # quando um fecha parênteses é encontrado
    elif expr[pos] == ")":
        pos_abre = pilha.pop()
        print(f"Parênteses aberto na posição {pos_abre} foi fechado na posição {pos}")
        # print(pilha)

# Verifica sobras na pilha
while not pilha.is_empty():
    pos_abre = pilha.pop()
    print(f"ERRO: Parêntese aberto na posição {pos_abre} não possui o fecha correspondente")