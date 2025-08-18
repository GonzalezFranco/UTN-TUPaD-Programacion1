Algoritmo Ejercicio7
	//Escribe un programa que calcule el área y el perímetro de un triángulo rectángulo. El usuario debe proporcionar dos catetos.
	Definir Area, Perimetro, Cat1, Cat2, Hipo Como Real
	
	Area = 0
	Perimetro = 0
	Cat1 = 0
	Cat2 = 0
	Hipo = 0
	
	Escribir "Por favor ingresar el Primer cateto: "
	Leer Cat1
	Escribir  "Por favor ingresarel Segundo cateto: "
	Leer Cat2
	Hipo = raiz(Cat1^2 + Cat2^2)
	Perimetro = Cat1 + Cat2 + Hipo
	Area = (Cat1*Cat2)/2
	Escribir "El Area del triangulo rectangulo es: ", Area, " y su perimetro es: ", Perimetro
FinAlgoritmo
