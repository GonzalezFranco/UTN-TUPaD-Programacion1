#Librerias
import random

#Ejercicio 1

for i in range (101):
    print(i)

#------------------------------------------------------------------------- 
#Ejercicio 2

num = input("Por favor ingrese un numero: ")
larg = len(num)
print(f"El numero ingresado contiene: {larg} digitos.")

#---------------------------------------------------------------------------
#Ejercicio 3

res = int(0)

numi = int (input("Por favor ingrese el primer numero: "))
numf = int (input("Por favor ingrese el ultimo numero: "))

for i in range(numi+1,numf,1):
    res = res + i

print(f"La suma de todos los numeros entre {numi} y {numf} excluyendo dichos numero ingresados es: {res}")  

#----------------------------------------------------------------------------
#Ejercicio 4

num = 1
res = 0
salida = 1

while num != 0:

    num = int(input("Por favor ahora ingrese un numero a sumar o ingrese (0) para finalizar y sumar todo lo ingresado: "))
    
    if num != 0:
        res = res + num

print(f"La sumatoria total de los numeros ingresados es: {res}")

#------------------------------------------------------------------------------
#Ejercicio 5

num = 0
resp = 0
intentos = 1

num = random.randint(0,9)

while res != num:

    res = int (input("Por favor ingrese el numero que estoy pensando: "))

    if (res != num):

        intentos = intentos + 1
        print("Incorrecto, vuelve a intentarlo.")

print(f"Felicidades, adivinaste el numero en {intentos} intentos")

#-----------------------------------------------------------------------------
#Ejercicio 6

for i in range (100,-1,-2):
    print (i)

#-----------------------------------------------------------------------------
#Ejercicio 7

res = int(0)

numi = int (input("Por favor ingrese un numero entero positivo: "))

for i in range(0,numi,1):
    res = res + i

print(f"La suma de todos los numeros entre 0 y {numi} es: {res}")  

#---------------------------------------------------------------------------------
#Ejercicio 8

par = int(0)
impar = int(0)
positivo = int(0)
negativo = int(0)

numing = int(input("Por favor ingrese cuantos numeros ingresara: "))

for i in range (0,numing,1):

    num = int(input("Por favor ingrese un numero: "))

    if (num % 2 == 0):
        par = par + 1
    else:
        impar = impar + 1  

    if (num >= 0):
        positivo = positivo + 1 
    else:
        negativo = negativo + 1

print (f"De los {numing} numeros ingresados habian:")
print (f"Numeros pares = {par}.")
print (f"Numeros impares = {impar}.")
print (f"Numeros positivos = {positivo}.")
print (f"Numeros negaticos = {negativo}.")

#----------------------------------------------------------------------------------------
#Ejercicio 9

res = int(0)

numing = int(input("Por favor ingrese cuantos numeros ingresara: "))

for i in range (0,numing,1):

    num = int(input("Por favor ingrese un numero: "))

    res = res + num
    
res = res / numing
print(f"La media es: {res}")    

#---------------------------------------------------------------------------------------
#Ejercicio 10
numinvco = str("")
num = (input("Por favor ingrese un numero: "))

largo = len(num) - 1

for largo in range (largo,-1,-1):

    numeinv = num[largo]
    
    numinvco = numinvco + numeinv
    
print (numinvco)

#--------------------------------------------------------------------------------------