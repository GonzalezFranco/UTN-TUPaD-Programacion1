Algoritmo Ejercicio6
	//Diseña un programa que pida al usuario dos números enteros. 
	//Posteriormente muestra por pantalla el resultado de sumarlos, dividirlos, multiplicarlos, restarlos...
	//La potencia del primero elevado al segundo, y el resto de dividir el primero entre el segundo. 
	
	Definir A, B Como entero
	Definir Resul Como Real
	
	A = 0
	B = 0
	Resul = 0
	
	Escribir "Por favor ingrese el primer numero entero: "
	Leer A
	Escribir "Por favor ingrese el segundo numero entero: "
	Leer B
	
	Resul = A + B
	Escribir "La Sumatoria de esta cuenta es: ", Resul
	Resul = A - B
	Escribir "La Resta de esta cuenta es: ", Resul
	Resul = A * B
	Escribir "La Multiplicacion de esta cuenta es: ", Resul
	Resul = A / B
	Escribir "La Division de esta cuenta es: ", Resul
	Resul = A^B
	Escribir "La potencia de esta cuenta es: ", Resul
	Resul = A MOD B
	Escribir "El Resto de la divicion entre estos numeros es: ", Resul
FinAlgoritmo
