#Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
#colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
#actividades enumeradas a continuación:

from list_ import List
from jediData import Jedi, jedis, order_by_especie, order_by_name, order_by_maestros

listJedi = List()
listJedi.add_criterion('name', order_by_name)
listJedi.add_criterion('especie', order_by_especie)
listJedi.add_criterion('maestros', order_by_maestros)

for jedi in jedis:
    personaje = Jedi(
        name = jedi[0],
        maestros = jedi[1],
        coloresSable = jedi[2],
        especie = jedi[3]
    )
    listJedi.append(personaje)

# a. listado ordenado por nombre y por especie;
def listadoOrdenado(lista):

    print("Ordenado por nombre: ")
    lista.sort_by_criterion('name')
    lista.show()
    print()
    print("Ordenado por especie: ")
    lista.sort_by_criterion('especie')
    lista.show()

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
def ahsokaAndKit(lista):

    index = lista.search('Ahsoka Tano', 'name')
    index2 = lista.search('Kit Fisto', 'name')

    if index is not None:
        ahsoka = lista[index]
        print("Información de Ahsoka Tano:")
        print(f"Especie: {ahsoka.especie} - Maestros: {ahsoka.maestros} - Colores del sable: {ahsoka.coloresSable}")
    print()
    if index2 is not None:
        kit = lista[index2]
        print("Información de Kit Fisto:")
        print(f"Especie: {kit.especie} - Maestros: {kit.maestros} - Colores del sable: {kit.coloresSable}")


# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
def aprendices(lista):
    yoda = False
    luke = False

    print("Aprendices de Yoda:")
    for jedi in lista:
        if jedi.maestros == "Yoda":
            print(jedi.name)
            yoda = True
    print()
    print("Aprendices de Luke Skywalker:")
    for jedi in lista:
        if jedi.maestros == "Luke Skywalker":
            print(jedi.name)
            luke = True

    if not yoda:
        print("No hay aprendices de Yoda en la lista.")

    if not luke:
        print("No hay aprendices de Luke Skywalker en la lista.")


# d. mostrar los Jedi de especie humana y twi'lek;
def especies(lista):
    humano = False
    twilek = False

    print("Jedi de especie humana:")
    for jedi in lista:
        if jedi.especie == "Humano":
            print(jedi.name)
            humano = True
    print()
    print("Jedi de especie twi'lek:")
    for jedi in lista:
        if jedi.especie == "twi'lek":
            print(jedi.name)
            twilek = True

    if not humano:
        print("No hay humanos en la lista.")


    if not twilek:
        print("No hay humanos en la twi'lek.")

# e. listar todos los Jedi que comienzan con A;
def jediA(lista):
    print("Jedi que comienzan con A:")
    for jedi in lista:
        if jedi.name.startswith('A'):
            print(f"{jedi.name}")

# f. mostrar los Jedi que usaron sable de luz de más de un color;
def coloresDelSable(lista):
    print("Jedi con más de un color de sable:")
    for jedi in lista:
        if jedi.coloresSable:
            colores = [c.strip() for c in jedi.coloresSable.split(' y ')]
            if len(colores) > 1:
                print(f"{jedi.name} - Colores: {colores}")
            

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
def coloresEspecificos(lista):
    print("Jedi que utilizaron un sable de luz amarillo o violeta:")
    for jedi in lista:
        if "amarillo" in jedi.coloresSable or "violeta" in jedi.coloresSable:
            print(f"{jedi.name}")

# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
def padawans(lista):
    quiGon = False
    mace = False

    print("Aprendices de Qui-Gon Jinn:")
    for jedi in lista:
        if jedi.maestros == "Qui-Gon Jinn":
            print(jedi.name)
            quiGon = True

    print()
    print("Aprendices de Mace Windu:")
    for jedi in lista:
        if jedi.maestros == "Mace Windu":
            print(jedi.name)
            mace = True

    if not quiGon:
        print("No hay aprendices de Qui-Gon Jin en la lista.")

    if not mace:
        print("No hay aprendices de Mace Windu en la lista.")


listadoOrdenado(listJedi)
print()
ahsokaAndKit(listJedi)
print()
aprendices(listJedi)
print()
especies(listJedi)
print()
jediA(listJedi)
print()
coloresDelSable(listJedi)
print()
coloresEspecificos(listJedi)
print()
padawans(listJedi)
