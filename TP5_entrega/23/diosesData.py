class CriaturasYDioses:
    def __init__(self, criatura, derrotadoPor, descripcion, capturada):
        self.criatura = criatura
        self.derrotadoPor = derrotadoPor
        self.descripcion = descripcion
        self.capturada = capturada
    def __str__(self):
        return f"Criatura: {self.criatura} / Derrotado por: {self.derrotadoPor} / Breve descipción: {self.descripcion} / Capturada por: {self.capturada}"


criaturas = [
    ("Ceto", "-", "Diosa primordial del mar y madre de monstruos marinos.", "Teseo"),
    ("Tifón", "Zeus", "Monstruo más temido de la mitología griega, padre de todos los monstruos.", "Heracles"),
    ("Equidna", "Argos Panoptes", "Mitad mujer, mitad serpiente, madre de muchas criaturas míticas.", "Teseo"),
    ("Dino", "-", "Una de las Grayas, hermanas que compartían un solo ojo y un diente.", "Atalanta"),
    ("Pefredo", "-", "Otra de las Grayas, conocida por su sabiduría y astucia.", "-"),
    ("Enio", "-", "La tercera de las Grayas, asociada con la destrucción y el terror.", "Heracles"),
    ("Escila", "-", "Monstruo marino con múltiples cabezas que devoraba marineros.", "-"),
    ("Caribdis", "-", "Monstruo marino que creaba remolinos gigantes en el estrecho de Mesina.", "-"),
    ("Euríale", "-", "Una de las Gorgonas inmortales, hermana de Medusa.", "-"),
    ("Esteno", "-", "Otra Gorgona inmortal, conocida por su fuerza y ferocidad.", "Teseo"),
    ("Medusa", "Perseo", "La única Gorgona mortal, con serpientes en la cabeza y mirada petrificante.", "-"),
    ("Ladón", "Heracles", "Dragón que custodiaba las manzanas doradas del jardín de las Hespérides.", "Hermes"),
    ("Águila del Cáucaso", "-", "Águila que devoraba el hígado de Prometeo como castigo eterno.", "-"),
    ("Quimera", "Belerofonte", "Criatura híbrida con cabeza de león, cuerpo de cabra y cola de serpiente.", "Medea"),
    ("Hidra de Lerna", "Heracles", "Serpiente de múltiples cabezas que se regeneraban al ser cortadas.", "-"),
    ("León de Nemea", "Heracles", "León con piel impenetrable, derrotado por Heracles en su primer trabajo.", "Apolo"),
    ("Esfinge", "Edipo", "Criatura con cuerpo de león, alas de ave y rostro de mujer, famosa por su enigma.", "-"),
    ("Dragón de la Cólquida", "-", "Dragón que custodiaba el vellocino de oro en la mitología griega.", "-"),
    ("Cerbero", "-", "Perro de tres cabezas que guardaba la entrada al inframundo.", "-"),
    ("Cerda de Cromión", "Teseo", "Jabalí monstruoso que aterrorizaba la región de Cromión.", "-"),
    ("Ortro", "Heracles", "Perro de dos cabezas, hermano de Cerbero, guardián del ganado de Gerión.", "-"),
    ("Toro de Creta", "Teseo", "Toro enviado por Poseidón, padre del Minotauro.", "-"),
    ("Jabalí de Calidón", "Atalanta", "Jabalí gigante enviado por Artemisa para castigar a Calidón.", "-"),
    ("Carcinos", "-", "Cangrejo gigante que ayudó a la Hidra de Lerna en su lucha contra Heracles.", "-"),
    ("Gerión", "Heracles", "Gigante de tres cuerpos que poseía un rebaño de ganado rojo.", "-"),
    ("Cloto", "-", "Una de las Moiras, hilaba el hilo de la vida.", "-"),
    ("Láquesis", "-", "Otra de las Moiras, medía el hilo de la vida.", "-"),
    ("Átropos", "-", "La última de las Moiras, cortaba el hilo de la vida.", "-"),
    ("Minotauro de Creta", "Teseo", "Criatura con cuerpo de hombre y cabeza de toro, encerrada en el laberinto.", "-"),
    ("Harpías", "-", "Criaturas aladas con rostro de mujer, conocidas por robar comida.", "-"),
    ("Argos Panoptes", "Hermes", "Gigante de cien ojos, guardián de Io.", "-"),
    ("Aves del Estínfalo", "-", "Aves con picos y plumas de metal, derrotadas por Heracles.", "-"),
    ("Talos", "Medea", "Autómata de bronce que protegía la isla de Creta.", "-"),
    ("Sirenas", "-", "Criaturas mitad mujer, mitad ave, que atraían a los marineros con su canto.", "-"),
    ("Pitón", "Apolo", "Serpiente gigante que custodiaba el oráculo de Delfos.", "-"),
    ("Cierva de Cerinea", "-", "Cierva sagrada de Artemisa, capturada por Heracles.", "-"),
    ("Basilisco", "-", "Criatura con mirada mortal, conocida como el rey de las serpientes.", "-"),
    ("Jabalí de Erimanto", "-", "Jabalí capturado por Heracles como uno de sus trabajos.", "-")
]
