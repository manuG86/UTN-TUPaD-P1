# Ejercicio 1: funcion recursiva que calcule el factorial de un numero. Luego, utiliza esa funcion para calcular y mostrar en pantalla el factorial de todos los numeros enteros entre 1 y el numero que indique el usuario.

def factorial(num):
    return 1 if num==0 or num==1 else num * factorial(num-1)

def mostrar_factoriales():
    x= int(input("Calcular los factoriales desde 1 hasta: "))
    for i in range(1,x+1):
        print(f'{i}! = {factorial(i)}')
        
mostrar_factoriales()

# Ejercicio 2: Crea una funcion recursiva que calcule el valor de la serie de Fibonacci en la posicion indicada. Posteriormente, muestra la serie completa hasta la posicion que el usuario especifique.

def fibo_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibo_recursivo(posicion-1)+fibo_recursivo(posicion-2)
    
def mostrar_fibonacci():
    num = int(input("Ingrese la posicion de la serie Fibonacci a mostrar: "))
    print(f'La posicion {num} de Fibonacci es el numero {fibo_recursivo(num)}')
    print(f'La serie completa hasta la posicion {num}: ')
    for i in range(num):
        print(fibo_recursivo(i), end='-')

mostrar_fibonacci()

# Ejercicio 3: Crea una funcion recursiva que calcule la potencia de un numero base elevado a un exponente, utilizando la formula nm= n * n (m-1). Prueba esta funcion en un algoritmo general.
print(' ')

def potencia(n,m):
    return 1 if m==0 else n * potencia(n,m-1)

print("Calculo de exponentes")
base= int(input("Ingresa la base: "))
exponente= int(input("Ingresa el exponente: "))
resultado = potencia(base,exponente)
print(f'{base} elevado a la {exponente} es: {resultado}')

# Ejercicio 4: Crea una funcion recursiva en Python que reciba un numero entero positivo en base decimal y devuelva su representacion en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    return decimal_a_binario(n // 2) + str(n % 2)

print(decimal_a_binario(64))

# Ejercicio 5: Implementa una funcion recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palindromo o False si no lo es.

def validar_palabra(palabra):
    tildes = "áéíóúÁÉÍÓÚ"
    return False if " " in palabra or any(letra in tildes for letra in palabra) else True

def es_palindromo(palabra):
    pal_min = palabra.lower()
    if validar_palabra(pal_min):
        if len(pal_min) <= 1:
            return True             # devuelve True si la palabra tiene 1 letra
        if pal_min[0] != pal_min[-1]:
            return False            
        return es_palindromo(pal_min[1:-1])
    else:
        print("Ingrese una palabra sin espacios ni tildes")

print(es_palindromo("lalalalal"))

# Ejercicio 6: Escribi una funcion recursiva en Python llamada suma_digitos(n) que reciba un numero entero positivo y devuelva la suma de todos sus digitos.

def suma_digitos(n):
    n = int(n)
    if n >= 0:
        return 0 if n==0 else (n%10) + suma_digitos(n//10)
    else:
        print("Ingrese un numero entero positivo")
        
print(suma_digitos(1234))

# Ejercicio 7: Un niño esta construyendo una piramide con bloques. En el nivel mas bajo coloca n bloques, en el siguiente nivel uno menos (n-1) y asi sucesivamente hasta llegar al ultimo nivel con un solo bloque.
# Escribi una funcion recursiva contar_bloques(n) que reciba el numero de bloques en el nivel mas bajo y devuelva el total de bloques que necesita para construir toda la piramide.

def contar_bloques(n):
    return 0 if n==0 else n + contar_bloques(n-1)

print(contar_bloques(4))

# Ejercicio 8: Escribi una funcion recursiva llamada contar_digito(numero,digito) que reciba un numero entero positivo (numero) y un digito (entre 0 y 9), y devuelva cuantas veces aparece ese digito dentro del numero.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

print(contar_digito(123432555331,5))