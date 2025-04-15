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
