Algoritmo Ejercicio9
	//Dise�ar un programa que dado el precio final de un art�culo, calcule cu�l es el IVA que tiene incluido. 
	
	Definir Precio, PrecioFin, Iva Como Real
	Precio = 0
	PrecioFin = 0
	Iva = 0
	
	Escribir "Por favor ingresar el Precio del articulo a comprar: "
	Leer Precio
	PrecioFin = (Precio * 21) / 100
	PrecioFin = PrecioFin + Precio
	Escribir "Su producto con el Iva incluido es: ", PrecioFin
FinAlgoritmo
