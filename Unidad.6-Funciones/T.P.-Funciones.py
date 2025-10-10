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
pass
