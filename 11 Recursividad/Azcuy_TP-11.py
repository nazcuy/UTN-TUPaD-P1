"""
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""
"""
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

num_usuario = int(input("Ingrese un número: "))
print(f"Los factoriales desde el 1 hasta el {num_usuario} son:\n")
for i in range(1, num_usuario + 1):
    print(f"Factorial de {i}: {factorial(i)}")
"""
"""2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique."""
"""
def fibonacci(f):
    if f == 0 or f == 1:
        return f
    else:
        return fibonacci(f-1)+fibonacci(f-2)

pos = int(input("Ingrese una posición: "))
for i in range(pos+1):
    print(f"Posición {i}: {fibonacci(i)}")
"""
"""3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑚^(𝑚−1). Prueba esta función en un algoritmo general.
"""
"""
def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(m, m-1)

print("Calcule la potencia de un número base elevado a su exponente utilizando la fórmula n^m = n * (m^(m-1))")
base = int(input("Número base: "))
exp = int(input("Elevado a: "))
resultado = potencia(base, exp)
print(f"El resultado es {resultado}.")
"""
"""4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto. """
"""
def binario(nro):
    if nro == 0:
        return '0'
    elif nro == 1:
        return '1'
    else:
        return binario(nro//2) + str(nro%2)
    
base10 = int(input("Ingrese un número: "))
print(f"El número en binario es: {binario(base10)} ")
"""
"""5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()."""
"""
def es_palindromo(palabra):
    if len(palabra) == 0:
        return True
    elif len(palabra) == 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

frase = input("Ingrese una frase para saber si es palíndromo: ")
if es_palindromo(frase) == True:
    print("Es un palíndromo!")
else:
    print("No lo es...")    
"""
"""6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)"""
"""
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + (suma_digitos(n // 10))

numero = int(input("Ingrese un número: "))
print(f"La suma de todos los dígitos es: {suma_digitos(numero)}")
"""
"""7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)"""

def contar_bloques(n):