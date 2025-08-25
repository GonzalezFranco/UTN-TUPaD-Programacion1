#Librerias
import random
from statistics import mode,median,mean
#--------------------------------------------------------------------------------------------
#1
edad = int(input("Por favor ingrese su edad: "))
if(edad > 18):
    print("Es mayor de Edad.")
#--------------------------------------------------------------------------------------------
#2 
nota = int (input("Por favor ingrese su nota: "))
if (nota >= 6):
    print("Aprobado.")
else:
    print("Desaprobado.")
#--------------------------------------------------------------------------------------------
#3
numero = int(input("Por favor ingrese un numero: "))
par = numero % 2
if par == 0:
    print("Ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")    
#--------------------------------------------------------------------------------------------
#4
edad = int(input("Por favor ingrese su edad: "))
if (edad < 12):
    print("Usted es un niño/a.")
elif ((edad >= 12)and(edad < 18)):
    print ("Usted es un Adolecente.")
elif (edad >= 18)and(edad<30):
    print ("Usted es un adulto joven.")
elif (edad >= 30):
    print ("Usted es un adulto.")    
#--------------------------------------------------------------------------------------------
#5
Pass = str(input("Por favor ingrese una contraseña de 8 a 14 caracteres: "))
Lpass = len(Pass)
if (Lpass >= 8) and (Lpass <= 14):
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")    
#--------------------------------------------------------------------------------------------
#6
NumAl = [random.randint(1, 100) for i in range (50)]
Pro = mean (NumAl)  #MEDIA
Mid = median (NumAl) #MEDIANA
ValCom = mode (NumAl) #MODA
if (Pro > Mid and Mid > ValCom):
    print ("Hay sesgo positivo.")
elif (Pro < Mid) and (Mid < ValCom):
    print ("Hay sesgo negativo.")
else:
    print ("No hay sesgo.")
#--------------------------------------------------------------------------------------------
#7
pal = str(input("Por favor ingrese una palabra: "))
Lpal = len(pal)
for Lpal in pal:
   car=Lpal   

if (((car == "a" or car == "e")or(car == "i" or car == "o")) or (car == "u")):
    print(f"{pal}!")
else:
    print(pal)
#----------------------------------------------------------------------------------------------
#8
nombre = str(input("Por favor ingrese su nombre: "))
print ("1. Si quiere su nombre en mayusculas.")
print ("2. Si quiere su nombre en minusculas.")
print ("3. Si quiere su nombre con la primer letra en mayuscula.")
opc = int(input("Seleccione el numero que corresponda a la opcion que desee llevar a cabo: "))
May = nombre.upper()
Min = nombre.lower()
Tit = nombre.title()
if (opc == 1):
    print(May)
elif (opc == 2):
    print(Min)
elif (opc == 3):
    print(Tit)
else:
    print("Por favor ingrese una opcion valida.") 
#-----------------------------------------------------------------------------------------------
#9
Magn = str(input("Por favor ingrese la magnitud de un terremoto: "))
Mag = float(Magn)
if (Mag >= 0 and Mag < 3):
    print("Muy Leve (Imperceptible).")
elif (Mag >=3 and Mag < 4):
    print("Leve (Ligeramente Perceptible).")
elif (Mag >= 4 and Mag < 5):
    print("Moderado (Sentido por personas, pero generalmente no causa daños).")
elif (Mag >= 5 and Mag < 6):
    print("Fuerte (Puede causar daños en estructuras debiles).")
elif (Mag >= 6 and Mag < 7):
    print("Muy Fuerte (Puede causar daños significativos).")
elif (Mag >= 7):
    print("Extremo (Puede causar grandes daños a escala).")
elif (Mag < 0):
    print ("Por favor ingrese una escala de magnitud existente.")
#-----------------------------------------------------------------------------------------------
#10
Emis = str(input("En que emisferio se encuentra(N/S): "))
mes = int(input("En que mes esta: "))
dia = int(input("Que dia es hoy: "))
if (Emis == "N" or Emis == "n"):
    if(((mes == 12 and (dia >=21 and dia <= 31)) or mes == 1) or (mes == 2 or (mes == 3 and (dia <=20 and dia >=1)))):
        print ("Usted esta en Invierno.")
    elif(((mes == 3 and (dia >=21 and dia <= 31)) or mes == 4) or (mes == 5 or (mes == 6 and (dia <=20 and dia >=1)))):
        print ("Usted esta en Primavera.")
    elif(((mes == 6 and (dia >=21 and dia <= 31)) or mes == 7) or (mes == 8 or (mes == 9 and (dia <=20 and dia >=1)))):
        print ("Usted esta en Verano.")    
    elif(((mes == 9 and (dia >=21 and dia <= 31)) or mes == 10) or (mes == 11 or (mes == 12 and (dia <=20 and dia >=1)))):
        print ("Usted esta en Otoño.")
    else:
        print("Usted ingreso un mes o dia inexistente.") 
elif (Emis == "S" or Emis == "s"):
    if(((mes == 12 and (dia >=21 and dia <= 31)) or mes == 1) or (mes == 2 or (mes == 3 and (dia <=20 and dia >=1)))):
        print ("Usted esta en Verano.")
    elif(((mes == 3 and (dia >=21 and dia <= 31)) or mes == 4) or (mes == 5 or (mes == 6 and (dia <=20 and dia >=1)))):
        print ("Usted esta en Otoño.")
    elif(((mes == 6 and (dia >=21 and dia <= 31)) or mes == 7) or (mes == 8 or (mes == 9 and (dia <=20 and dia >=1)))):
        print ("Usted esta en Invierno.")    
    elif(((mes == 9 and (dia >=21 and dia <= 31)) or mes == 10) or (mes == 11 or (mes == 12 and (dia <=20 and dia >=1)))):
        print ("Usted esta en Primavera.")
    else:
        print("Usted ingreso un mes o dia inexistente.")