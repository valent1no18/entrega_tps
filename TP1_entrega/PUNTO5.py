#Ejercicio 5: Conversor de números romanos a decimales
#Desarrollar una función que permita convertir un número romano en un número decimal.

diccionario_numromanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman(string):
    if not string: # Si la cadena esta vacia
        return 0
    decimal = diccionario_numromanos[string[0]] 
    if len(string) > 1:
        if decimal < diccionario_numromanos[string[1]]:
            return -decimal + roman(string[1:])
    return decimal + roman(string[1:]) # Llama la cadena a partir del 2° caracter


string = input("Ingrese un número romano: ") # Solicita el número romano al usuario
print(f"El número romano es: {string}") # Imprime el número romano ingresado
print(f"El número romano en decimal es: {roman(string)}") # Imprime el número romano convertido a decimal


