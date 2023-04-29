from lib.deque import Deque

deque = Deque()

# Deque se comportanto como fila comum
deque.insert_back('Antero')
deque.insert_back('Olentina')
deque.insert_back('Glaudencio')
deque.insert_back('Hildebrando')
deque.insert_back('Iranildes')

print(deque)

removido_frente = deque.remove_front()
print(f"Removido da frente: {removido_frente}")
print(deque)

deque.insert_back('Turibio')
print(deque)

primeiro = deque.peek_front()
print(f"Primeiro da fila: {primeiro}")
print(deque)

# USANDO RECURSOS EXCLUSIVOS DO DEQUE

# Inserção prioritária
deque.insert_front('Emerenciana')
print(deque)

# Desistencia da fila
desistente = deque.remove_back()
print(f"Desistente: {desistente}")

# Nova inserção prioritária
deque.insert_front('Deusdete')
print(deque)

# Consultando a última pessoa da fila
ultimo = deque.peek_back()
print(f"Último: {ultimo}")
print(deque)