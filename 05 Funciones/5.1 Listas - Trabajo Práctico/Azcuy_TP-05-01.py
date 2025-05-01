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

lista_vacia = []
lista_vacia.append("Programar")
lista_vacia.append("Trabajar")
lista_vacia.append("Reparar")
print(lista_vacia)