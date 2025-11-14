# 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios
# para resolver las tareas, listadas a continuación:

from graph import Graph
from heap import HeapMin
from list_ import List
from queue_ import Queue
from stack import Stack

red = Graph(is_directed=False) # h. debe utilizar un grafo no dirigido.

# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook,
# servidor, router, switch, impresor;

red.insert_vertex("Switch01", "switch")
red.insert_vertex("PC1", "pc")
red.insert_vertex("PC2", "pc")  
red.insert_vertex("Impresora1", "impresora") 
red.insert_vertex("RouterCentral", "router")
red.insert_vertex("Switch02", "switch")
red.insert_vertex("Red Hat", "notebook") 
red.insert_vertex("Debian", "notebook") 
red.insert_vertex("Arch", "notebook")    
red.insert_vertex("Manjaro", "pc")      
red.insert_vertex("Fedora", "pc")
red.insert_vertex("Guarani", "servidor")
red.insert_vertex("MongoDB", "servidor")

# Conexiones y pesos
red.insert_edge("Switch01", "PC1", 1)
red.insert_edge("Switch01", "PC2", 1)
red.insert_edge("Switch01", "Impresora1", 1)
red.insert_edge("Switch01", "RouterCentral", 1)
red.insert_edge("RouterCentral", "Switch02", 1)
red.insert_edge("RouterCentral", "Guarani", 1)
red.insert_edge("RouterCentral", "MongoDB", 1)
red.insert_edge("Switch02", "Red Hat", 1)
red.insert_edge("Switch02", "Debian", 1)
red.insert_edge("Switch02", "Arch", 1)
red.insert_edge("Switch02", "Manjaro", 1)
red.insert_edge("Switch02", "Fedora", 1)

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

def costoImpresora(red, origen):
    camino = red.dijkstra(origen)
    while camino.size() > 0:
        nodo = camino.pop()
        if nodo[0] == "Impresora1":
            return nodo[1]


print("[+] CAMINOS MAS CORTOS:")
print(f"[-] Desde Manjaro: {costoImpresora(red, 'Manjaro')}")
print(f"[-] Desde Red Hat: {costoImpresora(red, 'Red Hat')}")
print(f"[-] Desde Fedora: {costoImpresora(red, 'Fedora')}")
print()

# d. encontrar el árbol de expansión mínima;
arbolExpansion = red.kruskal("PC1")
print(f"[-] Arbol de expansion minima: {arbolExpansion}")
print()

# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
def costoServidor(red, origen, servidor):
    camino = red.dijkstra(origen)
    while camino.size() > 0:
        nodo = camino.pop()
        if nodo[0] == servidor:
            return nodo[1]


print("[+] PC MÁS CERCANA AL SERVIDOR GUARANÍ ")
pcs = ["PC1", "PC2", "Manjaro", "Fedora"]
mejorPC = None
menorCosto = float("inf")

for pc in pcs:
    costo = costoServidor(red, pc, "Guarani")
    if costo is not None and costo < menorCosto:
        menorCosto = costo
        mejorPC = pc
    print(f"Desde {pc}: {costo}")

print(f"[-] La PC más cercana a Guarani es: {mejorPC} con costo: {menorCosto}")
print()

# f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;
def costoServidorMongoDB(red, origen, servidor):
    camino = red.dijkstra(origen)
    while camino.size() > 0:
        nodo = camino.pop()
        if nodo[0] == servidor:
            return nodo[1]


print("[+] MEJOR CAMINO DESDE SWITCH01 A MONGODB")
dispositivos = ["PC1", "PC2", "Impresora1"]
mejorDispositivo = None
menorCosto = float("inf")

for dispositivo in dispositivos:
    costo = costoServidorMongoDB(red, dispositivo, "MongoDB")
    if costo is not None and costo < menorCosto:
        menorCosto = costo
        mejorDispositivo = dispositivo
    print(f"Desde {dispositivo}: {costo}")

print(f"[-] El mejor camino desde Switch01 es desde: {mejorDispositivo} con costo: {menorCosto}")

# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;

red.delete_edge("Switch01", "Impresora1", "value")

red.insert_edge("Switch02", "Impresora1", 1)
print()
print("[*] Impresora movida de Switch01 a Switch02")

print("[+] BARRIDO EN PROFUNDIDAD (CON IMPRESORA EN SWITCH02)")
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

print("[+] BARRIDOS EN AMPLITUD (CON IMPRESORA EN SWITCH02)")
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