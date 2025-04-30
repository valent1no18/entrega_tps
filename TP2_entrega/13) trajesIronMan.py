#13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
#verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
#usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
#las siguientes actividades:


from stack import Stack

trajesiIronMan = Stack()

trajes = [
    ("Mark I", "Iron Man", "Dañado"),
    ("Mark II", "Iron Man", "Impecable"),
    ("Mark III", "Iron Man", "Impecable"),
    ("Mark IV", "Iron Man 2", "Destruido"),
    ("Mark V", "Iron Man 2", "Dañado"),
    ("Mark VI", "Iron Man 2", "Impecable"),
    ("Mark XL (Shotgun)", "Iron Man 3", "Impecable"),
    ("Mark XLII", "Iron Man 3", "Dañado"),
    ("Mark XXXVIII (Igor)", "Iron Man 3", "Dañado"),
    ("Mark XLIV (Hulkbuster)", "Vengadores: La era de Ultrón", "Destruido"),
    ("Mark XLVII", "Spider-Man: Homecoming", "Impecable"),
    ("Mark XLVI", "Capitan America: Civil War" , "Dañado"),
    ("Mark L", " Vengadores: Infinity War", "Destruido")
]


for traje in trajes:
    trajesiIronMan.push(traje)

#A) determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
#además mostrar el nombre de dichas películas;

def hulkbuster(pila):
    pilaAux = Stack()
    trajeEncontrado = None 

    while pila.size() > 0:
        traje = pila.pop()
        pilaAux.push(traje)
        if traje[0] == "Mark XLIV (Hulkbuster)": 
            trajeEncontrado = traje
            break 

    while pilaAux.size() > 0:
        pila.push(pilaAux.pop())

    if trajeEncontrado:
        print(f"Modelo encontrado: Mark XLIV (Hulkbuster), en la película: {trajeEncontrado[1]}.")
    else:
        print("El modelo 'Mark XLIV (Hulkbuster)' no está en la pila.")

# B) mostrar los modelos que quedaron dañados, sin perder información de la pila.

def modelosDañados(pila):
    pilaAux = Stack()
    trajesDañados = []
    
    while pila.size() > 0:
        traje = pila.pop()
        pilaAux.push(traje)
        if traje[2] ==  "Dañado":
              trajesDañados.append(traje)

    if trajesDañados:
        for traje in trajesDañados:
            print(f"Modelo: {traje[0]}")
    else:
        print("No hay modelos de los trajes que estén dañados.")

    while pilaAux.size() > 0:
        pila.push(pilaAux.pop())

# C) eliminar los modelos de los trajes destruidos mostrando su nombre.

def modelosDestruidos(pila):
    pilaAux = Stack()
    destruido = False

    while pila.size() > 0:
        traje = pila.pop()
    
        if traje[2] ==  "Destruido":
              print(f"Modelo: {traje[0]}")
              destruido = True
        else:
            pilaAux.push(traje)
            
    if destruido == False:
        print("No hay modelos de los trajes que estén destruidos.")

    while pilaAux.size() > 0:
        pila.push(pilaAux.pop())

# D) un modelo de traje puede usarse en más de una película y en una película se pueden usar
#más de un modelo de traje, estos deben cargarse por separado.

def cargarNuevosModelos(pila, nameExtra, movieExtra, stateExtra):
    pilaAux = Stack()
    newModel = (nameExtra, movieExtra, stateExtra)
    yaCargado = False

    while pila.size() > 0:
        traje = pila.pop()
        pilaAux.push(traje)
        if traje == newModel:
            yaCargado = True

    if not yaCargado:
        pila.push(newModel)
        print(f"Modelo agregado: {newModel[0]}, Película: {newModel[1]}, Estado: {newModel[2]}.")

    while pilaAux.size() > 0:
        pila.push(pilaAux.pop())

# E) agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
#repetidos en una misma película;

def cargarModeloEspecifico(pila, name, movie, state):
    pilaAux = Stack()
    specificModel = (name, movie, state)
    existe = False

    while pila.size() > 0:
        traje = pila.pop()
        pilaAux.push(traje)
        if traje[0] == name and traje[1] == movie and traje[2] == state:
            existe = True

    if not existe:
        pila.push(specificModel)
        print(f"Modelo agregado: {specificModel[0]}, Película: {specificModel[1]}, Estado: {specificModel[2]}.")
    else:
        print("Este modelo ya fue cargado antes en la pila.")

    while pilaAux.size() > 0:
        pila.push(pilaAux.pop())
    
