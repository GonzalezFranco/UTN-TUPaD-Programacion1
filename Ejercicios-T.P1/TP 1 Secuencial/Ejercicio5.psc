Algoritmo Ejercicio5
	//Dise�a un programa que calcule el precio final de un art�culo. El usuario debe ingresar el precio inicial y el porcentaje de descuento.
	Definir PrecioIni, PrecioFin, Descuento Como Real
	
	PrecioIni = 0
	PrecioFin = 0
	Descuento = 0
	
	Escribir "Buenos d�as, por favor ingresar el precio inicial del producto: "
	Leer PrecioIni
	Escribir "Ahora ingrese el porcentaje de descuento que posee: "
	Leer Descuento
	PrecioFin = (PrecioIni * Descuento) /100
	PrecioFin = PrecioIni - PrecioFin
	Escribir "El precio final de su producto es de: $", PrecioFin
FinAlgoritmo
