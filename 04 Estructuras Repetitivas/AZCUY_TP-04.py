#TRABAJO PRÁCTICO NÚMERO 4 - AZCUY NICOLÁS DNI 33.368.267

"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""
for i in range (101):
    print(i)

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""
num = input("Escriba un número entero para conocer cuántos dígitos tiene: ")
print(len(num))

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""
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

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0."""
total = 0
numer = int(input("Ingrese un número: "))
while numer != 0:
    total += numer
    numer = int(input("Ingrese otro número: "))
print("La suma total es:", total)

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
import random
num_aleatorio = random.randint(0,9)
numero = int(input("Ingrese un número del 0 al 9: "))
intentos = 1
while num_aleatorio != numero:
    numero = int(input("Número incorrecto. Ingrese otro número: "))
    intentos += 1
print("Acertaste en el intento número:",intentos)

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""
for x in range (0, 101, 2):
    print(x)

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""
nro = int(input("Ingrese un número: "))
tot = 0
y = 0
while y <= nro:
    tot += y
    y += 1
print("La suma total es:", tot)

"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""
n = 0
par = 0
impar = 0
negat = 0
posit = 0

for i in range(1, 101):
    n = int(input("Escriba un número: "))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    if n < 0:
        negat += 1
    else:
        posit += 1

print("Cantidad de números pares:", par)
print("Cantidad de números impares:", impar)
print("Cantidad de números positivos:", posit)
print("Cantidad de números negativos:", negat)

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""
lista = 0
cont = 0
sumador = 0
for i in range(1, 101):
    lista = int(input("Escriba un número: "))
    cont += 1
    sumador += lista
prom = sumador / cont
print("La media de los números ingresados es: ",prom)

"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""
numusuario = input("Ingrese un número: ")
numinvertido = ""
caracterestot = len(numusuario)
for i in range(caracterestot-1, -1, -1):
    numinvertido += numusuario[i]
print(numinvertido)