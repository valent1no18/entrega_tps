class Jedi:
    def __init__(self, name, maestros, coloresSable, especie):
        self.name = name
        self.maestros = maestros  
        self.coloresSable = coloresSable 
        self.especie = especie

    def __str__(self):
        return f"{self.name} - Especie: {self.especie} - Maestros: {self.maestros} - Colores de sable: {self.coloresSable}"
    

jedis = [
    ("Luke Skywalker", "Yoda", "azul", "Humano"),
    ("Anakin Skywalker", "Obi-Wan Kenobi", "rojo", "twi'lek"),
    ("Obi-Wan Kenobi", "Qui-Gon Jinn", "violeta", "Humano"),
    ("Yoda", None, "verde y rojo", "Desconocida"),
    ("Ahsoka Tano", "Luke Skywalker", "blanco", "Togruta"),
    ("Mace Windu", "Cyslin Myr", "violeta y azul", "Humano"),
    ("Kit Fisto", "Leia Organa", "amarillo", "Humano")
]

def order_by_name(jedi):
    return jedi.name

def order_by_especie(jedi):
    return jedi.especie

def order_by_maestros(jedi):
    return jedi.maestros