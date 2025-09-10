#Librerias
import random
#Ejercicio1

for i in range (101):
    print(i)

#------------------------------------------------------------------------- 
#Ejercicio2

num = input("Por favor ingrese un numero: ")
larg = len(num)
print(f"El numero ingresado contiene: {larg} digitos.")

#---------------------------------------------------------------------------
#Ejercicio3

res = int(0)

numi = int (input("Por favor ingrese el primer numero: "))
numf = int (input("Por favor ingrese el ultimo numero: "))

for i in range(numi+1,numf,1):
    res = res + i

print(f"La suma de todos los numeros entre {numi} y {numf} excluyendo dichos numero ingresados es: {res}")  

#----------------------------------------------------------------------------
#Ejercicio4

res = 0
salida = 1

while salida != 0:
    num = int(input("Por favor ahora ingrese un numero a sumar: "))
    if num == 0:
        break
    else:
        res = res + num

print(f"La sumatoria total de los numeros ingresados es: {res}")

#------------------------------------------------------------------------------
#Ejercicio5

num = 0
resp = 10
intentos = 0

num= [random.randint(0,9)]

print (num)

while resp != num:

    resp = int(input("Por favor adivine el numero en que estoy pensando entre (0 y 9): "))

    if (resp != num):

        intentos = intentos + 1
        print("Buen intento, pero no estoy pensando en ese numero, proba de nuevo.")

print(f"Felicidades, adivinaste el numero en {intentos} intentos")
