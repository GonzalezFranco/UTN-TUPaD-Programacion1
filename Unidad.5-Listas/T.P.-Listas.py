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

listaO = [1,3,5,3,7,1,9,5,3]
listaM = []
for i in range(len(listaO)):
    if listaO[i] not in listaM:
        listaM.append(listaO[i])
print(f"La lista sin numeros repetidos es: {listaM}")
