"""
    Classe é uma estrutura que representa conuntamente dados e algoritmos.
    Uma classe pode ser comparada a uma "assadeira" com a qual se pode
    produzir diferentes "assados" (objetos), variando os "ingredientes"
    (dados) e o "modo de fazer" (algoritmos). Apesar dessa variação, todos
    os objetos criados a partir de uma classe terão sempre formato
    determinado por esta.
"""
from math import pi

# Por convenção, nomes de classe seguem a convenção PascalCase
class FormaGeometrica:

    """
        Uma classe pode ter, dentro de si, tanto dados quanto funções
        (estas, representando os algoritmos). Uma função especial,
        chamada __init__, é chamada sempre que um novo objeto é criado
        a partir de uma classe. Essa função especial é chamada de 
        CONSTRUTOR.

        Quando aparecem dentro de uma classe:
        ~> funções passam a ser chamadas de MÉTODOS, e seu primeiro
        parâmetro é sempre self, que representa o proprio objeto
        ~> variáveis passam a ser chamadas ATRIBUTOS
    """

    def __init__(self, base, altura, tipo):

        self.set_base(base)
        self.set_altura(altura)
        self.set_tipo(tipo)

    ## Métodos setter
    def set_base(self, val):
        if type(val) not in [int, float] or val <= 0:
            raise Exception(f"ERRO: a base ({val}) deve ser numérica e maior que zero.")
        self.__base = val

    def set_altura(self,val):
        if type(val) not in [int, float] or val <= 0:
            raise Exception(f"ERRO: a altura ({val}) deve ser numérica e maior que zero.")
        self.__altura = val

    def set_tipo(self,val):
        if val not in ["R", "T", "E"]:
            raise Exception(f"ERRO: o tipo ('{val}') deve ser 'R', 'T' ou 'E'.")
        self.__tipo = val 

    # Métodos getter
    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura 
    
    def get_tipo(self):
        return self.__tipo

    # Converte o objeto para um representação personalizada em string
    def __str__(self):
        return f"< Base: {self.__base}; Altura: {self.__altura}; Tipo: {self.__tipo} >"

    def calc_area(self):
        if self.__tipo == "R":    # Reângulo
            return self.__base * self.__altura
        elif self.__tipo == "T":  # Triângulo
            return self.__base * self.__altura / 2
        else:                     # Elipse/Círculo
            return (self.__base / 2) * (self.__altura / 2) * pi

###########################################################################

# Criando um objeto chamado forma1 a pertir da classe FormaGeometrica
forma1 = FormaGeometrica(10, 7.2, "T")
forma2 = FormaGeometrica(7, 4.5, "R")
forma3 = FormaGeometrica(12, 12, "E")

# forma1.set_base("batata")
# forma1.set_altura(-4)

# Formata a área com duas casas decimais
print(forma1, f"Área: {forma1.calc_area():.2f}")
print(forma2, f"Área: {forma2.calc_area():.2f}")
print(forma3, f"Área: {forma3.calc_area():.2f}")