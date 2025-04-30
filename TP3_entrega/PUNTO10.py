#Ejercicio 10: Notificaciones de redes sociales de un Smartphone. 
#Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
#de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
#resolver las siguientes actividades:


from queue_ import Queue
from stack import Stack

appSmartphone = Queue()
pilaTemporal = Stack()

notificaciones = [
    ("21:00", "Instagram", "Nuevo seguidor"),
    ("12:00", "WhatsApp", "Nuevo mensaje"),
    ("16:00", "Twitter", "Python publicó esto ..."),
    ("09:30", "Facebook", "Solicitud de amistad"),
    ("15:40", "Tiktok", "A un usuario le gustó el video que compartiste"),
    ("02:35", "Twitter", "Nuevo seguidor"),
    ("03:30", "Twitter", "Python comentó esto ..."),
    ("18:15", "Facebook", "Me gusta")
]

for notificacion in notificaciones:
    appSmartphone.arrive(notificacion)

# A. Escribir una función que elimine de la cola todas las notificaciones de Facebook.
def noticacionesFacebook(cola):
    tamañoCola = cola.size()  
    eliminados = 0 

    for i in range(tamañoCola):
        notificacion = cola.attention() 
        if notificacion[1] != "Facebook": 
            cola.arrive(notificacion)
        else:
            eliminados += 1  


    if eliminados == 0:
        print("No hay notificaciones de Facebook en el Smartphone.")
    else:
        print(f"Se eliminaron {eliminados} notificaciones de Facebook.")


# B. Escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
#la palabra ‘Python’, si perder datos en la cola.
def notificacionesTwitter(cola):
    tamañoCola = cola.size()
    notificacionTwitter = False

    for i in range(tamañoCola):
        notificacion = cola.on_front() 
        if notificacion[1].lower() == "twitter" and "python" in notificacion[2].lower():
            print(f"Contenido del mensaje: {notificacion}")
            notificacionTwitter = True
        cola.move_to_end()

    if not notificacionTwitter:
        print("No hay notificaciones de Twitter que tengan la palabra 'Python'.")
    

# C. Utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
#11:43 y las 15:57, y determinar cuántas son.
def stackTemporal(cola):
    tamañoCola = cola.size()
    pila = Stack()
    notificacionRecibida = False
    contador = 0

    for i in range(tamañoCola):
        notificacion = cola.attention() 
        if notificacion[0] >= "11:43" and notificacion[0] <= "15:57":
            pila.push(notificacion)
            notificacionRecibida = True
            contador += 1
        cola.arrive(notificacion)

    if not notificacionRecibida:
        print("No hubo notificaciones recibidas entre las 11:43 y las 15:57.")
    else:
        print("Notificaciones recibidas entre las 11:43 y las 15:57:")
        pila.show()
        print(f"Cantidad de estas notificaciones: {contador}")


#MENÚ
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrarMenu():
    print("-----> MENÚ PRINCIPAL DE LA COLA PARA NOTIFICACIONES DE REDES SOCIALES DE UN SMARTPHONE <-----")
    print("-Opciones:")
    print("1. Mostrar todas las notificaciones del Smartphone.")
    print("2. Mostrar notificaciones específicas del Smartphone.")
    print("3. Eliminar notificaciones de Facebook del Smartphone.")
    print("4. Salir.")

def mostrarSubMenu1():
    print("---> OPCIONES PARA MOSTRAR LAS NOTIFICACIONES <---")
    print("1. Notificaciones de Twitter que en su mensaje incluya la palabra ‘Python’.")
    print("2. Notificaciones producidas entre las 11:43 y las 15:57.")
    print("3. Volver al menú")

opcion = 0
while opcion != 4:
    limpiar_consola()
    mostrarMenu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        limpiar_consola()
        appSmartphone.show()
        input("Presione Enter para continuar...")
    elif opcion == 2:
        subopcion = 0
        while subopcion != 3:
            limpiar_consola()
            mostrarSubMenu1()
            subopcion = int(input("Seleccione una opción del submenú: "))
            if subopcion == 1:
                limpiar_consola()
                notificacionesTwitter(appSmartphone)
                input("Presione Enter para continuar...")
            elif subopcion == 2:
                limpiar_consola()
                stackTemporal(appSmartphone)
                input("Presione Enter para continuar...")
            elif subopcion == 3:
                limpiar_consola()
                print("Volviendo al menú principal...")
            else:
                print("Opción no válida. Intente de nuevo.")
    elif opcion == 3:
        limpiar_consola()
        noticacionesFacebook(appSmartphone)
        input("Presione Enter para continuar...")
    elif opcion == 4:
        limpiar_consola()
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente de nuevo.")


