Algoritmo Ejercicio10
	//Diseñar un programa que calcule la longitud de una circunferencia y el área. El usuario debe ingresar el radio. 
	Definir long, diametro, circunferencia, area, radio Como Real
	
	diametro = 0
	circunferencia = 0
	area = 0
	radio = 0
	
	Escribir "Por favor ingrese el radio de la circunferencia (en Cm): "
	Leer radio
	diametro = 2 * radio
	circunferencia = diametro * PI
	area = radio^2 * PI
	Escribir "La longitud de la circunferencia es de: ", circunferencia, "Cm y su area de: ", area, "Cm^2"
FinAlgoritmo
