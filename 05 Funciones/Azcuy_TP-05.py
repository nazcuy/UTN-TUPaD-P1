"""1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""
"""
#Funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Programa Principal
imprimir_hola_mundo()
"""
"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""
"""
#Funciones
def saludar_usuario(nombre):
    return(f"Hola {nombre}!")

#Programa Principal
nombre_nuevo = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_nuevo)
print(saludo)
"""
"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
dir los datos al usuario y llamar a esta función con los valores in-
gresados."""
"""
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nom_nvo = input("Ingrese su nombre: ")
ape_nvo = input("Ingrese su apellido: ")
edad_nva = input("Ingrese su edad: ")
resid_nva = input ("Ingrese su lugar de residencia: ")
informacion_personal(nom_nvo, ape_nvo, edad_nva, resid_nva)
"""

