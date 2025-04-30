#Ejercicio 22: Personajes de Marvel. 
# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
# por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, 
# etc., desarrollar un algoritmo que resuelva las siguientes actividades:

from queue_ import Queue

personajesMarvel = Queue()

personajes = [
    ("Tony Stark", "Iron Man", "M"),
    ("Scott Lang", "Hombre Hormiga", "M"),
    ("Steve Rogers","Capitán América", "M"),
    ("Natasha Romanoff", "Viuda Negra", "F"),
    ("Peter Parker", "Hombre Araña", "M"),
    ("Carol Danvers", "Capitana Marvel", "F"),
    ("Stephen Strange", "Doctor Strange", "M")
]

for personaje in personajes:
    personajesMarvel.arrive(personaje)

# A. Determinar el nombre del personaje de la superhéroe Capitana Marvel.
def capitanaMarvel(cola):
    tamañoCola = cola.size()
    capitana = False

    for i in range(tamañoCola):
        personaje = cola.on_front()
        if personaje[1].lower() == "capitana marvel": 
            print(f"Nombre del personaje de la superhéroe Capitana Marvel: {personaje[0]}")
            capitana = True
        cola.move_to_end()

    if not capitana:
        print("El personaje de la superhéroe Capitana Marvel no está en la cola.")


# B. Mostrar los nombres de los superhéroes femeninos.
def superheroesFemeninos(cola):
    tamañoCola = cola.size()
    femenino = False

    for i in range(tamañoCola):
        personaje = cola.on_front()
        if personaje[2].lower() == "f": 
            print(f"Nombre la superhéroe: {personaje[1]}")
            femenino = True
        cola.move_to_end()

    if not femenino:
        print("No hay superhéroes femeninos en la cola.")


# C. Mostrar los nombres de los personajes masculinos.
def superheroesMasculinos(cola):
    tamañoCola = cola.size()
    masculino = False

    for i in range(tamañoCola):
        personaje = cola.on_front()
        if personaje[2].lower() == "m": 
            print(f"Nombre del personaje: {personaje[0]}")
            masculino = True
        cola.move_to_end()

    if not masculino:
        print("No hay superhéroes femeninos en la cola.")


# D. Determinar el nombre del superhéroe del personaje Scott Lang.
def scottLang(cola):
    tamañoCola = cola.size()
    scott = False

    for i in range(tamañoCola):
        personaje = cola.on_front()
        if personaje[0].lower() == "scott lang": 
            print(f"Nombre del superhéroe del personaje Scott Lang: {personaje[1]}")
            scott = True
        cola.move_to_end()

    if not scott:
        print("El personaje de Scott Lang no está en la cola.")

# E. Mostrar todos los datos de los superhéroes o personaje cuyos nombres comienzan con la letra S.
def nombresConS(cola):
    tamañoCola = cola.size()
    nombre = False

    for i in range(tamañoCola):
        personaje = cola.on_front()
        
        if personaje[0][0].lower() == "s" or personaje[1][0].lower() == "s":
            print(f"Nombre del superhéroe: {personaje[0]} / Nombre del personaje: {personaje[1]} / Género: {personaje[2]}")
            nombre = True
        cola.move_to_end()
    
    if not nombre:
        print("No hay nombres de personajes ni de superhéroes que comiencen con 'S'")


# F. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
def carolDanvers(cola):
    tamañoCola = cola.size()
    carol = False

    for i in range(tamañoCola):
        personaje = cola.on_front()  
        if personaje[0].lower() == "carol danvers": 
            print(f"Nombre del superhéroe del personaje Carol Danvers: {personaje[1]}")
            carol = True
        cola.move_to_end()

    if not carol:
        print("El personaje de Carol Danvers no está en la cola.")



#MENÚ
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrarMenu():
    print("-----> MENÚ PRINCIPAL DE LA COLA PARA PERSONAJES DE PELICULAS DE MARVEL CINEMATIC UNIVERSE <-----")
    print("-Opciones:")
    print("1. Mostrar todos los personajes.")
    print("2. Mostrar el nombre del personaje de la superhéroe Capitana Marvel.")
    print("3. Mostrar los nombres de los superhéroes femeninos.")
    print("4. Mostrar los nombres de los personajes masculinos.")
    print("5. Mostrar el nombre del superhéroe del personaje Scott Lang.")
    print("6. Mostrar todos los datos de los superhéroes o personaje cuyos nombres comienzan con la letra 'S'.")
    print("7. Mostrar el nombre del superhéroe del personaje Carol Danvers.")
    print("8. Salir.")


opcion = 0
while opcion != 8:
    limpiar_consola()
    mostrarMenu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        limpiar_consola()
        personajesMarvel.show()
        input("Presione Enter para continuar...")
    elif opcion == 2:
        limpiar_consola()
        capitanaMarvel(personajesMarvel)
        input("Presione Enter para continuar...")
    elif opcion == 3:
        limpiar_consola()
        superheroesFemeninos(personajesMarvel)
        input("Presione Enter para continuar...")
    elif opcion == 4:
        limpiar_consola()
        superheroesMasculinos(personajesMarvel)
        input("Presione Enter para continuar...")
    elif opcion == 5:
        limpiar_consola()
        scottLang(personajesMarvel)
        input("Presione Enter para continuar...")
    elif opcion == 6:
        limpiar_consola()
        nombresConS(personajesMarvel)
        input("Presione Enter para continuar...")
    elif opcion == 7:
        limpiar_consola()
        carolDanvers(personajesMarvel)
        input("Presione Enter para continuar...")
    elif opcion == 8:
        limpiar_consola()
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente de nuevo.")





