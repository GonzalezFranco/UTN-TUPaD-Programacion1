#Ejercicio1 --------------------------------------------------------------------------------
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva':1450}                 #|
                                                                                            #|
precios_frutas ["Naranja"] = 1200                                                           #|
precios_frutas ["Manzana"] = 1200                                                           #| 
precios_frutas ["Pera"] = 1200                                                              #|
                                                                                            #|
print(precios_frutas,"\n")                                                                       #|
                                                                                            #|
#---------------                                                                            #|
#Ejercicio2                                                                                  |
precios_frutas ["Banana"] = 1330                                                            #|
precios_frutas ["Manzana"] = 1700                                                           #|
precios_frutas ["Melon"] = 2800                                                             #|
                                                                                            #|
print(precios_frutas,"\n")                                                                       #|
                                                                                            #|
#---------------                                                                             #|
#Ejercicio3                                                                                  |
frutas = list(precios_frutas.keys())                                                        #|
print (frutas)                                                                              #|
                                                                                            #|
#--------------------------------------------------------------------------------------------|
#Ejercicio4
def mod_agenga():
    for i in range (5):
        nombre = input("Por favor ingrese su nombre: ")
        telefono = int(input("Por favor ingrese su numero de telefono: "))
        agenda [nombre] = telefono
        
agenda = {}
mod_agenga()

name = input("Por favor, ingrese el nombre que desea ubicar en el diccionario: ")
if name in agenda:
    print(agenda.get(name))
else:
    print("El nombre que busca no se encuentra en el diccionario.")

#--------------------------------------------------
#Ejercicio5
frase = input("Ingrese una frase: ")
palabras_unicas = set(frase.split())
print("Palabras únicas:", palabras_unicas)

cantidad_palabras = {}

for palabra in frase.split():
    if palabra in cantidad_palabras:
        cantidad_palabras[palabra] += 1
    else:
        cantidad_palabras[palabra] = 1

print("Cantidad de veces que aparece cada palabra:", cantidad_palabras)

#--------------------------------------------------
#Ejercicio6

def tup_alumnos():
    for i in range(3):
        nombre = input("Por favor ingrese su nombre: ")
        notas = []
        for j in range(3):
            nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
            notas.append(nota)
        alumnos[nombre] = tuple(notas)

alumnos = {}
tup_alumnos()

print("Promedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#--------------------------------------------------
#Ejercicio7

parcial1 = {101, 102, 103, 104, 105}
parcial2 = {103, 104, 106, 107}

ambos = parcial1 & parcial2
print("Aprobó ambos parciales:", ambos)

solo_uno = (parcial1 ^ parcial2)
print("Aprobó solo uno de los dos:", solo_uno)

uno = parcial1 | parcial2
print("Aprobó al menos un parcial:",uno)

#--------------------------------------------------
#Ejercicio8

stock_productos = {
    "manzanas": 17,
    "bananas": 53,
    "naranjas": 22
}

def mostrar_menu():
    print("--- Menú de opciones ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Elegí una opción (1-4): ")

    if opcion == "1":
        producto = input("Ingresá el nombre del producto a consultar: ").lower()
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print(f"El producto '{producto}' no está registrado.")

    elif opcion == "2":
        producto = input("Ingresá el nombre del producto a actualizar: ").lower()
        if producto in stock_productos:
            cantidad = int(input(f"¿Cuántas unidades querés agregar a {producto}? "))
            stock_productos[producto] += cantidad
            print(f"Se agregaron {cantidad} unidades. Nuevo stock: {stock_productos[producto]}")
        else:
            print(f"El producto '{producto}' no existe. Usá la opción 3 para agregarlo.")

    elif opcion == "3":
        producto = input("Ingresá el nombre del nuevo producto: ").lower()
        if producto in stock_productos:
            print(f"El producto '{producto}' ya existe. Usá la opción 2 para agregar unidades.")
        else:
            cantidad = int(input(f"Ingresá la cantidad inicial de stock para {producto}: "))
            stock_productos[producto] = cantidad
            print(f"Producto '{producto}' agregado con {cantidad} unidades.")

    elif opcion == "4":
        print("¡Gracias por usar el sistema de stock!")
        break

    else:
        print("Opción inválida. Por favor elegí entre 1 y 4.")

#--------------------------------------------------
#Ejercicio9

agenda = {
    ("lunes", "10:00"): "Programación 1",
    ("martes", "17:00"): "Matemática",
    ("miércoles", "18:00"): "AySO",
    ("jueves", "19:00"): "OE",
    ("viernes", "08:00"): "Base de Datos"
}

def consultar_agenda():
    dia = input("Ingresá el día (ej: lunes): ").lower()
    hora = input("Ingresá la hora (ej: 10:00): ")
    clave = (dia, hora)
    
    if clave in agenda:
        print(f"El evento programado el {dia} a las {hora} es: {agenda[clave]}")
    else:
        print(f"No hay actividades registradas para el {dia} a las {hora}.")


consultar_agenda()

#--------------------------------------------------
#Ejercicio10

paises = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Japón": "Tokio",
    "Brasil": "Brasilia",
    "Italia": "Roma"
}


capitales = {capital: pais for pais, capital in paises.items()}


print("Diccionario invertido (capital → país):")
for capital, pais in capitales.items():
    print(f"{capital}: {pais}")
