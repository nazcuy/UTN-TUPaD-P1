#TRABAJO PRÁCTICO NÚMERO 4 - AZCUY NICOLÁS DNI 33.368.267

"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range (101):
    print(i)
"""
"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
num = input("Escriba un número entero para conocer cuántos dígitos tiene: ")
print(len(num))
"""
"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Escriba un número: "))
num2 = int(input("Escriba otro número: "))
suma = 0
if num1 < num2:
    for x in range(num1 + 1, num2):
        suma += x
else:
    for x in range(num2 + 1, num1):
        suma += x
print (suma)
"""
"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
total = 0
numer = int(input("Ingrese un número: "))
while numer != 0:
    total += numer
    numer = int(input("Ingrese otro número: "))
print("La suma total es:", total)
"""
"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
num_aleatorio = random.randint(0,9)
numero = int(input("Ingrese un número del 0 al 9: "))
intentos = 1
while num_aleatorio != numero:
    numero = int(input("Número incorrecto. Ingrese otro número: "))
    intentos += 1
print("Acertaste en el intento número:",intentos)
"""
"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
for x in range (0, 101, 2):
    print(x)
"""
"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""
nro = int(input("Ingrese un número: "))
tot = 0
y = 0
while y <= nro:
    tot += y
    y =+ 1
print("La suma total es:", tot)