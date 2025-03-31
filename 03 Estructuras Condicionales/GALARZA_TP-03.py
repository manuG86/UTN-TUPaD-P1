#ACTIVIDAD 1:
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, debera mostrar un mensaje en pantalla que diga "Es mayor de edad"

#Creo la variable edad que toma el valor dado por el usuario en un input y transorma el valor a un numero entero
edad = int(input("Indique su edad: "))
#Usando un condicional ternario se imprime el mensaje "Es mayor de edad" cuando la edad es igual o mayor a 18, de otro modo imprimo "Es menor de edad"
print("Es mayor de edad") if edad>=18 else print("Es menor de edad")

#ACTIVIDAD 2:
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”

#pido la nota al usuario con un input, y la guardo como un numero entero en la variable nota
nota = int(input("Indique su nota: "))

#Con un condicional ternario imprimo el mensaje Aprobado cuando la edad es mayor o igual a 6, de otro modo con else imprimimos el mensaje desaprobado cuando la condicion anterior no se cumple
print("Aprobado") if edad>=6 else print("Desaprobado")

#ACTIVIDAD 3:
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

#Con input pido un numero al usuario, que transformo en el tipo int y almaceno en la variable num
num = int(input("Ingrese un numero: "))

#Si el modulo de ese numero dividido 2 arroja 0 por resultado, quiere decir que el numero es entero y la condicion sera verdadera
if num % 2 == 0:
#Al ser verdadera la condicion imprimimos lo siguiente
    print("Ha ingresado un numero par")
else:
#En cualquier otro caso el mensaje sera el siguiente    
    print("Por favor, ingrese un numero par")

#ACTIVIDAD 4
#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

#Se pide la edad con un input
edad = int(input("Ingrese su edad: "))

#Uso if para comprobar que la edad dada sera menor a 12
if edad <12:
    print("Eres Niño/a")

#Si el numero no es menor a 12, paso a comprobar la siguiente proposicion logica que pregunta si es mayor o igual a 12 y a su vez menor o igual a 18
elif edad >= 12 and edad <=18:
    print("Eres adolescente")

#De no haberse cumplido las 2 sentencias anteriores, pasamos a verificar si la edad esta entre 18 a 30, de nuevo usando elif.
elif edad >=18 and edad<30:
    print("Eres adulto/a joven")
#Si ninguna condicion anterior se cumple volvemos a usar elif para comprobar otra sentencia.
elif edad >= 30:
    print("Eres adulto/a mayor")

#Por ultimo si ninguna de las condiciones anteriores se cumplen ejecutamos el ultimo print
else:
    print("Ingrese una edad valida")
    
#ACTIVIDAD 5:
#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

#Definimos las variables contrasenia que va a ser solicitada al usuario, y la variable l que devuelve el numero o cantidad de caracteres de la cadena dada por el usuario
contrasenia = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
l = len(contrasenia)

#usamos una estructura if, donde la condicion a cumplirse es que l este entre 7 y 15, de cumplirse la contraseña es valida y lo comunicamos con un mensaje.
if l > 7 and l < 15:
    print("Ha ingresado una contraseña correcta")
    
#Si la condicion anterior no se cumple, es decir que la contraseña tiene mas o menos caracteres de lo solicitado, imprimimos un mensaje que pisa ingresar una contraseña correcta
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#ACTIVIDAD 6:
#importo las librerias necesarias
from statistics import mode, median, mean
import random

#defino la variable como una lista de 50 numeros asignados al asar por la funcion random.
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
#declaro 3 variables que definen la moda, la mediana y el promedio de el listado de numeros_aleatorios
n_mode = mode(numeros_aleatorios)
n_median = median(numeros_aleatorios)
n_mean = mean(numeros_aleatorios)

#Uso la estructura condicional para definir cual es la relacion entre esas 3 variables, donde primero se deben cumplir 2 condiciones, que el promedio sea mayor a la mediana y esta mayor a la moda.
if n_mean > n_median and n_median > n_mode:
    print("Hay sesgo positivo")
    
#Si lo anterior no se cumple, verificamos si el promedio es menos a la mediana y esta a su vez es menor a la moda.
elif n_mean < n_median and n_median < n_mode:
    print("Hay sesgo negativo")
#Si eso no se cumple chequeamos con elif, si la moda, mediana y promedio son iguales
elif n_mean == n_median == n_mode:
    print("No hay sesgo")
    
#Por ultimo si nada de esto es cierto, con la clausula else indicamos que se imprime el siguiente mensaje.
else:
    print("Resultado distinto")

#ACTIVIDAD 7:
#pido una frase o palabra al usuario y guardo en la variable frase
frase = input("Ingrese una frase o palabra: ")
#defino la variable vocal con las 5 vocales en un string
vocal = "aeiou"
#toma la ultima letra de frase y la transforma a minuscula
ultima_letra = frase[-1].lower()

