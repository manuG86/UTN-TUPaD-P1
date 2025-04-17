# Definicion de funciones
def imprimir_hola_mundo():
    print("Hola Mundo")

def saludar_usuario(nombre):
    print(f"Hola {nombre}")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    pi = 3.14
    area = pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    pi = 3.14
    perimetro = 2 * pi * radio
    return perimetro

def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    division = a / b
    multiplicacion = a * b
    return suma, resta, division, multiplicacion

def calcular_imc(peso,altura):
    return peso/altura

def celsius_a_fahrenheit(celsius):
    f = (celsius*1.8)+32
    return f

def calcular_promedio(a, b, c):
    return (a+b+c)/3

# Programa principal
#1
imprimir_hola_mundo()
#2
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)
#3
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)
#4
radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {calcular_area_circulo(radio)}, y su perímetro es: {calcular_perimetro_circulo(radio)}")
#5
segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"Cantidad de horas: {segundos_a_horas(segundos)}")
#6
numero = int(input("Ingrese un número para la tabla de multiplicar: "))
tabla_multiplicar(numero)
#7
a = int(input("Ingrese un valor: "))
b = int(input("Ingrese otro valor: "))
print(f"""
        a + b = {operaciones_basicas(a,b)[0]}
        a - b = {operaciones_basicas(a,b)[1]}
        a / b = {operaciones_basicas(a,b)[2]}
        a * b = {operaciones_basicas(a,b)[3]}""")
#8
peso = int(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su indice de masa corporal es {calcular_imc(peso,altura)}")
#9
celsius = int(input("Ingrese la temperatura en celsius: "))
print(f"{celsius}ºC es igual a {celsius_a_fahrenheit(celsius)} Fahrenheit.")
#10
a = int(input("Ingrese valor 1 de 3 para calcular promedio: "))
b = int(input("Ingrese valor 2 de 3 para calcular promedio: "))
c = int(input("Ingrese valor 3 de 3 para calcular promedio: "))
print(f"El promedio de {a},{b},{c}, es igual a: {calcular_promedio(a,b,c)}")