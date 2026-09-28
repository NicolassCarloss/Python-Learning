# Mi guia de python que he ido creando mientras aprendo usando claude
#-------------------------BASICOS DE PYTHON---------------------------------------
# print(): muestra algo en pantalla
# input(): pide algo al usuario (siempre devuelve un string)
# Comentarios: se escriben con # para explicar el código o dejar notas.

#---------------------------OPERACIONES-------------------------------------------
# Aritméticos: +, -, *, /, // (división entera), % (módulo), ** (potencia)
# Asignación: =, +=, -=, etc.
# Comparación: ==, !=, >, <, >=, <=
# Lógicos: and, or, not

#---------------------TIPOS DE DATOS Y VARIABLES----------------------------------
# Variables: son contenedores de datos. No es necesario declarar su tipo.
# Tipos de datos: int, float, str, bool, list, tuple, dict, set
# bool: True o False
# str: cadenas de texto, se pueden usar comillas simples o dobles

#---------------------------IF, ELIF, ELSE----------------------------------------
#         ------estructuras de control para tomar decisiones------
# if edad >= 18:
#     print("Eres mayor de edad")
# elif edad > 0:
#     print("Eres menor de edad")
# else:
#     print("Edad no válida")

#----------------------------BUCLE WHILE------------------------------------------
#         ----se repite mientras una condición sea verdadera------
# contador = 1
# while contador <= 5:
#     print(contador)
#     contador += 1

#-----------------------------BUCLE FOR-------------------------------------------
#    -------se repite para cada elemento de una secuencia------------------
# for X in range(1, 6): 
#     print(X)
# NOTA: range(inicio, fin)

#-------------------------------BREAK---------------------------------------------
#                      ----rompe el bucle-----
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

#------------------------------CONTINUE-------------------------------------------
#              ------salta a la siguiente iteración------
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)  
# NOTA: Imprime solo los números impares

#-------------------------------LISTAS--------------------------------------------
#           -------son colecciones ordenadas y mutables-------
# frutas = ["manzana", "banana", "pera"]
# numeros = [1, 2, 3, 4, 5]
# mixta = [1, "hola", True, 3.5]

# print(frutas[0])   ---> manzana
# print(frutas[-1])  ---> pera (índice negativo = desde el final)

#-----------------------OPERACIONES CON LISTAS:-----------------------------------
# frutas.append("uva")        ---> agrega al final
# frutas.insert(1, "kiwi")    ---> inserta en posición específica
# frutas.remove("banana")     ---> elimina por valor
# frutas.pop()                ---> elimina y devuelve el último elemento
# print(len(frutas))          ---> cantidad de elementos
# print(frutas)               ---> ['manzana', 'kiwi', 'pera', 'uva']

#------------------------------SLICING--------------------------------------------
#         ------Slicing (rebanado), para obtener sub-listas------
# numeros = [10, 20, 30, 40, 50]
# print(numeros[1:3])   # [20, 30]      ---> desde índice 1 hasta 3 (sin incluir)
# print(numeros[:2])    # [10, 20]      ---> desde el inicio hasta índice 2
# print(numeros[2:])    # [30, 40, 50]  ---> desde índice 2 hasta el final

#-------------------------------TUPLAS--------------------------------------------
#    ---Las tuplas son similares a las listas pero son inmutables---
#            ---(no se pueden modificar después de crear)---
# tupla = (1, 2, 3)
# print(tupla[0])

#----------------------------DICCIONARIOS-----------------------------------------
#       ----Los diccionarios almacenan pares clave-valor----
#               ----Se definen con llaves {}----
# diccionario = {"nombre": "Nicolas", "edad": 20, "ciudad": "Bogotá"}
# print(diccionario["nombre"])              ---> Nicolás
# diccionario["edad"] = 21                  ---> Modificar valor
# diccionario["profesión"] = "Estudiante"   ---> Agregar nuevo par clave-valor

#-----------------------------CONJUNTOS-------------------------------------------
#       ----Los conjuntos son colecciones de elementos UNICOS----
#                  ----Se definen con llaves {}----
# conjunto_1 = {1, 2, 2, 3, 4, 4, 5}
# conjunto_2 = {4, 5, 6, 7, 8 , 9}
# print(conjunto_1)  ---> {1, 2, 3, 4, 5} (los duplicados se eliminan)

#-----------------------OPERACIONES CONJUNTOS:------------------------------------
# conjunto_1.add(6)                           ---> Agrega un elemento
# conjunto_1.remove(3)                        ---> Elimina un elemento
# print(conjunto_1.union(conjunto_2))         ---> Unión de conjuntos
# print(conjunto_1.intersection(conjunto_2))  ---> Intersección de conjuntos
# print(conjunto_1.difference(conjunto_2))    ---> Diferencia de conjuntos

#-----------------------------FUNCIONES-------------------------------------------
#       ----Las funciones son bloques de código reutilizables----
#            -----sin datos de entrada y salida-----
# def saludar():
#     print("Hola")
# saludar()  ---> Hola
#            -----con datos de entrada y salida-----
# def saludar(nombre):
#     print("Hola", nombre)
# saludar("Nicolas")  ---> Hola Nicolas

