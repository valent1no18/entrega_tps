# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y 
# resuelva las siguientes consultas:

from tree import BinaryTree
from diosesData import criaturas, CriaturasYDioses

arbol = BinaryTree()

for personaje in criaturas:
    # b. se debe permitir cargar una breve descripción sobre cada criatura;
    breveDescripcion = input(f"Ingrese una breve descripción sobre la criatura {personaje[0]}:")
    ente = CriaturasYDioses(
        criatura = personaje[0],
        derrotadoPor = personaje[1],
        descripcion = breveDescripcion,
        capturada = personaje[3]  # g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
    )
    arbol.insert(ente.criatura, ente)


# a. listado inorden de las criaturas y quienes la derrotaron;
def inOrder(tree_):
    def __inOrder(root):
        if root is not None:
            __inOrder(root.left)
            print(root.other_values) 
            __inOrder(root.right)

    if tree_.root is not None:
        __inOrder(tree_.root)


# c. mostrar toda la información de la criatura Talos;
pos = arbol.search('Talos')
if pos is not None:
    print(f"[+] INFORMACIÓN DE TALOS: {pos.other_values}")


# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;


# e. listar las criaturas derrotadas por Heracles;
def derrotadorHeracles(tree_):
    derrotados = []
    def __derrotadorHeracles(root):
        if root is not None:
            __derrotadorHeracles(root.left)
            if root.other_values.derrotadoPor == "Heracles":
                derrotados.append(root.other_values.criatura) 
            __derrotadorHeracles(root.right)

    if tree_.root is not None:
        __derrotadorHeracles(tree_.root)

    print("[+] CRIATURAS DERROTADAS POR HERACLES:")
    for criatura in derrotados:
        print(f"- {criatura}")

# f. listar las criaturas que no han sido derrotadas;
def noDerrotados(tree_):
    noDerrotado = []
    def __noDerrotados(root):
        if root is not None:
            __noDerrotados(root.left)
            if root.other_values.derrotadoPor == "-":
                noDerrotado.append(root.other_values.criatura) 
            __noDerrotados(root.right)

    if tree_.root is not None:
        __noDerrotados(tree_.root)

    print("[+] CRIATURAS QUE NO HAN SIDO DERROTADAS:")
    for criatura in noDerrotado:
        print(f"- {criatura}")

# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
def atrapadasPorHeracles(tree_):
    nombres = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto", "Aves del Estínfalo"] # k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
    for nombre in nombres:
        pos = tree_.search(nombre)
        if pos is not None:
            pos.other_values.capturada = "Heracles"
            print(f"[+] {nombre} AHORA ESTÁ COMO ATRAPADA POR HERACLES ({pos.other_values}).")
        else:
            print(f"[!] {nombre} NO SE ENCONTRÓ EN EL ÁRBOL.")

# i. se debe permitir búsquedas por coincidencia;



# j. eliminar al Basilisco y a las Sirenas;
def eliminados(tree_):
    delete_value, deleter_other_values = tree_.delete('Basilisco')
    if delete_value is not None:
        print(delete_value, deleter_other_values)


    delete_value2, deleter_other_values2 = tree_.delete('Sirenas')
    if delete_value2 is not None:
        print(delete_value2, deleter_other_values2)


# n. muestre las criaturas capturadas por Heracles.
def capturadosHeracles(tree_):
    capturados = []
    def __capturadosHeracles(root):
        if root is not None:
            __capturadosHeracles(root.left)
            if root.other_values.capturada == "Heracles":
                capturados.append(root.other_values.criatura) 
            __capturadosHeracles(root.right)

    if tree_.root is not None:
        __capturadosHeracles(tree_.root)

    print("[+] CRIATURAS DERROTADAS POR HERACLES:")
    for criatura in capturados:
        print(f"- {criatura}")




#print("[+] LISTADO INORDER DE LAS CRIATURAS Y DE QUIENES LAS DERROTARON:")
#print(inOrder(arbol))
#print()
#derrotadorHeracles(arbol)
#print()
#noDerrotados(arbol)
atrapadasPorHeracles(arbol)
print("[+] ÉSTOS PERSONAJES FUERON ELIMINADOS:")
eliminados(arbol)
print()
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;

value, other_value = arbol.delete("Ladón")
if value is not None:
    nuevaCriatura = "Dragón Ladón"
    other_value.criatura = nuevaCriatura
    arbol.insert(nuevaCriatura, other_value)
    print(f"[+] NUEVO NOMBRE PARA LADÓN: {other_value}")

# m. realizar un listado por nivel del árbol;
print("[+] LISTADO POR NIVEL DE LAS CRIATURAS Y DE QUIENES LAS DERROTARON:")
arbol.by_level()
print()
capturadosHeracles(arbol)


