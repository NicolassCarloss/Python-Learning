# Ejercicios tomados por Claude
# ---------------------------------------------- Clase 1 - Variables, tipos de datos, operadores ----------------------------------------------
print("---------------------- Clase 1 ----------------------")

# Crea una variable con tu nombre, otra con tu edad y otra con tu altura. Imprime las tres usando print()
nombre = "Nicolas"
edad = 20
altura = 1.77
print("Mi nombre es", nombre)
print("Tengo", edad, "años")
print("Mi altura es", altura)

# Pide al usuario su nombre con input() y muestra el mensaje: "Bienvenido, [nombre]"
nombre_usuario = input("¿Cuál es tu nombre? ")
print("Bienvenido,", nombre_usuario)

# Crea dos variables numéricas (a y b) con los valores 17 y 5. Calcula e imprime: suma, resta, multiplicación, división normal, división entera, módulo y potencia
a = 17
b = 5
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

# Usa type() para imprimir el tipo de dato de cada una de las variables que creaste en el ejercicio 1
print(type(nombre))
print(type(edad))
print(type(altura))

# ---------------------------------------------- Clase 2 - Operadores de comparación y lógicos ----------------------------------------------
print("---------------------- Clase 2 ----------------------")

# Crea dos variables numéricas, x = 8 y y = 15. Imprime el resultado de las seis comparaciones (>, <, ==, !=, >=, <=) entre ellas
x = 8
y = 15
print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)

# Crea una variable edad_permiso = 17 y otra tiene_permiso = True. Usa and para verificar si puede entrar a un evento que requiere ser mayor de 18 y tener permiso
edad_permiso = 17
tiene_permiso = True
print("¿La persona es mayor de 18 y tiene permiso?:", edad_permiso >= 18 and tiene_permiso)

# Con las mismas variables, usa or para verificar si puede entrar si el requisito es ser mayor de 18 años o tener permiso
print("¿La persona es mayor de 18 o tiene permiso?:", edad_permiso >= 18 or tiene_permiso)

# Crea una variable esta_lloviendo = False y usa not para imprimir si se puede salir sin paraguas
esta_lloviendo = False
print("¿Se puede salir sin paraguas?:", not esta_lloviendo)

# ---------------------------------------------- Clase 3 - Condicionales ----------------------------------------------
print("---------------------- Clase 3 ----------------------")

# Crea una variable temperatura con el valor 28. Si es mayor a 30, imprime "Hace calor". Si no, "Temperatura agradable"
temperatura = 28
if temperatura > 30:
    print("Hace calor")
else:
    print("Temperatura agradable")

# Usando if-elif-else, imprime "Excelente" si nota >= 90, "Aprobado" si >= 60, "Reprobado" en otro caso
nota = 55
if nota >= 90:
    print("Excelente")
elif nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")

# Usando condicionales anidados, determina si la persona puede conducir (>= 18 y con licencia)
edad_conducir = 16
tiene_licencia = True
if edad_conducir >= 18:
    if tiene_licencia:
        print("Puede conducir un carro")
    else:
        print("Mayor de edad pero sin licencia")
else:
    print("Menor de edad, no puede conducir")

# Determina si un número es positivo, negativo o cero
numero_signo = -8
if numero_signo > 0:
    print("El numero es positivo")
elif numero_signo < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")

# ---------------------------------------------- Clase 4 - Bucles ----------------------------------------------
print("---------------------- Clase 4 ----------------------")

# Usando while, imprime los números del 1 al 10
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# Usando while, pide al usuario una entrada hasta que escriba "salir"
while True:
    entrada = input("Escriba algo (o 'salir' para terminar): ").lower()
    if entrada == "salir":
        print("Hasta luego")
        break
    else:
        print("Sigue intentando")

# Usando for con range(), imprime los números pares del 0 al 20
for i in range(0, 21, 2):
    print(i)

# Usando for, encuentra e imprime el primer número del 1 al 50 divisible entre 7
for i in range(1, 51):
    if i % 7 == 0:
        print(i)
        break

# Usando for y continue, imprime solo los números del 1 al 20 que NO sean divisibles entre 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

# Usando bucles anidados, imprime las tablas de multiplicar del 1 al 5
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

# ---------------------------------------------- Clase 5 - Estructuras de datos ----------------------------------------------
print("---------------------- Clase 5 ----------------------")

