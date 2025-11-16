# 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios
# para resolver las s, listadas a continuación:

from graph import Graph
import math

red = Graph(is_directed=False) # h. debe utilizar un grafo no dirigido.

# a. cada value además del nombre del equipo deberá almacenar su tipo: pc, notebook,
# servidor, router, switch, impresor;

red.insert_vertex("Red Hat", "notebook")
red.insert_vertex("Debian", "notebook")
red.insert_vertex("Arch", "notebook")
red.insert_vertex("Manjaro", "pc")
red.insert_vertex("Fedora", "pc")
red.insert_vertex("Impresora", "impresora")
red.insert_vertex("Guarani", "servidor")
red.insert_vertex("Switch1", "switch")
red.insert_vertex("Switch2", "switch")
red.insert_vertex("MongoDB", "servidor")
red.insert_vertex("Ubuntu", "pc")
red.insert_vertex("Mint", "pc")
red.insert_vertex("Router1", "router")
red.insert_vertex("Router2", "router")
red.insert_vertex("Router3", "router")
red.insert_vertex("Parrot", "pc")

# Conexiones y pesos
red.insert_edge("Ubuntu", "Switch1", 18),
red.insert_edge("Impresora", "Switch1", 22),
red.insert_edge("Mint", "Switch1", 80),
red.insert_edge("Debian", "Switch1", 17),
red.insert_edge("Switch1", "Router1", 29),
red.insert_edge("Router1", "Router2", 37),
red.insert_edge("Router1", "Router3", 43),
red.insert_edge("Router2", "Router3", 50),
red.insert_edge("Router2", "Guarani", 9),
red.insert_edge("Router2", "Red Hat", 25),
red.insert_edge("Router3", "Switch2", 61),
red.insert_edge("Switch2", "Fedora", 3),
red.insert_edge("Switch2", "Arch", 56),
red.insert_edge("Switch2", "Manjaro", 40),
red.insert_edge("Switch2", "Parrot", 12),
red.insert_edge("Switch2", "MongoDB", 5)

# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch;
print("[+] BARRIDOS EN PROFUNDIDAD")
print()
print("[-] Desde Red Hat:")
red.deep_sweep("Red Hat")
print()
print("[-] Desde Debian:")
red.deep_sweep("Debian")
print()
print("[-] Desde Arch:")
red.deep_sweep("Arch")
print()

print("[+] BARRIDOS EN AMPLITUD")
print()
print("[-] Desde Red Hat:")
red.amplitude_sweep("Red Hat")
print()
print("[-] Desde Debian:")
red.amplitude_sweep("Debian")
print()
print("[-] Desde Arch:")
red.amplitude_sweep("Arch")
print()

# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, 
# Red Hat, Fedora hasta la impresora;

def caminoImpresora(grafo):
    pcs = ["Manjaro", "Red Hat", "Fedora"]
    resultado = {}

    for pc in pcs:
        camino = grafo.dijkstra(pc)
        destino = "Impresora"
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
    resultado[pc] = {
            "camino": caminoCompleto,
            "distancia": pesoTotal if pesoTotal is not None and pesoTotal != math.inf else math.inf
        }
    
    return resultado


# d. encontrar el árbol de expansión mínima;
def expansionMinima(grafo):
    expansionArbol = grafo.kruskal("Impresora") #ejemplo de prueba
    pesoTotal = 0
    for edge in expansionArbol.split(';'):
        origen, destino, peso = edge.split('-')
        pesoTotal += int(peso)
    print(f"Peso total: {pesoTotal}")


# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
def caminoServidor(grafo):
    pcs = ["Manjaro", "Parrot", "Fedora", "Ubuntu", "Mint"]
    pcCercana = None
    mejorCamino = {}
    distanciaMinima = math.inf
    for pc in pcs:
        camino = grafo.dijkstra(pc)
        destino = "Guarani"
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

        if pesoTotal is not None and pesoTotal < distanciaMinima:
            distanciaMinima = pesoTotal
            pcCercana = pc
            mejorCamino = {
                pc: {
                    "camino": caminoCompleto,
                    "distancia": pesoTotal
                }
            }
    return mejorCamino if pcCercana else False


# f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;
def caminoServidorMongoDB(grafo):
    pcs = ["Ubuntu", "Mint"]
    pcCercana = None
    mejorCamino = {}
    distanciaMinima = math.inf
    for pc in pcs:
        camino = grafo.dijkstra(pc)
        destino = "MongoDB"
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

        if pesoTotal is not None and pesoTotal < distanciaMinima:
            distanciaMinima = pesoTotal
            pcCercana = pc
            mejorCamino = {
                pc: {
                    "camino": caminoCompleto,
                    "distancia": pesoTotal
                }
            }
    return mejorCamino if pcCercana else False


# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;

red.delete_edge("Impresora", "Switch1", "value")

red.insert_edge("Impresora", "Router2", 1)
print()
print("[*] Conexion de la impresora al router 02 fue cambiada correctamente")

print("[+] BARRIDO EN PROFUNDIDAD (CON IMPRESORA EN Switch2)")
print()
print("[-] Desde Red Hat:")
red.deep_sweep("Red Hat")
print()
print("[-] Desde Debian:")
red.deep_sweep("Debian")
print()
print("[-] Desde Arch:")
red.deep_sweep("Arch")
print()

print("[+] BARRIDOS EN AMPLITUD (CON IMPRESORA EN Switch2)")
print()
print("[-] Desde Red Hat:")
red.amplitude_sweep("Red Hat")
print()
print("[-] Desde Debian:")
red.amplitude_sweep("Debian")
print()
print("[-] Desde Arch:")
red.amplitude_sweep("Arch")
print()

print("CAMINOS MAS CORTOS A LA IMPRESORA DESDE LAS PCS:")
caminoImpresora(red)
print()
expansionMinima(red)
print()
resultado = caminoServidor(red)
print(f"EL CAMINO MÁS CORTO DESDE UNA PC AL GUARANI ES: {resultado}")
print()
resultado2 = caminoServidorMongoDB(red)
print(f"EL CAMINO MÁS CORTO DESDE UNA PC A MONGODB ES: {resultado2}")