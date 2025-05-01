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