# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):  # Itera desde 0 hasta 100 (inclusive), ya que range(101) genera números de 0 a 100
    print(i)          # Imprime el valor actual de la variable 'i' en cada iteración

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num = int(input("Ingrese un numero entero: ")) # Solicita al usuario un número entero y lo convierte a tipo entero
digitos = 1                                    # Inicializa la variable 'digitos' en 1 para contar al menos un dígito

while num >= 10:                                 # Mientras el número sea mayor que 1, ejecuta el bucle
    num //= 10                                 # Divide el número por 10 y descarta los decimales (división entera)
    digitos += 1                               # Incrementa la cantidad de dígitos en 1 por cada división

print(f"La cantidad de digitos que tiene el numero dado es {digitos}.")  # Imprime el número total de dígitos calculados

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

print("Ingrese 2 numeros enteros: ")    # Pide 2 valor y se almacenan en variables
valor_1 = int(input())
valor_2 = int(input())
acumulador = 0                          # Inicializa el acumulador

if valor_1 > valor_2:                   # Invierte los valores para que el 2do sea siempre el mayor
    valor_1, valor_2 = valor_2, valor_1

if (valor_2-valor_1) > 1:               # Busca que existan numeros entre los 2 valores
    while valor_1 != valor_2-1:
        valor_1 += 1                    # Agrega 1 al valor menor (Porque el valor dado no se cuenta)
        acumulador += valor_1           # Suma el valor resultante al acumulador
else:
    print("No hay numero entre los numeros dados")  # Si los numero dados son seguidos, no hay numeros para sumar

print(f"La suma de los numeros entre los valores dados es {acumulador}") # Imprime el resultado

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

acumulador = 0                                                     # Inicializa el acumulador
num = int(input("Ingrese un numero (0 para terminar): "))          # Pide numero al usuario
while num != 0:                                                    # Inicia bucle si el num no es 0
    acumulador += num                                              # Suma el numero del usuario a acumulador
    num = int(input("Ingrese otro numero (0 para terminar): "))    # Vuelve a pedir numero al usuario (Si es 0 sale del bucle)
print(f"La suma de los numeros ingresados es {acumulador}")        # Imprime el resultado de haber sumado los numeros dados

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random as R  # Importa la librería `random` y la abrevia como `R` para simplificar su uso.
numero_aleatorio = R.randint(0, 9)  # Genera un número aleatorio entero entre 0 y 9.
guess = int(input("Adivina el numero entre 0 y 9: "))  # Solicita al usuario que ingrese un número y lo convierte a entero.
contador = 1  # Inicializa un contador que lleva la cuenta de los intentos del usuario.

# Verifica si el número ingresado está dentro del rango válido (entre 0 y 9).
if 0 <= guess <= 9:
    # Si el número no es igual al generado, entra en el bucle.
    while guess != numero_aleatorio:
        guess = int(input("No es el numero correcto! Prueba con otro numero: "))  # Pide otro número al usuario.
        contador += 1  # Incrementa el contador con cada intento.
    print(f"Muy bien, has adivinado en tu {contador}º intento!")  # Muestra un mensaje de éxito con el número de intentos.
else:
    # Si el número ingresado está fuera del rango, muestra un mensaje de error.
    print("No has ingresado un numero de 0 a 9")

    
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(98,0,-2):    # Inicializa bucle con cuenta decreciente desde 98 (inclusive) a 0 (No inclusive)
    print(i)                # Imprime el contador en cada bucle hasta llegar a 0

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

# Solicita al usuario un número entero mayor a 0 y lo convierte a entero.
numero_usuario = int(input("Ingrese un numero entero mayor a 0: "))  
acumulador = 0  # Inicializa una variable acumuladora para guardar la suma.

# Verifica si el número ingresado por el usuario es mayor a 0.
if numero_usuario > 0:
    # Utiliza un bucle 'for' que recorre desde 1 hasta el número ingresado (inclusive).
    for i in range(1, numero_usuario + 1):  
        acumulador += i  # Suma cada número del rango al acumulador.
    
    # Muestra el resultado final de la suma utilizando f-strings para formatear el texto.
    print(f"La suma de los numeros comprendidos entre 0 y {numero_usuario} es igual a: {acumulador}")
