from lib.graph import Graph

familia = Graph(True)   # Grafo direcionado

familia.add_edge("Temístocles", "Gercina", "marido de")
familia.add_edge("Gercina", "Temístocles", "esposa de")
print(familia)

familia.add_edge("Jerusa", "Termístocles","filha de")
familia.add_edge("Jerusa", "Gercina","filha de")
familia.add_edge("Termístocles", "Jerusa","pai de")
familia.add_edge("Gercina", "Jerusa","mãe de")
print(familia)