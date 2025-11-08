#librerias
import os

documento = "productos.txt"
productos = []  # Lista de diccionarios

# Ejercicio 1: Crear archivo inicial con productos
with open(documento, "w", encoding="UTF-8") as archivo:
    archivo.write("Calabaza,180,2\n")
    archivo.write("Salamin,246,1\n")
    archivo.write("Limon,180,2\n")

# Ejercicio 2 y 4: Leer archivo y cargar en lista de diccionarios
def leer_archivo():
    productos.clear()
    with open(documento, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) == 3:
                nombre = datos[0]
                precio = float(datos[1].strip())
                cantidad = int(datos[2].strip())
                productos.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })
    # Mostrar productos
    for prod in productos:
        print(f"Producto: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")

leer_archivo()

# Ejercicio 3: Agregar producto desde teclado
with open(documento, "a", encoding="UTF-8") as archivo:
    archivo.write(input("Por favor ingrese un nuevo producto, su precio y la cantidad, separado por comas: "))

leer_archivo()

# Ejercicio 4: La lista productos ya queda cargada como lista de diccionarios
print("\nLista final de productos en memoria:")
print(productos)

# Ejercicio 5: Buscar producto por nombre
busqueda = input("\nIngrese el nombre de un producto para buscar: ")
encontrado = False
for prod in productos:
    if prod["nombre"].lower() == busqueda.strip().lower():
        print(f"Producto encontrado: {prod}")
        encontrado = True
        break
if not encontrado:
    print("Error: El producto no existe.")

# Ejercicio 6: Guardar productos actualizados (sobrescribir el archivo)
with open(documento, "w", encoding="UTF-8") as archivo:
    for prod in productos:
        archivo.write(f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n")
print("\nArchivo actualizado correctamente.")