# Crea una lista con 5 nombres de ciudades. Imprime la primera, la última y las tres del medio
ciudades = ["Bogotá", "Medellin", "Cali", "Barranquilla", "Cartagena"]
print(ciudades[0])
print(ciudades[-1])
print(ciudades[1:4])

# Agrega una ciudad con append(), elimina una con remove(), imprime la lista final y su longitud
ciudades.append("Santa Marta")
ciudades.remove("Cali")
print(ciudades)
print(len(ciudades))

# Crea un diccionario que represente un libro, modifica y agrega claves, recórrelo con for
libro = {
    "titulo": "Cien Años de Soledad",
    "autor": "Gabriel Garcia Márquez",
    "año": 1967,
    "paginas": 417
}
print(libro["titulo"])
print(libro["autor"])
print(libro["año"])
print(libro["paginas"])
libro["paginas"] = 420
libro["genero"] = "Realismo Mágico"
for clave, valor in libro.items():
    print(clave, ":", valor)

# Convierte una lista con duplicados en conjunto para eliminarlos
numeros_duplicados = [1, 2, 2, 3, 4, 4, 5]
conjunto_sin_duplicados = set(numeros_duplicados)
print(conjunto_sin_duplicados)

# Crea dos conjuntos con elementos en común e imprime unión, intersección y diferencia
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
print("Unión:", conjunto1.union(conjunto2))
print("Intersección:", conjunto1.intersection(conjunto2))
print("Diferencia (conjunto1 - conjunto2):", conjunto1.difference(conjunto2))

# ---------------------------------------------- Clase 6 - Funciones ----------------------------------------------
print("---------------------- Clase 6 ----------------------")

# Función que devuelve True si un número es par, False si es impar
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(4))
print(es_par(7))
print(es_par(10))

# Función que calcula el precio final con descuento (por defecto 10%)
def calcular_precio_final(precio, descuento=10):
    return precio * (1 - descuento / 100)

print(calcular_precio_final(100))
print(calcular_precio_final(100, 20))

# Función que devuelve el mayor de tres números sin usar max()
def mayor_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(mayor_de_tres(3, 7, 5))
print(mayor_de_tres(10, 2, 8))

