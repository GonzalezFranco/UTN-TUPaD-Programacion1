#Librerias:
import random
#--------------------------------------------------------------------
#Ejercicio1
notas = [10,8,4,5,9,10,2,4,7,6]
notaAlta = max(notas)
notaBaja = min(notas)
promedio = float(0) 

for i in range(len(notas)):    
    promedio = ((promedio + notas[i])) 

promedio = promedio / len(notas)
print (f"Las notas de los estudiantes son: {notas}.")
print (f"El promedio de dichas notas son: {promedio}.")
print (f"La nota mas alta es: {notaAlta}.")
print (f"La nota mas baja es: {notaBaja}.")

#--------------------------------------------------------------------
#Ejercicio2

productos = []

for i in range(5):
    productos.append(input("Ingrese un producto: "))

productos = sorted(productos)
print(f"Los productos ordenados son: {productos}")
productos.remove(input("'Que producto desea eliminar?: "))
print(f"La lista actualizada es: {productos}")

#--------------------------------------------------------------------
#Ejercicio3

lista = [random.randint(1,100) for i in range(15)]
listapar = []
listaimpar = []

print(lista)
for i in range(len(lista)):
    res = lista[i] % 2
    if res == 0:
        listapar.append(lista[i])
    else:
        listaimpar.append(lista[i])
par = len(listapar)
impar = len(listaimpar)
print(f"La lista par tiene: {par} numeros")
print (f"La lista impar tiene: {impar} numeros" )

#--------------------------------------------------------------------
#Ejercicio4

lista_r = [1,3,5,3,7,1,9,5,3]
lista_m = []
   
for i in range(len(lista_r)):
    if (lista_r[i] not in lista_m):
         lista_m.append(lista_r[i])   

print(lista_m)

#--------------------------------------------------------------------
#Ejercicio5

lista_n = ["Tamara","Joaquin","Emanuel","Diana","Cintia","Ramiro","Carlos","Romina"]

opc= input("¿Quiere agregar un estudiante a su clase (Agregar) o eliminarlo (Eliminar)?: ")

if (opc.lower() == "agregar"):
    nombre = input("Por favor ingrese el nombre del alumno que agregara a su curso: ")
    lista_n.append(nombre)
elif (opc.lower() == "eliminar"):
    print(f"Actualmente sus alumnos son: {lista_n}")
    nombre_d = input("Por favor ingrese el nombre del alumno a eliminar de su curso: ")
    lista_n.remove(nombre_d)
else:
    print("Por favor ingrese una de las dos opciones anteriores mencionadas.")    
print(f"Su curso esta compuesto por los alumnos: {lista_n}")

#--------------------------------------------------------------------
#Ejercicio6

lista_v = [0,1,2,3,4,5,6]

ud = lista_v.pop()
lista_v.insert(0,ud)
print(lista_v)

#--------------------------------------------------------------------
#Ejercicio7

lista_r = [[10,24],[2,12],[5,8],[16,17],[14,20],[22,30],[12,18]]
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

tempmax = 0
tempmin = lista_r[0][0]
promtmax = 0
promtmin = 0
for i in range (len(lista_r)):
    promtmax = promtmax + lista_r[i][1]
    promtmin = promtmin + lista_r[i][0]
    if (lista_r[i][1] > tempmax):
        tempmax = lista_r[i][1]
        tempmini = lista_r[i][0]
        dia = dias[i]
        
    if (lista_r[i][0] < tempmin):
        tempmin = lista_r[i][0]  

amplitud = tempmax - tempmini
promtmin = round(promtmin / (len(lista_r)))
promtmax = round(promtmax / (len(lista_r)))

print(f"La temperatura minima de la semana fue: {tempmin}°")
print(f"La temperatura maxima de la semana fue: {tempmax}°")
print(f"El promedio de la temperatura maxima es: {promtmax}°")
print(f"El promedio de la temperatura minima es: {promtmin}°")
print(f"La mayor amplitud térmica fue de {amplitud}°C el día {dia}")
#--------------------------------------------------------------------
#Ejercicio8