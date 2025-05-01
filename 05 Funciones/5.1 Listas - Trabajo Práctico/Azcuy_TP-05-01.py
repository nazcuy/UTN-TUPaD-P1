# TRABAJO PRÁCTICO LISTAS
# NICOLAS AZCUY - DNI: 33.368.267

""" 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. 
Utilizar la función range."""
"""
print("Múltiplos de 4, del 1 al 100: ")
multip = list(range(4, 101, 4))
print(multip)
"""
"""2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) 
y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos 
o bien investigar cómo funciona el indexing con números negativos!"""
"""
elementos = ["pelota", "café", "destornillador", "computadora", "lapicera"]
penultimo = elementos[-2]
print(elementos)
print(f"Usando indexación negativa, el penúltimo es: {penultimo}")
penultimo =elementos[3]
print(f"Usando indexación positiva, el penúltimo es: {penultimo}")
"""
"""3) Crear una lista vacía, agregar tres palabras con append 
e imprimir la lista resultante por pantalla. 
Pista: para crear una lista vacía debes colocar los corchetes 
sin nada en su interior. Por ejemplo: lista_vacia []"""
"""
lista_vacia = []
lista_vacia.append("Programar")
lista_vacia.append("Trabajar")
lista_vacia.append("Reparar")
print(lista_vacia)
"""
"""4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos"""
"""
animales = ["Perro", "Gato", "Conejo", "Pez"]
animales[1] = "Loro"
animales[-1] = "Oso"
print(f"Lista modificada: {animales}")
"""
"""5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza."""
"""
## El programa tiene por objetivo remover el elemento máximo de una lista y mostrar por pantalla la lista modificada.

# Crea una lista de 5 elementos númericos, y la almacena en la variable "números":
numeros = [8, 15, 3, 22, 7]
# Utiliza la función "max()" para devolver el valor máximo de la lista. En este caso "22".
# Luego, la función "remove" busca y elimina el primer elemento que encuentre de ese valor "remove(22)"
numeros.remove(max(numeros))
# Imprime en pantalla la nueva lista modificada.
print(numeros)
"""
"""6) Crear una lista con números del 10 al 30 (incluído), 
haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros."""
"""
num = list(range(10, 31, 5))
print(f"La lista total es: {num}")
print("Los primeros 2 elementos son: ")
print(num[0])
print(num[1])
"""
"""7) Reemplazar los dos valores centrales (índices 1 y 2)
 de la lista “autos” por dos nuevos valores cualesquiera."""
"""
autos = ["sedan", "polo", "suran", "gol"]
autos [1:3] = ["Dodge 1500", "Agile"]
print(autos)
"""
"""8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla."""
"""
dobles =[]
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(f"Lista con valores dobles: {dobles}")
"""