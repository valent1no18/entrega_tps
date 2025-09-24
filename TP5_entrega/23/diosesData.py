class CriaturasYDioses:
    def __init__(self, criatura, derrotadoPor, descripcion, capturada):
        self.criatura = criatura
        self.derrotadoPor = derrotadoPor
        self.descripcion = descripcion
        self.capturada = capturada
    def __str__(self):
        return f"Criatura: {self.criatura} / Derrotado por: {self.derrotadoPor} / Breve descipción: {self.descripcion} / Capturada por: {self.capturada}"


criaturas = [
    ("Ceto", "-", "", "Teseo"),
    ("Tifón", "Zeus", "", "Heracles"),
    ("Equidna", "Argos Panoptes", "", "Teseo"),
    ("Dino", "-", "", "Atalanta"),
    ("Pefredo", "-", "", "-"),
    ("Enio", "-", "", "Heracles"),
    ("Escila", "-", "", "-"),
    ("Caribdis", "-", "", "-"),
    ("Euríale", "-", "", "-"),
    ("Esteno", "-", "", "Teseo"),
    ("Medusa", "Perseo", "", "-"),
    ("Ladón", "Heracles", "", "Hermes"),
    ("Águila del Cáucaso", "-", "", "-"),
    ("Quimera", "Belerofonte", "", "Medea"),
    ("Hidra de Lerna", "Heracles", "", "-"),
    ("León de Nemea", "Heracles", "", "Apolo"),
    ("Esfinge", "Edipo", "", "-"),
    ("Dragón de la Cólquida", "-", "", "-"),
    ("Cerbero", "-", "", "-"),
    ("Cerda de Cromión", "Teseo", "", "-"),
    ("Ortro", "Heracles", "", "-"),
    ("Toro de Creta", "Teseo", "", "-"),
    ("Jabalí de Calidón", "Atalanta", "", "-"),
    ("Carcinos", "-", "", "-"),
    ("Gerión", "Heracles", "", "-"),
    ("Cloto", "-", "", "-"),
    ("Láquesis", "-", "", "-"),
    ("Átropos", "-", "", "-"),
    ("Minotauro de Creta", "Teseo", "", "-"),
    ("Harpías", "-", "", "-"),
    ("Argos Panoptes", "Hermes", "", "-"),
    ("Aves del Estínfalo", "-", "", "-"),
    ("Talos", "Medea", "", "-"),
    ("Sirenas", "-", "", "-"),
    ("Pitón", "Apolo", "", "-"),
    ("Cierva de Cerinea", "-", "", "-"),
    ("Basilisco", "-", "", "-"),
    ("Jabalí de Erimanto", "-", "", "-")
]
