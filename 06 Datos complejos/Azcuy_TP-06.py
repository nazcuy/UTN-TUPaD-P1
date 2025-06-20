# TP NRO 6 - AZCUY NICOLÁS DNI 33.368.267

""" 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""
precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva':1450
    }

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)


""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)


"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""
frutas = list(precios_frutas.keys())
print(frutas)


""" 4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""
contactos = {}
for i in range(2):
    nombre = input("Ingrese nombre del contacto: ")
    numero = input("Ingrese su número de teléfono: ")
    contactos[nombre] = numero

consulta = input("A quién querés llamar?: ")

if consulta in contactos:
    print("El número de", consulta, "es", contactos[consulta])
else:
    print("Ese número no está en la agenda")

    
""" 5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas: ", palabras_unicas)

conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
print("Conteo de palabras: ", conteo)


""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno."""
alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    nota1 = int(input("Ingresá la primera nota: "))
    nota2 = int(input("Ingresá la segunda nota: "))
    nota3 = int(input("Ingresá la tercera nota: "))

    notas = (nota1, nota2, nota3)
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print("El promedio de", nombre, "es:", format(promedio, ".2f"))

    
"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""
parcial1 = {"Ana", "Luis", "Sofía", "Carlos", "María"}
parcial2 = {"Carlos", "María", "Pedro", "Lucía", "Tomás"}
ambos = parcial1 & parcial2
print("Los que aprobaron ambos parciales son:", ambos)
solo_uno = parcial1 ^ parcial2
print("Aprobaron un sólo parcial:", solo_uno)
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)


""" 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""
stock_productos = {
    "manzanas": 10,
    "peras": 5,
    "naranjas": 8
}

producto = input("Ingresá el nombre del producto: ").lower()

if producto in stock_productos:
    print("Stock actual de", producto + ":", stock_productos[producto])
    agregar = input("¿Querés agregar unidades al stock? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print("Nuevo stock de", producto + ":", stock_productos[producto])

else:
    print("El producto no existe.")
    nuevo = input("¿Querés agregarlo como nuevo producto? (s/n): ").lower()
    if nuevo == "s":
        cantidad = int(input("¿Cuántas unidades tiene en stock?: "))
        stock_productos[producto] = cantidad
        print("Producto agregado. Stock de", producto + ":", stock_productos[producto])

print("\nStock total actualizado:")
for prod, cant in stock_productos.items():
    print(prod + ":", cant)


""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos."""
agenda = {}
while True:
    dia = input("Ingresá el día del evento (o escribí 'salir' para terminar): ").lower()
    if dia == "salir":
        break
    hora = input("Ingresá la hora del evento (por ejemplo, 14:00): ")
    if hora == "salir":
        break
    evento = input("Ingresá el nombre del evento: ")
    if evento == "salir":
        break

    agenda[(dia, hora)] = evento
    print("Evento agregado.\n")

print("\n--- CONSULTA DE EVENTOS ---")
dia_consulta = input("Ingresá el día que querés consultar: ").lower()
hora_consulta = input("Ingresá la hora que querés consultar: ")
clave = (dia_consulta, hora_consulta)
if clave in agenda:
    print(f"El evento el {dia_consulta} a las {hora_consulta} es: {agenda[clave]}")
else:
    print(f"No hay evento registrado para el {dia_consulta} a las {hora_consulta}.")


""" 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""
paises = {
    "Argentina": "Asado",
    "Italia": "Fideos",
    "Japón": "Sushi"
}
comidas = {}
for pais, comida in paises.items():
    comidas[comida] = pais
print("Diccionario invertido:")
print(comidas)

