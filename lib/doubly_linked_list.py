"""
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    Trata-se de uma lista linear, em que que seus elementos
    (chamados nodos ou nós) não estão fisicamente adjacentes
    uns dos outros, mas ligados logicamente por ponteiros que
    indicam o nodo anterior e o proximo nodo de sequência.
    Não possui restrições de acesso - inserções, exclusões e 
    consultas podem ser realizadas em qualquer posição da
    lista
"""
class DoublyLinkedList:

    """
        Classe que representa a unidade de informação
        armazenada pela lista duplamente encadeada
    """
    class Node:

        def __init__(self,data):
            self.prev = None   # Ponteiro para o nodo anterior
            self.data = data   # Dado útil para o usuário
            self.next = None   # Ponteiro para o nodo posterior

    """ Construtor da classe DoublyLinkedList """
    def __init__(self):
        self.__head = None     # Ponteiro para o primeiro nodo da lista
        self.__tail = None     # Ponteiro para o último nodo da lista
        self.__count = 0       # Qauntidade de nodos da lista

    """ Método que retorna a quantidade de itens da lista """
    def get_count(self):
        return self.__count

    """ Método PRIVADO que encontra um nodo na posição especificada """
    def __find_node(self, pos):
        # 1º caso: posição 0, retorna self.__head
        if pos == 0: return self.__head

        # 2º caso: posição final (self.get_count() -1)
        if pos == self.get_count() - 1: return self.__tail

        # 3º caso: posição intermediária

        # Se a posição estiver na primeira metade da lista, faz o
        # percurso a partir de self.__head, seguindo next
        if pos < self.get_count() // 2:
            # Percorre a lista quantas vezes for necessário para encontrar
            # o nodo
            node = self.__head
            for i in range(1, pos + 1): node = node.next
            return node

        # Senão, a posição estando na segunda metade da lista, faz
        # percurso reverso a partir de self.__tail, seguindo prev
        else:
            node = self.__tail   # Começa pelo último nodo
            for i in range(self.get_count() - 2, pos - 1, -1):
                node = node.prev
            return node

    """ Método que insere um novo valor à lista"""
    def insert(self, pos, val):

        # Criaremos um nodo para armazenar a informação do usuário e
        # também os ponteiros prev e next, ambos apontados para None
        inserted = self.Node(val)

        # 1º caso: a lista está vazia, e este é o primeiro nodo a
        # ser inserido
        if self.get_count() == 0:
            self.__head = inserted
            self.__tail = inserted

        # 2º caso: inserção no início da lista (posição 0)
        elif pos == 0:
            inserted.next = self.__head
            self.__head.prev = inserted
            self.__head = inserted

        # 3º caso: inserção no final da lista
        # Obs: consideramos como posição final qualquer posição
        # que seja >= self.get_count()
        elif pos > self.get_count():
            inserted.prev = self.__tail
            self.__tail.next = inserted
            self.__tail = inserted

        # 4º caso: inserção em posição intermediária
        elif pos > 0:  # Descarta posições negativas
            # Encontra o nodo que atualmente ocupa a posição de inerção
            current = self.__find_node(pos)

            # Determina o nodo anterior à posição de inserção
            before = current.prev

            before.next = inserted
            inserted.prev = before
            inserted.next = current
            current.prev = inserted            

        # Incrementa a quantidade de nodos da lista
        self.__count +=1
