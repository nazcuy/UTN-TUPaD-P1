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
    for i in range(num1 + 1, num2):
        suma += i
else:
    for i in range(num2 + 1, num1):
        suma += i
print (suma)
"""
"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
total = 0
num = int(input("Ingrese un número: "))
while num != 0:
    total += num
    num = int(input("Ingrese otro número: "))
print("La suma total es:", total)
"""
