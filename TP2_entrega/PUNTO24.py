#Ejercicio 24: Personajes de Marvel. 
#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:


from stack import Stack

personajesMarvel = Stack()

personajes = [
    ("Spider-Man", "6 películas"),
    ("Thor Odinson", "9 películas"),
    ("Hulk", "8 películas"),
    ("Rocket Raccoon", "6 películas"),
    ("Capitán América", "7 películas"),
    ("Viuda Negra", "9 películas"),
    ("Pantera Negra", "4 películas"),
    ("Thanos", "5 películas"),
    ("Groot", "4 películas"),
    ("Doctor Stephen Strange", "4 películas")
]

for personaje in personajes:
    personajesMarvel.push(personaje)

# A. Determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila.
def rocketAndGroot(pila):
    pilaAux = Stack()
    posRocket = None
    posGroot = None
    posicion = 1
    while pila.size() > 0:
        personaje = pila.pop()
        pilaAux.push(personaje)

        if personaje[0] == "Rocket Raccoon":
            posRocket = posicion
        elif personaje[0] == "Groot":
            posGroot = posicion

        posicion += 1

    while pilaAux.size() > 0:
        pila.push(pilaAux.pop())

    if posRocket is not None:
        print(f"Rocket Raccoon se encuentra en la posición {posRocket} de la pila.")
    else:
        print("Rocket Raccoon no aparece en la pila.")

    if posGroot is not None:
        print(f"Groot se encuentra en la posición {posGroot} de la pila.")
    else:
        print("Groot no aparece en la pila.")

# B. Determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece.
def cincoPeliculas(pila):
    pilaAux = Stack()

    while pila.size() > 0:
        personaje = pila.pop()
        pilaAux.push(personaje)
        cantPeliculas = int(personaje[1].split()[0])

        if cantPeliculas > 5:
            print(f"{personaje[0]} participó en {cantPeliculas} peliculas de Marvel Cinematic Universe.")

    while pilaAux.size() > 0:
        pila.push(pilaAux.pop())

# C. Determinar en cuantas películas participo la Viuda Negra (Black Widow).
def blackWidow(pila):
    pilaAux = Stack()
    viudaNegra = False

    while pila.size() > 0:
        personaje = pila.pop()
        pilaAux.push(personaje)
        cantPeliculas = int(personaje[1].split()[0])

        if personaje[0] == "Viuda Negra":
            cantPeliculas = int(personaje[1].split()[0])
            print(f"Viuda Negra participó en {cantPeliculas} peliculas de Marvel Cinematic Universe.")
            viudaNegra = True


    if not viudaNegra:
        print("Viuda Negra no forma parte de la pila.")

    while pilaAux.size() > 0:
        pila.push(pilaAux.pop())

# D. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
def nombresCDG(pila):
    pilaAux = Stack()
    letras = ["C", "D", "G"]
    nombre = False

    while pila.size() > 0:
        personaje = pila.pop()
        pilaAux.push(personaje)

       
        if personaje[0][0] in letras:
            print(f"{personaje [0]} enpieza con alguna de las siguientes letras: {letras}")
            nombre = True

    if not nombre:
        print(f"No hay nombres que comiencen con las letras {letras}")

    while pilaAux.size() > 0:
        pila.push(pilaAux.pop())




#MENÚ
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrarMenu():
    print("-----> MENÚ PRINCIPAL DE LA PILA PARA PELICULAS DE MARVEL CINEMATIC UNIVERSE <-----")
    print("-Opciones:")
    print("1. Mostrar todos los personajes con su cantidad de peliculas.")
    print("2. Mostrar cosas específicas de los personajes.")
    print("3. Salir.")

def mostrarSubMenu1():
    print("---> OPCIONES PARA MOSTRAR COSAS DE LOS PERSONAJES <---")
    print("1. Posición donde se encuentran Rocket Raccoon y Groot.")
    print("2. Personajes que participaron en más de 5 películas de la saga.")
    print("3. Cantidad de películas en las que participó la Viuda Negra")
    print("4. Personajes cuyos nombre empiezan con C, D y G.")
    print("5. Volver al menú")

opcion = 0
while opcion != 3:
    limpiar_consola()
    mostrarMenu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        personajesMarvel.show()
        input("Presione Enter para continuar...")
    elif opcion == 2:
        subopcion = 0
        while subopcion != 5:
            limpiar_consola()
            mostrarSubMenu1()
            subopcion = int(input("Seleccione una opción del submenú: "))
            if subopcion == 1:
                limpiar_consola()
                rocketAndGroot(personajesMarvel)
                input("Presione Enter para continuar...")
            elif subopcion == 2:
                limpiar_consola()
                cincoPeliculas(personajesMarvel)
                input("Presione Enter para continuar...")
            elif subopcion == 3:
                limpiar_consola()
                blackWidow(personajesMarvel)
                input("Presione Enter para continuar...")
            elif subopcion == 4:
                limpiar_consola()
                nombresCDG(personajesMarvel)
                input("Presione Enter para continuar...")
            elif subopcion == 5:
                limpiar_consola()
                print("Volviendo al menú principal...")
            else:
                print("Opción no válida. Intente de nuevo.")
    elif opcion == 3:
        limpiar_consola()
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente de nuevo.")



