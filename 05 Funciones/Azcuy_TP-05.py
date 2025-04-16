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
"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
dio como parámetro y devuelva el área del círculo. calcular_peri-
metro_circulo(radio) que reciba el radio como parámetro y devuel-
va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
bas funciones para mostrar los resultados."""
"""
from math import pi
def calcular_area_circulo(radio):
    area = pi * (radio ** 2)    
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    return perimetro

radio_nvo = float(input("Ingrese el radio del círculo: "))
print(f"El area del círculo es: {calcular_area_circulo(radio_nvo):.2f}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio_nvo):.2f}")
"""
"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos-
trar el resultado usando esta función."""
"""
def segundos_a_horas(segundos):
    horas = segundos/3600
    return horas

segundos_usuario = float(input("Ingrese los segundos que transformaremos a horas: "))
print(f"La cantidad de horas es: {segundos_a_horas(segundos_usuario):.2f}")
"""
"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro e imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun-
ción."""
"""
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

num_a_multip = int(input("Ingrese un número: "))
tabla_multiplicar(num_a_multip)
"""
