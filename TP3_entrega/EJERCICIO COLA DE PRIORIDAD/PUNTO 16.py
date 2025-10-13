# 16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
# siguiente situación:

from heap import HeapMax


colaPrioridad = HeapMax()
# a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
colaPrioridad.arrive("Juan", 1)
colaPrioridad.arrive("Ana", 1)
colaPrioridad.arrive("Sergio", 1)


# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
print(f"[+] Primer documento de la cola: {colaPrioridad.attention()[1]}")
print()

# c. cargue dos documentos del staff de TI.
colaPrioridad.arrive("Marcos", 2)
colaPrioridad.arrive("Lucia", 2)


# d. cargue un documento del gerente.
colaPrioridad.arrive("Nicolas", 3)

# e. imprima los dos primeros documentos de la cola.
print(f"[+] Documento de la cola: {colaPrioridad.attention()[1]}")
print(f"[+] Documento de la cola: {colaPrioridad.attention()[1]}")
print()

# f. cargue dos documentos de empleados y uno de gerente.
colaPrioridad.arrive("Marcos", 1)
colaPrioridad.arrive("Lucas", 1)
colaPrioridad.arrive("Sofia", 3)

# g. imprima todos los documentos de la cola de impresión.
print("[+] Lista de todos los documentos de la cola:")
while colaPrioridad.size() > 0:
    print(f"[+] Documento de la cola completa: {colaPrioridad.attention()[1]}")