#Ejercicio1
print ("Ejercicio 1")
print("Hola Mundo!")

#Ejercicio2
print ("Ejercicio 2")
Nombre = input ("Por favor, ingrese su nombre a continuacion: ")
print(f"Hola {Nombre}!")

#Ejercicio3
print ("Ejercicio 3")
Nombre = input("Por favor, ingrese su nombre: ")
Apellido = input("Estupendo, ahora ingrese su apellido: ")
Edad = input("A continuacion, ingrese su edad: ")
Direccion = input("Finalmente, ingrese su lugar de residencia: ")
print(f"Soy {Nombre} {Apellido}, tengo {Edad} años y vivo en {Direccion}.")

#Ejercicio4
print ("Ejercicio 4")
Radio = float(input("Por favor, ingrese el radio del circulo: "))
Area = Radio ** 2 * 3.14
Perimetro = Radio * 2 * 3.14
print(f"El area del circulo es {Area} y su perimetro es {Perimetro}.")

#Ejercicio5
print ("Ejercicio 5")
Segundos = int(input("Por favor, ingrese la cantidad de segundos que quiere convertir a horas: "))
Horas = Segundos // 3600
print(f"{Segundos} segundos equivalen a {Horas} horas.")

#Ejercicio6
print ("Ejercicio 6")
Numero = int(input("Por favor ingrese el numero del cual quiere saber la tabla de multiplicar: "))
for i in range (1,10):
    Tabla = Numero * i
    print(f"{Numero} * {i} = {Tabla}")

#Ejercicio7
print ("Ejercicio 7")
num1 = int(input("Por favor, ingrese un numero positivo y distinto a 0: "))
num2 = int(input("Estupendo, ahora ingrese el segundo numero cumpliendo las mismas indicaciones anteriores: "))
if (num1 != 0 and num2 != 0) and (num1 > 0 and num2 > 0):
    print("La suma de los numeros es: ", num1 + num2)
    print("La division de los numeros es: ", num1 / num2)
    print("La multiplicacion de los numeros es: ", num1 * num2)
    print("La resta de los numeros es: ", num1 - num2)
else: 
    print("Alguno de los numeros ingresados es 0 o un numero negativo, por favor cumpla las indicaciones que se les pide.")  

#Ejercicio8
print ("Ejercicio 8")
Altura = float(input("Por favor, ingrese su altra estimada en Metros: "))
Peso = float(input("Ahora, ingrese su peso estimado en Kg: "))    
print(f"Su indice de masa corporal es: {Peso / (Altura ** 2)}")

#Ejercicio9
print ("Ejercicio 9")
TempC = float(input("Por favor, ingrese la temperatura en grados Celsius: "))
print(f"La temperatura {TempC}°C equivale a {((TempC * 9) / 5) + 32}°F")

#Ejercicio10
print ("Ejercicio 10")
num1 = float(input("Por favor, ingrese un numero: "))
num2 = float(input("Ahora, ingrese el segundo numero: "))
num3 = float(input("Finalmente, ingrese el tercer numero: "))
print(f"El promedio de los 3 numeros ingresados es: {(num1 + num2 + num3) / 3}")

