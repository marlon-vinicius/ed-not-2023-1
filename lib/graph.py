"""
    ESTRUTURA DE DADOS GRAFO
    É uma estrutura de dados não-linear, formada por vértices
    (ou nodos) e arestas (ou arcos). Sua principal finalidade
    é representar as relações entre diferentes objetos. Tais
    relações podem ser bidirecionais, resultando em grafos não
    direcionados, ou unidirecionais, constituindo grafos
    direcionais (digrafos). Tem várias aplicações, como a 
    reprentação de redes de computadores, mapas e caminhos e
    redes sociais.
"""
class Graph:

    """
        Método construtor
    """
    def __init__(self, is_directed = False):
        self.__is_directed = is_directed

        # __data armazenará o grafo no formato de 
        # LISTA DE ADJACÊNCIA
        self.__data = {}    # Dicionário vazio

    """
        Método que adiciona um vértice ao grafo
    """
    def add_vertex(self, val):
        # Verifica se o vértice já existe no dicionário.
        # Só cria se o vértice não existir
        if not val in self.__data:
            self.__data[val] = set()   # Conjunto vazio

    """
        Método que adiciona a aresta entre dois vértices
        origin: vértice de origem
        dest: vértice de destino
        rel: nome do relacionamento (opcional)
    """
    def add_edge(self, origin, dest, rel = None):
        # Cria os vértices de origem e destino, caso não
        # existam ainda
        if not origin in self.__data: self.add_vertex(origin)
        if not dest in self.__data: self.add_vertex(dest)

        # Monta a aresta
        edge1 = (dest,rel)     # Isto é uma tupla ("lista imutável")

        # Adiciona a relação origem -> destino
        self.__data[origin].add(edge1)

        # Se o grafo não for direcionado, adicionamos também a
        # relação no sentido oposto, isto é, destino -> origem
        if not self.__is_directed:
            edge2 = (origin, rel)  # Tupla
            self.__data[dest].add(edge2)

    """
        Método que retorna o grau (número de arestas incidentes)
        de um vértice
    """
    def __degree(self, vertex):
        # Se vertex existir no dicionário self.__data, retorna o
        # número de elementos do respectivo conjunto de vértices
        # adjacentes
        if vertex in self.__data: return len(self.__data[vertex])
        else: return 0

    """
        Método que verifica se um determinado vértice é referenciado
        por outro (necessário na exclusão de vértices de grafos
        direcionados)
    """
    def __is_referenced(self, vertex):
        for vtx_ref in self.__data.keys():    # Percorrendo o dicionário
            for edge in self.data[vtx_ref]:   # Percorrendo os conjuntos
                if vertex == edge[0]: return True
        return False
    """
        Método que representa o grafo com uma string
    """
    def __str__(self):
        output = str(self.__data)
        output += f",\nis_directed: {self.__is_directed}\n\n"
        return output

#################################################################

estradas = Graph()   # Não direcionado, por padrão
print(estradas)

estradas.add_vertex("Franca")
print(estradas)

estradas.add_edge("Franca", "Batatais", "Rod. Candido Portinari")
print(estradas)

estradas.add_edge("Franca", "Restinga")
print(estradas)