# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

from personajesData import Personaje, personajesMCU
from tree import BinaryTree

arbol = BinaryTree()
arbolHero = BinaryTree()
arbolVillain = BinaryTree()


for character in personajesMCU:
    hero = Personaje(
        name = character[0],
        isVillano = character[1]
    )
    arbol.insert(hero.name, hero)

# b. listar los villanos ordenados alfabéticamente;
def orderVillanos(tree_):
    def __orderVillanos(root):
        if root is not None:
            __orderVillanos(root.left)
            if root.other_values.isVillano:
                print(root.value)
            __orderVillanos(root.right)
    __orderVillanos(tree_.root)


# c. mostrar todos los superhéroes que empiezan con C;
def namesC(tree_):
    def __namesC(root):
        if root is not None: # caso base: si la raíz es None, termina la rama
            __namesC(root.left) # llamada recursiva del izquierdo
            if root.other_values.name.startswith("C") and not root.other_values.isVillano:
                print(root.value)
            __namesC(root.right) # llamada recursiva del nodo derecho
    __namesC(tree_.root) # recorrido de la raiz

# d. determinar cuántos superhéroes hay el árbol;
def nodeCounter(tree_):
    def __nodeCounter(root):
        if root is None:
            return 0

        if not root.other_values.isVillano:
            return 1 + __nodeCounter(root.left) + __nodeCounter(root.right)
        else:
            return __nodeCounter(root.left) + __nodeCounter(root.right)
    
    return __nodeCounter(tree_.root)

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
def busqProximidad(tree_):
    tree_.proximity_search("Doc")
    name = input('Ingrese nombre para modificar: ')
    value, other_value = tree_.delete(name)

    if value is not None:
        fix_name = input('Ingrese el nuevo nombre: ')
        other_value.name = fix_name
        tree_.insert(fix_name, other_value) 

    print()
    tree_.proximity_search('Doc')
    print()
    pos = tree_.search('Doctor Strange')
    if pos is not None:
        print(pos.value, pos.other_values)

# f. listar los superhéroes ordenados de manera descendente;
def orderDescendente(tree_):
    def __orderDescendente(root):
        if root is not None:
            __orderDescendente(root.right)
            if not root.other_values.isVillano:
                print(root.value)
            __orderDescendente(root.left)
    __orderDescendente(tree_.root)

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:

def generarBosque(tree_, treeHero, treeVillain):
    def __generarBosque(root, treeHero, treeVillain):
        if root is not None:
            if root.other_values.isVillano is False:
                treeHero.insert(root.value, root.other_values)
            else:
                treeVillain.insert(root.value, root.other_values)
            __generarBosque(root.left, treeHero, treeVillain)
            __generarBosque(root.right, treeHero, treeVillain)

    __generarBosque(tree_.root, treeHero, treeVillain)
    return treeHero, treeVillain


# I. determinar cuántos nodos tiene cada árbol;
def nodeCounterBosque(tree_):
    def __nodeCounterBosque(root):
        if root is None:
            return 0
        return 1 + __nodeCounterBosque(root.left) + __nodeCounterBosque(root.right)
    return __nodeCounterBosque(tree_.root)

print("Villanos ordenados alfabéticamente:")
orderVillanos(arbol)
print()
print("Superhéroes que empiezan con C: ")
namesC(arbol)
print()
print("Cantidad de súperheroes en el árbol: ", nodeCounter(arbol))
print()
print("Superhéroes listados de forma descendente:")
orderDescendente(arbol)
print()
generarBosque(arbol, arbolHero, arbolVillain)
print("Cantidad de superhéroes en el bosque: ", nodeCounterBosque(arbolHero))
print("Cantidad de villanos en el bosque: ", nodeCounterBosque(arbolVillain))
print()
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
print("Superhéroes (DEL BOSQUE) ordenados alfabéticamente:")
arbolHero.in_order()
print()
print("Villanos (DEL BOSQUE) ordenados alfabéticamente:")
arbolVillain.in_order()
print()
busqProximidad(arbol)