# F) mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
#“Capitan America: Civil War”.

def mostrarNombresTrajes(pila):
    pilaAux = Stack()
    
    while pila.size() > 0:
        traje = pila.pop()
        pilaAux.push(traje)
        if  traje[1] == "Spider-Man: Homecoming":
            print(f"El modelo de la película Spider-Man: Homecoming es: {traje[0]}.")
        elif traje[1] == "Capitan America: Civil War":
            print(f"El modelo de la película Capitan America: Civil War es: {traje[0]}.")

    while pilaAux.size() > 0:
        pila.push(pilaAux.pop())










#MENÚ
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrarMenu():
    print("-----> MENÚ PRINCIPAL DE LA PILA PARA TRAJES DE IRON MAN <-----")
    print("-Opciones:")
    print("1. Mostrar todos los modelos de trajes")
    print("2. Buscar el modelo Mark XLIV (Hulkbuster)")
    print("3. Cargar modelos")
    print("4. Salir")

def mostrarSubMenu1():
    print("---> OPCIONES PARA MOSTRAR MODELOS <---")
    print("1. Mostrar todos los modelos de trajes cargados")
    print("2. Mostrar los modelos que quedaron dañados")
    print("3. Mostrar los modelos destruidos que quedaron eliminados")
    print("4. Mostrar los modelos utilizados en las películas “Spider-Man: Homecoming” y “Capitan America: Civil War” ")
    print("5. Volver al menú")

def mostrarSubMenu2():
    print("---> OPCIONES PARA CARGAR MODELOS <---")
    print("1. Cargar a la pila el modelo Mark LXXXV")
    print("2. Cargar otros modelos a la pila")
    print("3. Volver al menú")

opcion = 0
while opcion != 4:
    limpiar_consola()
    mostrarMenu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        subopcion = 0
        while subopcion != 5:
            limpiar_consola()
            mostrarSubMenu1()
            subopcion = int(input("Seleccione una opción del submenú: "))
            if subopcion == 1:
                limpiar_consola()
                trajesiIronMan.show()
                input("Presione Enter para continuar...")
            elif subopcion == 2:
                limpiar_consola()
                print("LISTA DE MODELOS DAÑADOS: ")
                modelosDañados(trajesiIronMan)
                input("Presione Enter para continuar...")
            elif subopcion == 3:
                limpiar_consola()
                print("LISTA DE MODELOS DESTRUIDOS A ELIMINAR DE LA PILA: ")
                modelosDestruidos(trajesiIronMan)
                input("Presione Enter para continuar...")
            elif subopcion == 4:
                limpiar_consola()
                mostrarNombresTrajes(trajesiIronMan)
                input("Presione Enter para continuar...")
            elif subopcion == 5:
                limpiar_consola()
                print("Volviendo al menú principal...")
            else:
                print("Opción no válida. Intente de nuevo.")
    elif opcion == 2:
        limpiar_consola()
        hulkbuster(trajesiIronMan)
        input("Presione Enter para continuar...")
    elif opcion == 3:
        subopcion = 0
        while subopcion != 3:
            limpiar_consola()
            mostrarSubMenu2()
            subopcion = int(input("Seleccione una opción del submenú: "))
            if subopcion == 1:
                limpiar_consola()
                cargarModeloEspecifico(trajesiIronMan, "Mark LXXXV", "Avengers: Endgame", "Impecable")
                input("Presione Enter para continuar...")
            elif subopcion == 2:
                limpiar_consola()
                trajeExtra = input("Modelo de traje nuevo: ")
                peliculaExtra = input("Película del nuevo modelo cargado: ")
                estadoExtra = input("Estado en el que quedó el traje: ")
                cargarNuevosModelos(trajesiIronMan, trajeExtra, peliculaExtra, estadoExtra)
                input("Presione Enter para continuar...")
            elif subopcion == 3:
                print("Volviendo al menú principal...")
            else:
                print("Opción no válida. Intente de nuevo.")
    elif opcion == 4:
        limpiar_consola()
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente de nuevo.")