else:
    # Si el número ingresado no es mayor a 0, muestra un mensaje de error.
    print("El numero ingresado no es correcto")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

n = 100  # Define la cantidad de números que se solicitarán al usuario.
positivos = 0  # Contador para números positivos.
negativos = 0  # Contador para números negativos.
pares = 0  # Contador para números pares.
impares = 0  # Contador para números impares.
numero_usuario = 0  # Inicializa la variable que almacenará el número ingresado por el usuario.

# Bucle que se ejecutará 'n' veces, de 0 a 99 (100 números en total).
for i in range(0, n):  
    # Solicita al usuario ingresar un número y lo convierte en un entero.
    numero_usuario = int(input(f"Ingrese el numero {i+1} de {n}: "))  
    
    # Verifica si el número es 0.
    if numero_usuario == 0:
        print("El 0 no se contara como positivo, negativo, par o impar")  # Mensaje específico para el caso del 0.
    
    # Si el número es positivo y par (divisible entre 2).
    elif numero_usuario > 0 and numero_usuario % 2 == 0:  
        positivos += 1  # Incrementa el contador de positivos.
        pares += 1  # Incrementa el contador de pares.
    
    # Si el número es positivo e impar (no divisible entre 2).
    elif numero_usuario > 0 and numero_usuario % 2 != 0:  
        positivos += 1  # Incrementa el contador de positivos.
        impares += 1  # Incrementa el contador de impares.
    
    # Si el número es negativo y par.
    elif numero_usuario < 0 and numero_usuario % 2 == 0:  
        negativos += 1  # Incrementa el contador de negativos.
        pares += 1  # Incrementa el contador de pares.
    
    # Si el número es negativo e impar.
    elif numero_usuario < 0 and numero_usuario % 2 != 0:  
        negativos += 1  # Incrementa el contador de negativos.
        impares += 1  # Incrementa el contador de impares.
    
    # Caso de error, aunque este bloque no debería activarse nunca con los chequeos previos.
    else:  
        print("ERROR")  # Mensaje de error para un caso inesperado.

# Al finalizar el bucle, muestra los resultados de los contadores.
print(f"Positivos: {positivos}")  # Imprime la cantidad total de números positivos.
print(f"Negativos: {negativos}")  # Imprime la cantidad total de números negativos.
print(f"Pares: {pares}")  # Imprime la cantidad total de números pares.
print(f"Impares: {impares}")  # Imprime la cantidad total de números impares.


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

n = 10  # Define la cantidad de números que se solicitarán al usuario.
numero_usuario = 0  # Inicializa la variable que almacenará cada número ingresado por el usuario.
acumulador = 0  # Inicializa la variable acumuladora que sumará todos los números.

# Utiliza un bucle 'for' para iterar desde 0 hasta n-1 (10 iteraciones en total).
for i in range(0, n):  
    # Solicita al usuario ingresar un número entero y lo almacena en 'numero_usuario'.
    numero_usuario = int(input(f"Ingrese el numero {i+1} de {n}: "))  
    acumulador += numero_usuario  # Suma el número ingresado al acumulador.

# Calcula la media dividiendo el acumulador entre la cantidad de números (n).
print(f"La media de los numeros ingresados es: {acumulador/n}")  # Muestra la media al usuario.


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
# Solicita al usuario un número entero y lo convierte en tipo entero.
numero_usuario = int(input("Ingrese un numero: "))  

# Calcula la longitud del número ingresado convirtiéndolo primero en una cadena y luego usando len().
l = len(str(numero_usuario))  

# Inicializa la variable 'resultado' donde se acumulará el resultado final.
resultado = 0  

# Recorre desde la longitud del número hasta 1 (en reversa) usando un bucle 'for'.
for i in range(l, 0, -1):  
    # Toma el último dígito del número usando el módulo (%10), luego lo posiciona correctamente en base a su lugar decimal.
    resultado += (numero_usuario % 10) * (10 ** (i - 1))  
    
    # Elimina el último dígito del número dividiéndolo entre 10 y tomando solo la parte entera con '//' (división entera).
    numero_usuario = numero_usuario // 10  

# Imprime el valor final de 'resultado', que es el número invertido.
print(resultado)