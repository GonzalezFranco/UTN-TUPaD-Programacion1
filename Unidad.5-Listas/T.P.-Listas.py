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
notas = [[10,8,6,"Alejo"],[2,10,10,"Alejando"],[10,10,10,"Tamara"],[5,10,7,"Franco"],[3,5,9,"Rodrigo"]]

prom_mat =0
prom_pro = 0
prom_log = 0
prom_a = 0

for i in range (len(notas)):
    matematica = notas[i][0]
    programacion = notas[i][1]
    logica = notas [i][2]
    alumno = notas [i][3]
    prom_mat = prom_mat + matematica
    prom_pro = prom_pro + programacion
    prom_log = prom_log + logica
    prom_a = (matematica + programacion + logica) / 3
    print(f"El alumno {alumno} tiene como notas: {matematica},{programacion},{logica} y tiene un promedio gral de: {prom_a}")
prom_mat = prom_mat / 5
prom_pro = prom_pro / 5
prom_log = prom_log / 5    
print(f"El promedio gral. de Matematica es: {prom_mat}, el de Programacion es: {prom_pro} y el de Logica es: {prom_log}")
#--------------------------------------------------------------------
#Ejercicio9 

tablero = [["-" for _ in range(3)] for _ in range(3)]
salida = True
turno = 0

for fila in tablero:
    print(" ".join(fila))

while salida == True:
    
    if turno % 2 == 0:
        jugador = "X" 
    else:
        jugador = "O"
    print(f"Turno del jugador {jugador}")

    num_val = True
    while num_val == True:

        fila = (input("Ingresa la fila (1, 2, 3): "))
        columna = (input("Ingresa la columna (1, 2, 3): "))
        if ((fila == "1" or fila == "2" or fila == "3") and (columna == "1" or columna == "2" or columna == "3") and (fila != "" and columna != "")):
            fila = int(fila)
            columna = int(columna)
            fila -= 1
            columna -= 1
            
            if tablero[fila][columna] == "-":
                tablero[fila][columna] = jugador
                num_val = False
            else:
                print("Casilla ocupada. Reintentalo")           
        else:
            print("El numero ingresado no es valido, por favor vuelva a ingresarlos segun lo especificado.")

    for fila_tablero in tablero:
        print(" ".join(fila_tablero))
   
        if fila_tablero == [jugador, jugador, jugador]:
            salida = False

    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            salida = False        

    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        salida = False
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        salida = False

    if turno == 8 and salida == True:
        print("¡Empate!")
        salida = False
    else:
        turno += 1
    
print(f"Felicidades el jugador {jugador} es el ganador")
#--------------------------------------------------------------------
#Ejercicio10

ventas = [
    [5, 6, 20, 15, 19, 1, 7],   
    [10,25,3,6,7,8,11],      
    [13,15,12,20,22,4,9], 
    [12,5,9,20,11,14,12]         
]

print("Total vendido por cada producto:")
for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto += ventas[i][j]
    print(f"Producto {i+1}: {total_producto}")

mayor_ventas = 0
dia_mayor = 0
for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    if total_dia > mayor_ventas:
        mayor_ventas = total_dia
        dia_mayor = j
print(f"\nDía con mayores ventas totales: Día {dia_mayor+1} con {mayor_ventas} unidades")

mayor_producto = 0
indice_producto = 0
for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto += ventas[i][j]
    if total_producto > mayor_producto:
        mayor_producto = total_producto
        indice_producto = i
print(f"\nProducto más vendido en la semana: Producto {indice_producto+1} con {mayor_producto} unidades")