#------------------------------RETURN---------------------------------------------
# def sumar(a, b):
#     return a + b
# resultado = sumar(3, 5)
# print(resultado)      ---> 8
# print(sumar(10, 20))  ---> 30
# NOTA: return devuelve un valor, mientras que print() solo lo muestra en pantalla.

#-----------------------------SCOPES----------------------------------------------
#   ---Las variables definidas dentro de una función solo existen---
#                 ---dentro de esa misma función---
#             ---fuera de ella tienen un scope global---
# def ejemplo():
#     x = 10
#     print(x)
#
# ejemplo()
# print(x)  ---> Error! x no existe fuera de la función

#--------------------------STRING METHODS-----------------------------------------
#       ---Los strings tienen métodos que permiten manipularlos---
# texto = "Hola Mundo"
# print(texto.upper())          ---> HOLA MUNDO
# print(texto.lower())          ---> hola mundo
# print(texto.replace("Mundo", "Python"))       ---> Hola Python
# print(texto.split())          ---> ['Hola', 'Mundo'] (divide el string en palabras)
# print(texto.strip())          ---> Hola Mundo (elimina espacios al inicio y final)
# print(texto[0])               ---> H (accede al primer carácter)
# print(texto[-1])              ---> o (accede al último carácter)
# print(texto[0:4])             ---> Hola (subcadena desde índice 0 hasta 4)
# print(texto[::-1])            ---> odnuM aloH (invierte el string)
# print(len(texto))             ---> 10 (longitud del string)
# print("Mundo" in texto)       ---> True (verifica si "Mundo" está en el texto)
# print(texto.count("o"))       ---> 2 (cuenta cuántas veces aparece "o")

#-----------------------TiPOS DE EXCEPCIONES (ERRORES)----------------------------
#  --Excepciones son errores que ocurren durante la ejecución del programa--
# ValueError: ocurre cuando se intenta convertir un tipo de dato a otro incompatible   ------------> int("hola")
# ZeroDivisionError: ocurre cuando se intenta dividir por cero    ---------------------------------> 5 / 0
# IndexError: ocurre cuando se intenta acceder a un índice que no existe en una lista o string  ---> lista[10]
# KeyError: ocurre cuando se intenta acceder a una clave que no existe en un diccionario    -------> diccionario["clave_no_existente"]
# TypeError: ocurre cuando se intenta realizar una operación con tipos de datos incompatibles   ---> 5 + "hola"
# FileNotFoundError: ocurre cuando se intenta leer un archivo que no existe.    -------------------> with open("archivo_que_no_existe.txt", "r") as archivo:

#-----------------------------TRY / EXCEPT-----------------------------------------
#  --Se usa para manejar excepciones y evitar que el programa se detenga--
# try:
#     numero = int(input("Ingresa un número: "))|
#     print("El número ingresado es:", numero)
# except ValueError:
#     print("Error: Debes ingresar un número válido.")

#----------------------------ELSE / FINALLY----------------------------------------
#       ---else se ejecuta solo si no ocurrió ningún error en el try---
#                    --finally se ejecuta siempre--
# try:
#     numero = int(input("Ingresa un número: "))
# except ValueError:
#     print("No es un número.")
# else:
#     print("Todo salió bien, ingresaste:", numero)
# finally:
#     print("Este mensaje aparece siempre.")

#-------------------------------ARCHIVOS-------------------------------------------
#                       -----ABRIR UN ARCHIVO-----
# archivo = open("datos.txt", "r")
#
# "r" ---> lectura (read). El archivo debe existir.
# "w" ---> escritura (write). Crea el archivo si no existe. Si ya existe, lo sobreescribe completo.
# "a" ---> agregar (append). Crea el archivo si no existe. Si ya existe, agrega al final sin borrar lo anterior.
# "r+" ---> lectura y escritura simultánea.
#
#                           ------WITH------
#          ---Siempre que trabajes con archivos usa el bloque with---
#  ---Cierra el archivo automáticamente al terminar el bloque, aunque ocurra un error---
# with open("datos.txt", "w") as archivo:
#
#                    -----ESCRIBIR EN UN ARCHIVO-----
# with open("datos.txt", "w") as archivo:
#     archivo.write("Primera línea\n")
#     archivo.write("Segunda línea\n")
# NOTA: \n es el salto de línea. Sin él, todo quedaría en una sola línea
#
#                     -----LEER EN UN ARCHIVO-----
#           ---Leer todo el contenido como un solo string---
# with open("datos.txt", "r") as archivo:
#     contenido = archivo.read()
#     print(contenido)
#
#          ---Leer línea por línea (útil para archivos grandes)---
# with open("datos.txt", "r") as archivo:
#     for linea in archivo:
#         print(linea.strip())
# NOTA: .strip() elimina el \n al final de cada línea

