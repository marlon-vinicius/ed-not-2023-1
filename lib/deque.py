"""
    ESTRUTURA DE DADOS DEQUE
    Deque (Double-Ended QUEue) é uma estrutura de dados derivada
    da fila que permite inserções e remoções em qualquer uma de
    suas extremidades. Com isso, o deque pode se comportar tanto
    como uma fila comum quanto uma fila em que são admitidas
    inserções prioritárias e a possibilidade de desistência
    (remoção) do último item.
"""
class Deque:

    """ Método construtor """
    def __init__(self):
        self.__data = []    # Lista vazia

    """ Método para inserção no inicio """
    def insert_front(self,val):
        self.__data.insert(0,val)

    """ Método para inserção no final """
    def insert_back(self,val):
        self.__data.append(val)

    """
        Método que retorna se o deque está vazio (True)
        ou não (False)
    """
    def is_empty(self):
        return len(self.__data) == 0

    """ Método para remoção no inicio """
    def remove_front(self):
        if self.is_empty():
            raise Exception("ERRO: impossivel remover de um deque vazio.")
        return self.__data.pop(0)

    """ Método para remoção no final """
    def remove_back(self):
        if self.is_empty():
            raise Exception("ERRO: impossivel remover de um deque vazio.")
        return self.__data.pop()

    """ Método para consultar do inicio """
    def peek_front(self):
        if self.is_empty():
            raise Exception("ERRO: impossivel consultar um deque vazio.")
        return self.__data[0]

    """ Método para consultar do final """
    def peek_back(self):
        if self.is_empty():
            raise Exception("ERRO: impossivel consultar um deque vazio.")
        return self.__data[-1]

    """ Método para consultar uma representação do deque como string """
    def __str__(self):
        return str(self.__data)