# Función que cuenta vocales en un string (incluyendo tildes y mayúsculas)
def contar_vocales(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador

print(contar_vocales("Hola Mundo"))
print(contar_vocales("Python es genial"))

# Función que determina si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

print(es_primo(1))
print(es_primo(7))
print(es_primo(10))

# ---------------------------------------------- Clase 7 - Strings y formateo ----------------------------------------------
print("---------------------- Clase 7 ----------------------")

# Pide una frase al usuario e imprime: mayúsculas, minúsculas, invertida y longitud
frase_usuario = input("Ingresa una frase: ")
print("Frase en mayusculas:", frase_usuario.upper())
print("Frase en minusculas:", frase_usuario.lower())
print("Frase invertida:", frase_usuario[::-1])
print("Cantidad de caracteres:", len(frase_usuario))

# Separa nombre completo con split() e imprime con f-string
nombre_completo = input("Ingresa tu nombre completo (nombre y apellido): ")
nombre_split, apellido_split = nombre_completo.split()
print(f"Tu nombre es {nombre_split} y tu apellido es {apellido_split}")

# Función que formatea un número como precio con 2 decimales
def formatear_precio(numero):
    return f"${numero:.2f}"

print(formatear_precio(1234.56789))
print(formatear_precio(9.9))

# Cuenta cuántas veces aparece la letra 'a' en una palabra
palabra_input = input("Ingresa una palabra: ")
print(f"La letra 'a' aparece {palabra_input.lower().count('a')} veces en '{palabra_input}'")

# Une una lista de palabras con .join()
palabras_lista = ["No", "se", "que", "escribir", "OK"]
frase_unida = " ".join(palabras_lista)
print("Frase unida:", frase_unida)

# ---------------------------------------------- Clase 8 - Manejo de errores ----------------------------------------------
print("---------------------- Clase 8 ----------------------")

# División con manejo de ValueError y ZeroDivisionError
try:
    num1 = int(input("Ingrese el primer numero a dividir: "))
    num2 = int(input("Ingrese el segundo numero (divisor): "))
    print("Resultado:", num1 / num2)
except ValueError:
    print("Error: ingrese valores numericos enteros.")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")

# Lista con manejo de IndexError y ValueError
personas = ["Nicolas", "Esteban", "David"]
try:
    indice = int(input("Ingrese un índice (0, 1 o 2): "))
    print(personas[indice])
except IndexError:
    print("Error: índice fuera de rango.")
except ValueError:
    print("Error: ingrese un número entero.")

# Diccionario con manejo de KeyError
persona_dict = {"Nombre": "Nicolas", "Edad": 20, "Profesión": "Ingeniero", "Ciudad": "Bogotá"}
try:
    clave = input("Ingrese una clave ('Nombre', 'Edad', 'Profesión' o 'Ciudad'): ")
    print(persona_dict[clave])
except KeyError:
    print("Error: clave no encontrada.")

# Bucle de reintento hasta ingresar un número válido entre 1 y 10
while True:
    try:
        numero_rango = int(input("Ingresa un numero entero del 1 al 10: "))
        if 1 <= numero_rango <= 10:
            print(f"Numero valido: {numero_rango}")
            break
        else:
            print("El numero debe estar entre 1 y 10.")
    except ValueError:
        print("Eso no es un numero entero.")

# Función dividir con manejo de ZeroDivisionError usando return
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división por cero"

print(dividir(10, 2))
print(dividir(10, 0))

# ---------------------------------------------- Clase 9 - Archivos ----------------------------------------------
print("---------------------- Clase 9 ----------------------")

# Escribir tres líneas en notas.txt y leerlo completo
with open("notas.txt", "w") as archivo:
    archivo.write("Primera linea.\n")
    archivo.write("Segunda linea.\n")
    archivo.write("Tercera linea")

with open("notas.txt", "r") as archivo:
    print(archivo.read())

# Agregar dos líneas con modo "a" y leer el archivo completo para confirmar
with open("notas.txt", "a") as archivo:
    archivo.write("Cuarta linea.\n")
    archivo.write("Quinta linea.\n")

with open("notas.txt", "r") as archivo:
    print(archivo.read())

# Pedir 4 nombres al usuario, guardarlos en nombres.txt y leerlos línea por línea
with open("nombres.txt", "w") as archivo:
    for i in range(1, 5):
        nombre_archivo = input(f"Ingrese el nombre {i}: ")
        archivo.write(nombre_archivo + "\n")

with open("nombres.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())

# Leer configuracion.txt o crearlo con valores por defecto si no existe
try:
    with open("configuracion.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    with open("configuracion.txt", "w") as archivo:
        archivo.write("configuracion_por_defecto=True")
    with open("configuracion.txt", "r") as archivo:
        print(archivo.read())

# Leer nombres.txt, ordenar alfabéticamente y guardar en nombres_ordenados.txt
with open("nombres.txt", "r") as archivo:
    lineas_nombres = archivo.readlines()

lineas_nombres.sort()
print("Lista ordenada:", lineas_nombres)

with open("nombres_ordenados.txt", "w") as archivo:
    archivo.writelines(lineas_nombres)

# ---------------------------------------------- Clase 10 - Programación Orientada a Objetos ----------------------------------------------
print("---------------------- Clase 10 ----------------------")

# Clase Rectangulo con métodos area() y perimetro()
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return (self.ancho * 2) + (self.alto * 2)

nevera = Rectangulo(10, 20)
print("Área de la nevera:", nevera.area())
print("Perímetro de la nevera:", nevera.perimetro())

ventana = Rectangulo(5, 3)
print("Area de la ventana:", ventana.area())
print("Perimetro de la ventana:", ventana.perimetro())

# Clase CuentaBancaria con depositar(), retirar() y ver_saldo()
class CuentaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente.")

    def ver_saldo(self):
        print(self.saldo)

nicolas_cuenta = CuentaBancaria()
nicolas_cuenta.ver_saldo()
nicolas_cuenta.depositar(1000)
nicolas_cuenta.retirar(700)
nicolas_cuenta.ver_saldo()
nicolas_cuenta.retirar(500)

# Clase Estudiantes con agregar_nota() y promedio()
class Estudiantes:
    def __init__(self, nombre, notas=None):
        self.nombre = nombre
        self.notas = [] if notas is None else notas

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return 0

    def ver_notas(self):
        if self.notas:
            print(self.notas)
        else:
            print("Sin notas registradas.")

esteban = Estudiantes("Esteban")
esteban.ver_notas()
esteban.agregar_nota(50)
esteban.agregar_nota(10)
esteban.agregar_nota(90)
esteban.agregar_nota(45)
esteban.ver_notas()
print("Promedio de Esteban:", esteban.promedio())

# Clases con herencia: Vehiculos (base), Carro y Moto (hijas) con polimorfismo en descripcion()
class Vehiculos:
    def __init__(self, marca, velocidad_maxima):
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima

    def descripcion(self):
        return f"Vehículo {self.marca}, velocidad máxima: {self.velocidad_maxima}"

class Carro(Vehiculos):
    def __init__(self, marca, velocidad_maxima, numero_puertas, modelo, tipo_carro):
        super().__init__(marca, velocidad_maxima)
        self.numero_puertas = numero_puertas
        self.modelo = modelo
        self.tipo_carro = tipo_carro

    def descripcion(self):
        return (f"Auto {self.marca} modelo {self.modelo}, {self.velocidad_maxima}, "
                f"{self.numero_puertas} puertas, tipo {self.tipo_carro}")

class Moto(Vehiculos):
    def __init__(self, marca, velocidad_maxima, modelo, tipo_moto, cilindraje):
        super().__init__(marca, velocidad_maxima)
        self.modelo = modelo
        self.tipo_moto = tipo_moto
        self.cilindraje = cilindraje

    def descripcion(self):
        return (f"Moto {self.marca} modelo {self.modelo}, {self.velocidad_maxima}, "
                f"{self.cilindraje} de cilindraje, tipo {self.tipo_moto}")

Camaro = Carro("Chevrolet", "200 km/h", 2, 2010, "Deportivo")
F150 = Carro("Ford", "180 km/h", 4, 2020, "4x4 todo terreno")
NKD = Moto("AKT", "130 km/h", 2023, "urbano", "150cc")
kawasaki = Moto("Kawasaki", "250 km/h", 2024, "Deportivo", "948cc")
jet_privado = Vehiculos("Gulfstream G800", "1100 km/h")

for vehiculo in [Camaro, F150, NKD, kawasaki, jet_privado]:
    print(vehiculo.descripcion())

# ---------------------------------------------- Clase 11 - Módulos y paquetes ----------------------------------------------
print("---------------------- Clase 11 ----------------------")

import math
import random
import datetime

# Función hipotenusa usando math.sqrt
def hipotenusa(cateto_1, cateto_2):
    return math.sqrt((cateto_1 ** 2) + (cateto_2 ** 2))

print(hipotenusa(7, 9))
print(hipotenusa(3, 6))

# Simula 10 lanzamientos de un dado de 6 caras con random e imprime el promedio
lista_lanzamientos = []
for _ in range(10):
    lista_lanzamientos.append(random.randint(1, 6))
print(lista_lanzamientos)
print("Promedio lanzamientos:", sum(lista_lanzamientos) / len(lista_lanzamientos))

# Funciones de calculadora (en un proyecto real estarían en calculadora.py)
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir_calc(a, b):
    if b == 0:
        return "No se puede dividir por 0"
    return a / b

print(sumar(10, 45))
print(restar(29, 8))
print(multiplicar(9, 5))
print(dividir_calc(10, 0))
print(dividir_calc(10, 2))

# Calcula cuántos días faltan hasta el 31 de diciembre del año en curso
def dias_hasta_fin_de_año():
    hoy = datetime.date.today()
    fin_año = datetime.date(hoy.year, 12, 31)
    return (fin_año - hoy).days

print(f"Faltan {dias_hasta_fin_de_año()} días para año nuevo.")

# ---------------------------------------------- Clase 12 - List comprehension y funciones avanzadas ----------------------------------------------
print("---------------------- Clase 12 ----------------------")

# Cubos del 1 al 10 con list comprehension
cubos = [numero ** 3 for numero in range(1, 11)]
print(cubos)

# Filtrar palabras con más de 4 letras usando list comprehension
palabras_filtro = ["sol", "luna", "estrella", "mar", "galaxia", "rio"]
resultado_palabras = [palabra for palabra in palabras_filtro if len(palabra) > 4]
print(resultado_palabras)

# Convertir temperaturas de Celsius a Fahrenheit con map y lambda
temperaturas_celsius = [0, 20, 37, 100, -10, 25]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperaturas_celsius))
print(fahrenheit)

# Filtrar números divisibles entre 3 con filter y lambda
numeros_filtro = [15, 8, 23, 4, 42, 16, 7, 99, 3, 30]
divisibles_3 = list(filter(lambda n: n % 3 == 0, numeros_filtro))
print(divisibles_3)

# Combinar map y filter: de la lista, filtrar positivos y elevarlos al cuadrado
numeros_mix = [-5, -3, -1, 0, 2, 4, 6, 8]
resultado_map_filter = list(map(lambda n: n ** 2, filter(lambda n: n > 0, numeros_mix)))
print(resultado_map_filter)

# Equivalente con list comprehension
resultado_comprehension = [n ** 2 for n in numeros_mix if n > 0]
print(resultado_comprehension)



#───────▄▀▀▀▀▀▀▀▀▀▀▄▄
#────▄▀▀░░░░░░░░░░░░░▀▄
#──▄▀░░░░░░░░░░░░░░░░░░▀▄
#──█░░░░░░░░░░░░░░░░░░░░░▀▄
#─▐▌░░░░░░░░▄▄▄▄▄▄▄░░░░░░░▐▌
#─█░░░░░░░░░░░▄▄▄▄░░▀▀▀▀▀░░█
#▐▌░░░░░░░▀▀▀▀░░░░░▀▀▀▀▀░░░▐▌
#█░░░░░░░░░▄▄▀▀▀▀▀░░░░▀▀▀▀▄░█
#█░░░░░░░░░░░░░░░░▀░░░▐░░░░░▐▌
#▐▌░░░░░░░░░▐▀▀██▄░░░░░░▄▄▄░▐▌
#─█░░░░░░░░░░░▀▀▀░░░░░░▀▀██░░█
#─▐▌░░░░▄░░░░░░░░░░░░░▌░░░░░░█
#──▐▌░░▐░░░░░░░░░░░░░░▀▄░░░░░█
#───█░░░▌░░░░░░░░▐▀░░░░▄▀░░░▐▌
#───▐▌░░▀▄░░░░░░░░▀░▀░▀▀░░░▄▀
#───▐▌░░▐▀▄░░░░░░░░░░░░░░░░█
#───▐▌░░░▌░▀▄░░░░▀▀▀▀▀▀░░░█
#───█░░░▀░░░░▀▄░░░░░░░░░░▄▀
#──▐▌░░░░░░░░░░▀▄░░░░░░▄▀
#─▄▀░░░▄▀░░░░░░░░▀▀▀▀█▀
#▀░░░▄▀░░░░░░░░░░▀░░░▀▀▀▀▄▄▄▄▄




#_________________¶¶111111¶11111111111111¶¶111¶____
#_________________¶¶11111¶111111111111111¶¶111¶____
#________________¶¶111111¶11111111¶¶11¶¶¶¶1111¶____
#_______________¶¶1111111111111111¶¶¶¶¶¶¶11111¶____
#_____________1¶¶11111111111111111¶¶___¶¶11111¶____
#___________¶¶¶¶11111¶1111111¶¶1111¶¶¶11¶11111¶____
#_________¶¶¶111111111111111111111111¶¶¶¶11111¶____
#_______1¶¶11111111111111111111111111111¶¶¶111¶____
#______¶¶111111111111111111111111111111111¶¶¶1¶____
#_____¶¶1111111111111111¶11¶¶111111111111111¶¶¶____
#____¶¶11111111111111111¶¶¶¶11111111111111111¶¶____
#___¶¶1111111111111111111¶¶1111111111111111111¶¶___
#__¶¶11111111111111111111¶¶11111111111111111111¶¶__
#__¶111111111111111111111¶1111111111111111111111¶__
#_¶¶11111111111111111111¶¶1111111111111111111111¶¶_
#_¶111111111111111111111¶¶1111111111111111111111¶¶_
#_¶111111111111111111111¶¶1111111111111111111111¶¶_
#1¶111111111111111111111¶¶1111111111111111111111¶¶_
#1¶111111111111111111111¶¶1111111111111111111111¶¶_
#1¶111111111111111111111¶¶1111111111111111111111¶1_
#_¶1111111111111111111111¶¶11111111111111111111¶¶__
#_¶1111111111111111111111¶¶11111111111111111111¶1__
#_¶111111111111111111111¶¶¶¶111111111111111111¶¶___
#_¶¶1111111111111111111¶¶1¶¶¶¶111111111111111¶¶____
#_1¶1111111111111111¶¶¶¶¶¶¶¶¶¶¶¶111111111111¶¶1____
#__¶11111111111¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶11111¶¶¶1____
#__¶¶1111111111¶¶¶¶11111¶¶_¶¶1111¶¶¶¶1111¶¶¶1¶¶____
#__1¶¶¶11111111111111111¶¶_¶1¶1111111111¶¶¶11¶¶____
#___¶¶¶¶¶1111111111111111¶¶¶¶1111111111¶¶_¶_1¶¶____
#___1¶111¶¶¶11111111111111¶¶¶¶111111¶1¶¶_1¶_11¶____
#____¶¶1111¶¶¶111111111111¶¶¶1111111¶¶¶_¶¶1111¶____
#____1¶111111¶¶¶1111111111¶1¶¶1111111¶¶¶11¶11¶¶____
#_____¶¶1111111¶¶¶¶1111111¶¶¶¶111111111¶1¶¶_1¶¶____
#_____1¶1111111111¶¶¶¶1111¶¶1¶¶11111111¶¶¶¶_1¶1____
#______¶¶11111111111¶¶¶¶111¶1¶¶111111111¶¶¶__¶1____
#______1¶11111111111111¶¶¶¶¶_1¶1111111111¶¶111¶____
#_______¶¶111111111111111¶¶¶1¶¶1111111111¶¶¶¶¶¶1___
#________¶111111111111111¶¶__1¶¶¶11111111¶¶¶1¶¶¶___
#________¶¶111111111111111¶1__1¶1¶¶¶¶¶1111¶¶¶¶¶¶1__
#_________¶111111111111111¶¶___¶111¶¶¶¶¶¶¶¶¶¶_1¶___
#_________¶¶11111111111111¶¶___¶¶1111111¶¶¶____¶___
#__________¶1111111111111¶¶_____¶111111111¶________
#__________¶¶111111111111¶¶_____¶¶1111111¶¶________
#___________¶111111111111¶1______¶1111111¶¶________
#___________¶¶11111111111¶_______¶¶111111¶¶________
#____________¶1111111111¶¶________¶111111¶¶________
#____________¶¶111111111¶¶________¶¶11111¶¶________
#____________1¶111111111¶¶_________¶11111¶¶________
#_____________¶¶11111111¶1_________¶¶1111¶¶________
#_____________¶¶111¶1111¶__________1¶1111¶¶________
#______________¶111¶¶111¶¶__________¶¶1111¶________
#______________¶111¶¶111¶¶__________¶¶1111¶________
#______________¶11111111¶1__________1¶1¶¶1¶¶_______
#_____________¶¶11111111¶____________¶1¶¶11¶_______
#____________1¶111111111¶____________¶11__1¶_______
#____________¶¶11111111¶¶____________¶¶¶¶¶¶¶_______
#____________¶111111111¶¶____________¶¶¶¶¶¶¶_______
#____________¶1111111111¶____________¶¶¶¶¶¶¶¶______
#___________1¶1111111111¶____________¶¶¶¶¶¶¶¶______
#___________1¶1111111111¶1___________¶¶¶¶¶¶¶¶1_____
#____________¶1111111111¶¶___________1¶¶¶¶¶¶¶______
#____________¶1111111111¶¶____________¶¶¶¶¶¶¶______
#____________¶¶111111111¶¶____________¶¶¶¶¶¶¶¶_____
#____________1¶1111111111¶_____________¶¶¶¶¶¶¶_____
#_____________¶1111111111¶_____________¶¶¶¶¶¶¶¶____
#_____________¶¶111111111¶_____________1¶¶¶¶¶¶¶¶___
#______________¶111111111¶1____________¶¶¶¶¶¶¶¶¶¶__
#______________¶¶11111111¶1____________¶¶¶¶¶¶¶¶¶¶__
#_______________¶11111111¶¶___________¶¶¶¶¶¶¶¶¶¶1__
#_______________¶¶1111111¶¶___________¶¶¶¶¶¶¶¶¶¶___
#________________¶¶111111¶¶____________¶¶¶¶¶¶¶¶____
#_________________¶111111¶¶_____________¶¶¶¶¶¶_____