#-------------------------------CLASES-------------------------------------------
#       ---Son plantillas para crear objetos con atributos y métodos---
# class Personaje:
#     def __init__(self, nombre, defensa, inteligencia, vida):
#     self.nombre = nombre
#     self.defensa = defensa
#     self.inteligencia = inteligencia
#     self.vida = vida
# mi_personaje = Personaje("Nicolas", 50, 85, 100)
# print("El nombre del jugador es: ", mi_personaje.nombre)   ---> Nicolas
# print("La vida del jugador es: ", mi_personaje.vida)       ---> 100

#-------------------------------HERENCIA-----------------------------------------
#  -crea una clase base y una clase derivada que hereda sus atributos y métodos-
# class Personaje:
#     def __init__(self, nombre, defensa, inteligencia, vida):
#        self.nombre = nombre
#        self.defensa = defensa
#        self.inteligencia = inteligencia
#        self.vida = vida
# class Guerrero(Personaje):
#   def __init__(self, nombre, defensa, inteligencia, vida, fuerza):
#     super().__init__(nombre, defensa, inteligencia, vida)
#    self.fuerza = fuerza
#   def atacar(self):
#    print(f"{self.nombre} ataca con fuerza {self.fuerza}")
# guerrero = Guerrero("Nicolas", 50, 85, 100, 90)
# guerrero.atacar()  ---> Nicolas ataca con fuerza 90

#---------------------------------MODULOS-----------------------------------------
#       --Un módulo es un archivo que contiene código Python--
#                --(funciones, clases, variables)--
#     --Y se puede usar en otros archivos por medio de importaciones--
# archivo 'ejemplo_modulo.py':
#    def saludar():
#        print("Hola desde el módulo")
#
# archivo 'principal.py':
#    import ejemplo_modulo
#    ejemplo_modulo.saludar()  ---> Hola desde el módulo

#----------------------------MODULOS DE PYTHON------------------------------------
#             --Python tiene muchos módulos integrados que--
#                   --puedes usar para tareas comunes--
# import math
#    print(math.sqrt(16))   ---> 4.0 (raíz cuadrada)
#    print(math.pi)         ---> 3.141592653589793 (valor de pi)
# import random
#    print(random.randint(1, 10))  ---> número entero aleatorio entre 1 y 10
#    print(random.choice(["rojo", "verde", "azul"]))  ---> elige un color al azar
# import datetime
#    print(datetime.datetime.now())   ---> fecha y hora actual
#    print(datetime.date.today())     ---> fecha actual

#-----------------------FORMAS DE IMPORTAR MODULOS--------------------------------
#       ---Importar el módulo completo (accedes con math.sqrt)---
# import math
# print(math.sqrt(25))
#
#     ---Importar solo lo que necesitas (accedes directamente como sqrt)---
# from math import sqrt, pi
# print(sqrt(25))
#
#          ---Importar con alias (útil cuando el nombre es largo)---
# import datetime as dt
# hoy = dt.date.today()
#
#     ---Importar todo (no recomendado: puede generar conflictos de nombres)---
# from math import *

#-------------------------------Lambda--------------------------------------------
#       ---Las funciones lambda son funciones anónimas de una sola línea---
#       ---Se usan para operaciones simples y rápidas---
# suma = lambda a, b: a + b
# print(suma(5, 3))  ---> 8

#--------------------------------MAP----------------------------------------------
#       ---map() aplica una función a cada elemento de un iterable---
# numeros = [1, 2, 3, 4, 5]
# cuadrados = list(map(lambda x: x ** 2, numeros))
# print(cuadrados)  ---> [1, 4, 9, 16, 25]

#--------------------------------FILTER-------------------------------------------
#       ---filter() filtra elementos de un iterable según una condición---
# numeros = [1, 2, 3, 4, 5]
# pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(pares)  ---> [2, 4]



#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#░░░░░████░░░░░░░░░░░░░░░████░░░░░
#░░░░███░░░░░░░░░░░░░░░░░░░███░░░░
#░░░███░░░░░░░░░░░░░░░░░░░░░███░░░
#░░███░░░░░░░░░░░░░░░░░░░░░░░███░░
#░███░░░░░░░░░░░░░░░░░░░░░░░░░███░
#████░░░░░░░░░░░░░░░░░░░░░░░░░████
#████░░░░░░░░░░░░░░░░░░░░░░░░░████
#██████░░░░░░░███████░░░░░░░██████
#█████████████████████████████████
#█████████████████████████████████
#░███████████████████████████████░
#░░████░███████████████████░████░░
#░░░░░░░███▀███████████▀███░░░░░░░
#░░░░░░████──▀███████▀──████░░░░░░
#░░░░░░█████───█████───█████░░░░░░
#░░░░░░███████▄█████▄███████░░░░░░
#░░░░░░░███████████████████░░░░░░░
#░░░░░░░░█████████████████░░░░░░░░
#░░░░░░░░░███████████████░░░░░░░░░
#░░░░░░░░░░█████████████░░░░░░░░░░
#░░░░░░░░░░░███████████░░░░░░░░░░░
#░░░░░░░░░░███──▀▀▀──███░░░░░░░░░░
#░░░░░░░░░░███─█████─███░░░░░░░░░░
#░░░░░░░░░░░███─███─███░░░░░░░░░░░
#░░░░░░░░░░░░█████████░░░░░░░░░░░░
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
