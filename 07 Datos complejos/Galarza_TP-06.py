# 1) Dado el diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

# Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

frutas = list(precios_frutas.keys())

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
agenda = {}

for i in range(1,6):
    nombre = input(f"Ingrese el nombre del contacto {i} de 5: ")
    tel = input(f"Ingrese el telefono de {nombre}: ")
    agenda[nombre] = tel

print(agenda[input("Ingrese un nombre para ver su telefono: ")])

# 5) Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
# Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras_unicas = frase.split()
print(f"Palabras unicas de la frase = {set(palabras_unicas)}")

conteo = {}

for palabra in palabras_unicas:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print(f"\nRecuento: {conteo}")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
calificaciones = {}

for i in range(1,4):
    alumno = input(f"Ingrese el nombre del alumno {i} de 3: ")
    notas_temporales = []
    for n in range(1,4):
        nota = float(input(f"Ingrese la nota {n}: "))
        notas_temporales.append(nota)
        notas = tuple(notas_temporales)
    calificaciones[alumno] = notas

# El metodo items permite desempaquetar tanto el key como el value del diccionario, que por defecto solo desempaqueta key
for alumno, notas in calificaciones.items():
    promedio = sum(notas) / len(notas)
    print(f"Alumno: {alumno} \n Notas: {notas} \n Promedio: {promedio:.2f} \n ------------------------")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

aprobados_parcial_1 = {"Ana", "Luis", "Jorge", "Pedro", "Juan", "Marcela", "Claudia"}
aprobados_parcial_2 = {"Luis", "Ana", "Marcos", "Manu", "Carlos", "Florencia", "Guadalupe", "Lucio", "Claudia"}

ambos = aprobados_parcial_1 & aprobados_parcial_2
solo_uno = aprobados_parcial_1 ^ aprobados_parcial_2
al_menos_uno = aprobados_parcial_1 | aprobados_parcial_2
print(f"Aprobaron parciales 1 y 2: {ambos}")
print(f"Aprobaron solo un parcial: {solo_uno}")
print(f"Aprobaron al menos un parcial: {al_menos_uno}")

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe.

stock = {
    "Pan": 250,
    "Avena": 320,
    "Semilla de chia": 50,
    "Aceite de coco": 18,
    "Levadura nutricional": 7,
    "Aceite de oliva": 15,
    "Fideos": 42,
    "Arroz": 68,
    "Datiles": 5,
    "Yerba": 19,
    "Café": 22,
    "Tomate": 89,
    "Papa": 450,
    "Cebolla": 52,
    "Banana": 79,
    "Manzana": 82,
    "Salsa de soja": 37,
    "Tempeh": 23,
    "Jabón": 35,
    "Papel Higiénico": 13
}

def consulta_stock():
    prod = input("Escribe el producto a consultar: ")
    if prod in stock.keys():
        print(f"{prod}: {stock.get(prod)} unidades. \n")
        sn = input("Desea agregar unidades al stock? (s/n) ")
        if sn == "s":
            agregar = int(input("Indique cuantas unidades agregar: "))
            stock[prod] += agregar
            print(f"Valores actualizados: \n{prod}: {stock.get(prod)} unidades. \n")
    else:
        sn = input("El producto consultado no existe, desea agregarlo? (s/n) ")
        if sn == "s":
            stock[prod] = 0
            agregar = int(input("Indique cuantas unidades agregar: "))
            stock[prod] += agregar
            print(f"Valores actualizados: \n{prod}: {stock.get(prod)} unidades. \n")
        else:
            print("Producto no agregado, saliendo del programa")
consulta_stock()

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("Lunes", "10:00"): "Dentista",
    ("Martes", "11:00"): "Reunion",
    ("Jueves", "18:00"): "Tennis",
    ("Viernes", "21:00"): "Concierto"
}

def consultar_evento():
    dia = input("Ingrese el día (por ejemplo: Lunes): ").capitalize()
    hora = input("Ingrese la hora (por ejemplo: 09:00): ")
    clave = (dia, hora)
    
    if clave in agenda:
        print(f"Actividad: {agenda[clave]}")
    else:
        print("No hay ninguna actividad programada en ese día y horario.")

consultar_evento()

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.

original = {"Argentina": "Buenos Aires", "España": "Madrid", "Francia": "Paris", "Nueva Zelanda": "Wellington", "Uruguay": "Montevideo"}
paises = list(original.keys())
capitales = list(original.values())

invertido = dict(zip(capitales, paises))

print(f'Diccionario original: {original}')
print(f'Diccionario invertido: {invertido}')