#se busca si esa ultima letra pertenece al conjunto de vocales en el string vocal. Si se cumple esa condicion, se imprime la frase con el signo de admiracion concatenado
if ultima_letra in vocal:
    print(frase + "!")
    
#caso contrario se imprime la frase tal cual fue dada por el usuario
else:
    print(frase)

#ACTIVIDAD 8:
#defino la variable nombre y pido al usuario ingresar este dato
nombre = input("Ingrese su nombre: ")
#se le pide al usuario seleccionar entre 3 opciones, se guarda el numero en la variable opcion
opcion = int(input("""
               Ingrese 1: Para imprimir su nombre en mayuscula.
               Ingrese 2: Para imprimir su nombre en minuscula.
               Ingrese 3: Para imprimir su nombre con la primera letra mayuscula"""))

#Si el usuario selecciono la opcion 1, se cumple la condicion if, y se imprime la variable nombre transformada a mayusculas con el modulo upper
if opcion == 1:
    print(nombre.upper())
#si la opcion elegida fue 2, la condicion siguiente es verdadera y se imprime el nombre en minuscula, transformado por el modulo lower()
elif opcion == 2:
    print(nombre.lower())
#Ls siguiente condicion sera verdadera si se eligio la opcion 3, y se ejecutara la linea de print que imprime el nombre con la primera letra en mayuscula, logrado con el modulo title()
elif opcion == 3:
    print(nombre.title())
#Si se ingreso cualquier otra cosa que no sea 1, 2 o 3, se imprime el siguiente mensaje
else:
    print("Por favor ingrese una opcion valida")

#ACTIVIDAD 9:
#Se pide la escala con un input
e_r = float(input("Ingrese la magnitud del terremoto: "))

#Uso if para comprobar si la magnitud es menor a 3
if e_r < 3:
    print("Muy leve")
#Uso una serie de elif para agregar la siguiente validacion de no ser verdadera la anterior
elif e_r >= 3 and e_r <4:
    print("Leve")
elif e_r >= 4 and e_r <5:
    print("Moderado")
elif e_r >= 5 and e_r <6:
    print("Fuerte")
elif e_r >= 6 and e_r <7:
    print("Muy fuerte")
elif e_r >=7:
    print("Extremo")
#Por ultimo si ninguna condicion es verdadera doy un mensaje indicando que el numero no se encuentra dentro de la escala Richter
else:
    print("El numero ingresado no es valido dentro de la escala Richter")

#ACTIVIDAD 10:

#Pedimos al usuario que ingrese 3 variables, el hemisferio, el mes y el dia de la fecha.
hemisferio = input("Indique en que hemisferio se encuentra con N (para norte) o S (para sur)")
mes = int(input("Indique que mes es (formato mm): "))
dia = int(input("Indique que dia es (formato dd): "))

#se crea una funcion que verifica a partir de las variables mes y dia, si la fecha es valida. No se considera el año bisiesto, por lo que asigno 29 dias a febrero.
def fecha_valida(mes,dia):
    #el arreglo indica en cada posicion la cantidad de dias que tiene el mes de esa posicion, comenzando por 0 ya que el mes valido comienza desde la posicion 1
    dias_en_mes = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    #meses mayores a 12 o menores a 1, y dias menores a 1 dan una fecha invalida
    if mes < 1 or mes > 12 or dia < 1:
        return False
    #Sino se crea la variable dias_maximos igualandola a la cantidad de dias que corresponden a la posicion del mes dentro del arreglo dias_en_mes
    else:
        dias_maximos = dias_en_mes[mes]
        return dia <= dias_maximos

#Ahora creo una funcion que determina de acuerdo al mes y dia, cual de las 4 estaciones corresponde, a su vez dentro de cada estacion diferenciando con un condicional ternario si se trata de hemisferio sur o norte dentro de la linea de return.
def determinar_temporada(mes,dia):
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
        return "Verano" if hemisferio == "S" else "Invierno"
    
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
        return "Otoño" if hemisferio == "S" else "Primavera"
    
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
        return "Invierno" if hemisferio == "S" else "Verano"
    else:
        return "Primavera" if hemisferio == "S" else "Otoño"

#Uso de estructura condicional if, para filtrar primero si la fecha es valida a traves de la funcion anteriormente creada, tomando como parametros el mes y dia ingresado por el usuario.
if fecha_valida(mes,dia):
#si la fecha es valida ejecutamos el codigo que sigue, donde asignamos a la variable temporada, el resultado de correr la funcion determinar_temporada e imprimo un mensaje con el resultado
    temporada = determinar_temporada(mes,dia)
    print(f"La temporada es {temporada}")
else:
#Si la fecha no es valida se arroja este mensaje de error
    print("Por favor, ingrese una fecha valida")