#TRABAJO PRÁCTICO - AZCUY NICOLÁS - DNI 33.368.267

""" 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”."""
print("Hola Mundo!")



""" 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla."""
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")



""" 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla."""
nombre1 = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre1} {apellido}, tengo {edad} años. Vivo en {residencia}.")



""" 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro."""
radio = input("Coloque el radio: ")
radio = float(radio)
area = (3.1416 * (radio**2))
perimetro = 2 * 3.1416 * radio
print(f"El área del círculo es: {area:.2f}. Y su perímetro es: {perimetro:.2f}.")



""" 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale."""
segundos = float(input("Ingrese una cantidad de segundos: "))
horas = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_finales = segundos_restantes % 60
print(f"Los segundos ingresados equivalen a {int(horas)} horas, {int(minutos)} minutos y {int(segundos_finales)} segundos.")



""" 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número."""
numero = int(input("Ingrese un número por favor: "))
for i in range (1, 11):
    resultado = numero * i
    print(f"{numero} multiplicado por {i} es igual a: {resultado}.")



""" 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos."""
num1 = int(input("Escriba un número entero distinto de cero: "))
num2 = int(input("Escriba un segundo número entero distinto de cero: "))
if num1 == 0 or num2 == 0:
    print("Error al ingresar número.")
else:
    suma = num1 + num2
    resta = num1 - num2
    division = num1 / num2
    multiplicacion = num1 * num2
    
    print(f"La suma de {num1} y {num2} es: {suma}.")
    print(f"La resta de {num1} y {num2} es: {resta}.")
    print(f"La división de {num1} y {num2} es: {division:.2f}.")
    print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}.")



""" 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo: IMC = peso en kg / (altura en m)↑2"""
peso = float(input("Ingrese el peso en kg: "))
alt = float(input("Ingrese la altura en metros: "))
imc = peso / (alt**2)
print(f"El índice de masa corporal es: {imc:.2f}")



""" 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
Temp F = 9/5 * Temp C + 32 """
tempC = float(input("Ingrese la temperatura en grados Celcius: "))
tempF = float((9/5) * tempC + 32)
print(f"{tempC} grados Celsius equivalen a {tempF:.2f} grados Fahrenheit.")



""" 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números."""
numero1 = float(input("Escriba un número: "))
numero2 = float(input("Escriba un segundo número: "))
numero3 = float(input("Escriba un tercer número: "))
prom = (numero1 + numero2 + numero3) / 3
print(f"EL promedio de los 3 números ingresados es: {prom:.2f}")