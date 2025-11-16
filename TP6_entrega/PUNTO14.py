# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución 
# a las siguientes tareas:

from graph import Graph
import math

casa = Graph(is_directed=False)

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

casa.insert_vertex("cocina")
casa.insert_vertex("comedor")
casa.insert_vertex("cochera")
casa.insert_vertex("quincho")
casa.insert_vertex("baño1")
casa.insert_vertex("baño2")
casa.insert_vertex("habitacion1")
casa.insert_vertex("habitacion2")
casa.insert_vertex("salaEstar")
casa.insert_vertex("terraza")
casa.insert_vertex("patio")

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, 
# el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
casa.insert_edge("cocina", "comedor", 5)
casa.insert_edge("cocina", "salaEstar", 8)
casa.insert_edge("cocina", "baño1", 6)
casa.insert_edge("cocina", "patio", 12)
casa.insert_edge("cocina", "habitacion1", 15)

casa.insert_edge("comedor", "salaEstar", 4)
casa.insert_edge("comedor", "terraza", 10)
casa.insert_edge("comedor", "patio", 7)

casa.insert_edge("cochera", "patio", 3)
casa.insert_edge("cochera", "quincho", 8)
casa.insert_edge("cochera", "habitacion2", 18)

casa.insert_edge("quincho", "patio", 5)
casa.insert_edge("quincho", "terraza", 6)
casa.insert_edge("quincho", "baño2", 9)
casa.insert_edge("quincho", "habitacion2", 12)
casa.insert_edge("quincho", "cochera", 8)

casa.insert_edge("baño1", "habitacion1", 4)
casa.insert_edge("baño1", "salaEstar", 7)
casa.insert_edge("baño1", "cocina", 6)

casa.insert_edge("baño2", "habitacion2", 5)
casa.insert_edge("baño2", "terraza", 8)
casa.insert_edge("baño2", "quincho", 9)

casa.insert_edge("habitacion1", "salaEstar", 6)
casa.insert_edge("habitacion1", "baño1", 4)
casa.insert_edge("habitacion1", "cocina", 15)

casa.insert_edge("habitacion2", "terraza", 7)
casa.insert_edge("habitacion2", "baño2", 5)
casa.insert_edge("habitacion2", "quincho", 12)

casa.insert_edge("salaEstar", "terraza", 9)
casa.insert_edge("salaEstar", "patio", 11)
casa.insert_edge("salaEstar", "comedor", 4)

casa.insert_edge("terraza", "patio", 6)
casa.insert_edge("terraza", "quincho", 6)
casa.insert_edge("terraza", "comedor", 10)

casa.insert_edge("patio", "cochera", 3)
casa.insert_edge("patio", "quincho", 5)
casa.insert_edge("patio", "terraza", 6)

print("[+] ESTRUCTURA DE LA CASA")
casa.show()
print()

# c. Árbol de expansión mínima y metros de cables necesarios
def expansionMinima(grafo):
    expansionArbol = grafo.kruskal("baño1") #ejemplo de prueba
    metrosTotal = 0
    for edge in expansionArbol.split(';'):
        origen, destino, peso = edge.split('-')
        metrosTotal += int(peso)
    print(f"Total de metros requeridos: {metrosTotal} m")



# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.
def caminoCocinaSala(grafo):
    resultado = {}
    camino = grafo.dijkstra("habitacion1")
    destino = "salaEstar"
    pesoTotal = None
    caminoCompleto = []

    while camino.size() > 0:
        value = camino.pop()
        if value[0] == destino:
            if pesoTotal is None:
                pesoTotal = value[1]
            caminoCompleto.append(value[0])
            destino = value[2]

    caminoCompleto.reverse()
    resultado["habitacion1"] = {
            "camino": caminoCompleto,
            "distancia": pesoTotal if pesoTotal is not None and pesoTotal != math.inf else math.inf
        }
    
    return resultado

expansionMinima(casa)
print()
print("CAMINO MÁS CORTO HABITACIÓN 1 → SALA DE ESTAR")
print(caminoCocinaSala(casa))

