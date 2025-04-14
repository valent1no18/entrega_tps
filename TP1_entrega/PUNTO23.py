#Ejercicio 22: Mochila Jedi
#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
#c. Utilizar un vector para representar la mochila.

#FUNCIÓN RECURSIVA

def usarlafuerza(mochila, objeto_a_buscar, contadordeobjetos):
    """
    Función que busca un objeto en la mochila Jedi usando la fuerza.
    La función utiliza recursividad para buscar el objeto en la lista de objetos de la mochila.

    """
   
    if mochila[0] == objeto_a_buscar:
        print(f"¡Encontramos nuestro {objeto_a_buscar} en la mochila!")
        return contadordeobjetos + 1
    elif len(mochila) == 1:
        print(f"¡No encontramos nuestro {objeto_a_buscar} en la mochila y esta quedo vacía!") 
        return contadordeobjetos 
    else:
        print(f"{mochila[0]} no es el que buscamos, seguimos buscando...")
        input("<<Presione enter para continuar buscando>>")
        return usarlafuerza(mochila[1:], objeto_a_buscar, contadordeobjetos + 1)
        
        


mochila = ["Comunicador", "Respirador", "Botiquin", "Sable de Luz" , "Objetos personales", "Comida", "Agua", "Municiones", "Cargador", "Linterna"] 
objeto_a_buscar = "Sable"
contador = 0 

print("La mochila Jedi contiene los siguientes objetos: ", mochila)
print("------------------------------------------------")
print("Buscamos en la mochila...")
print(f"Debemos encontrar el {objeto_a_buscar} en la mochila...")

#Para mostrar la cantidad de objetos que se han sacado de la mochila.
contadorfinal = usarlafuerza(mochila, objeto_a_buscar, contador) 
print("Objetos sacados de la mochila: ", contadorfinal)