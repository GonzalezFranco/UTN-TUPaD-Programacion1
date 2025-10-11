#Librerias
import math

#------------------------------------------------------
#Eejercicio1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#------------------------------------------------------
#Ejercicio2

def saludar_usuario(nombre):
    print(f"Hola {nombre}")

nombre = input("Por favor ingrese su nombre: ")

saludar_usuario(nombre)

#------------------------------------------------------
#Ejercicio3

def informacion_personal(nombre,apellido,edad,domicilio):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {domicilio}")

nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = int(input("Por favor, ingrese su edad: "))
domicilio = input("Por ultimo ingrese su domicilio por favor: ")

informacion_personal(nombre,apellido,edad,domicilio)

#------------------------------------------------------
#Ejercicio4
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2) 
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio = float(input("Por favor ingrese el radio del circulo al cual desea sacar el area y perimetro: "))

print(f"El area del circulo es: {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")

#------------------------------------------------------
#Ejercicio5

def segundos_a_horas(segundos):
    minutos = segundos / 60
    horas = minutos / 60
    return horas

segundos = int(input("Por favor ingrese la cantidad de segundos que desea pasar a horas: "))

print(f"Los segundos ingresados son: {segundos_a_horas(segundos)} Hrs.")

#------------------------------------------------------
#Ejercicio6

def tabla_multiplicar(numero):
    for i in range (11):
        print (f"{numero} * {i} = {numero * i}")
               
numero = int(input("Por favor ingrese el numero del cual quiere saber su tabla de multiplicar: "))

tabla_multiplicar(numero)

#------------------------------------------------------
#Ejercicio7
def operaciones_basicas(a,b):
    print(f"La suma de dichos numeros es: {a + b}")
    print(f"La resta de dichos numeros es: {a - b}")
    print(f"La multiplicacion de dichos numeros es: {a * b}")
    print(f"La division de dichos numeros es: {a / b}")
    

a = int(input("Por favor ingrese el primer digito: "))
b = int(input("Por favor ingrese el segundo digito: "))

operaciones_basicas(a,b)

#------------------------------------------------------
#Ejercicio8

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    imc = round(imc,2)
    return imc

peso = float(input("Por favor ingrese su peso en Kg. : "))
altura = float(input("Por favor ingrese su altura en Metros: "))

print(f"Su indice de masa corporal es: {calcular_imc(peso, altura)}")

#-------------------------------------------------------
#Ejercicio9

def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

celsius = float(input("Por favor ingrese la temperatura actual en grados celcius: "))

print(f"La temperatura en grados fahrenheit es: {celsius_a_fahrenheit(celsius)}")

#-------------------------------------------------------
#Ejercicio10

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = float(input("Por favor ingrese el primer numero: "))
b = float(input("Por favor ingrese el segundo numero: "))
c = float(input("Por favor ingrese el tercer numero: "))

print(f"El promedio de los tres numeros es: {calcular_promedio(a,b,c)}")