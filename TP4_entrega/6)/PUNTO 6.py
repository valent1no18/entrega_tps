# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:

from list_ import List
from superheroesComicData import Superhero, superheroes, order_by_name

listSuperheroes = List()
listSuperheroes.add_criterion('name', order_by_name)


for superhero in superheroes:
    hero = Superhero(
        name = superhero[0],
        año = superhero[1],
        casaComic = superhero[2],
        shortBio = superhero[3],
    )
    listSuperheroes.append(hero)

# a. eliminar el nodo que contiene la información de Linterna Verde.
print("PERSONAJE ELIMINADO DE LA LISTA: ")
print(listSuperheroes.delete_value('Linterna Verde', 'name'))
print()

# b. mostrar el año de aparición de Wolverine;
def añoWolverine(lista):
    index = lista.search('Wolverine', 'name')
    if index:
        print(f"AÑO DE APARICION DE WOLVERINE: {lista[index].año}")
    else:
        print("EL SUPERHEROE WOLVERINE NO ESTA EN LA LISTA.")

# c. cambiar la casa de Dr. Strange a Marvel;
def cambiarCasa(lista):
    index = lista.search('Doctor Strange', 'name')
    if index:
        print(f"CASA DEL DOCTOR STRANGE: {lista[index].casaComic}")
        lista[index].casaComic = "Marvel Comics"
        print(f"CASA DEL DOCTOR STRANGE (ACTUALIZADA): {lista[index].casaComic}")
    else:
        print('EL SUPERHEROE DOCTOR STRANGE NO ESTA EN LA LISTA.')

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
def biografias(lista):
    print("SUPERHEROES CON TRAJE O ARMADURA:")
    for superhero in lista:
        if 'armadura' in superhero.shortBio or "traje" in superhero.shortBio:
            print(superhero)

#e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
#sea anterior a 1963;
def yearsBefore1963(lista):
    print("SUPERHEROES CON AÑOS DE APARICION ANTERIORES A 1963:")
    for superheroe in lista:
        if superheroe.año < 1963:
            print(f"Nombre del superheroe: {superheroe.name} - Fecha de aparición: {superheroe.año}")

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
def capitanaMarvelAndMujerMaravilla(lista):
    for superheroe in lista:
        if superheroe.name == "Capitana Marvel":
            print(f"CASA DE LA CAPITANA MARVEL: {superheroe.casaComic}")
        elif superheroe.name == "Mujer Maravilla":
            print(f"CASA DE LA MUJER MARAVILLA: {superheroe.casaComic}")

# g. mostrar toda la información de Flash y Star-Lord;
def flashAndStarLord(lista):
    for superheroe in lista:
        if superheroe.name == "Flash":
            print("INFORMACION DE FLASH:")
            print(f"Casa: {superheroe.casaComic}, Año: {superheroe.año}, Bibliografia: {superheroe.shortBio}")
        elif superheroe.name == "Star-Lord":
            print()
            print("INFORMACION DE STAR-LORD:")
            print(f"Casa: {superheroe.casaComic}, Año: {superheroe.año}, Bibliografia: {superheroe.shortBio}")


# h. listar los superhéroes que comienzan con la letra B, M y S;
def namesBMS(lista):
    for superhero in lista:
        if superhero.name.startswith(('B', 'M', 'S')):
            print(superhero)

# i. determinar cuántos superhéroes hay de cada casa de comic.
def houses(lista):
    cantMarvel = 0
    cantDC = 0
    for superheroe in lista:
        if superheroe.casaComic == "DC Comics":
            cantDC += 1
        elif superheroe.casaComic == "Marvel Comics":
            cantMarvel += 1

    print(f"CANTIDAD DE SUPERHEROES DE LA CASA DC COMICS: {cantDC}")
    print(f"CANTIDAD DE SUPERHEROES DE LA CASA MARVEL COMICS: {cantMarvel}")


#listSuperheroes.show()
añoWolverine(listSuperheroes)
print()
cambiarCasa(listSuperheroes)
print()
biografias(listSuperheroes)
print()
yearsBefore1963(listSuperheroes)
print()
capitanaMarvelAndMujerMaravilla(listSuperheroes)
print()
flashAndStarLord(listSuperheroes)
print()
print("SUPERHEROES CUYO NOMBRE EMPIEZAN CON B, M Y/O S:")
namesBMS(listSuperheroes)
print()
houses(listSuperheroes)