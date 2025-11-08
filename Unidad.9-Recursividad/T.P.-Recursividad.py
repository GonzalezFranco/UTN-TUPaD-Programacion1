#Libreria
import os

# 1) Factorial recursivo y mostrar todos los factoriales hasta N
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def mostrar_factoriales_hasta_n():
    N = int(input("Ingrese un número para calcular todos los factoriales hasta ese número: "))
    for i in range(1, N+1):
        print(f"Factorial de {i}: {factorial(i)}")

# 2) Fibonacci recursivo y mostrar la serie hasta N
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def mostrar_fibonacci_hasta_n():
    N = int(input("Ingrese una posición hasta la cual mostrar la serie de Fibonacci: "))
    serie = [fibonacci(i) for i in range(N+1)]
    print("Serie de Fibonacci:")
    print(serie)

# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def probar_potencia():
    n = int(input("Base: "))
    m = int(input("Exponente: "))
    print(f"{n} elevado a {m} es {potencia(n, m)}")

# 4) Decimal a binario recursivo
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def probar_binario():
    n = int(input("Ingrese un número decimal para convertir a binario: "))
    binario = decimal_a_binario(n)
    # Maneja el caso de 0, pues la función regresa cadena vacía
    print(f"Binario: {binario if binario else '0'}")

# 5) Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

def probar_palindromo():
    palabra = input("Ingrese una palabra para verificar si es palíndromo: ")
    if es_palindromo(palabra):
        print("Es palíndromo.")
    else:
        print("No es palíndromo.")

# 6) Suma recursiva de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

def probar_suma_digitos():
    n = int(input("Ingrese un número para sumar sus dígitos: "))
    print(f"Suma de sus dígitos: {suma_digitos(n)}")

# 7) Contar bloques de pirámide
def contar_bloques(n):
    if n <= 1:
        return n
    else:
        return n + contar_bloques(n - 1)

def probar_contar_bloques():
    n = int(input("Bloques en el nivel más bajo: "))
    print(f"Total de bloques necesarios: {contar_bloques(n)}")

# 8) Contar veces que aparece un dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    # extrae último dígito y compara
    count = 1 if numero % 10 == digito else 0
    return count + contar_digito(numero // 10, digito)

def probar_contar_digito():
    numero = int(input("Número: "))
    digito = int(input("Dígito a contar (0-9): "))
    print(f"El dígito aparece {contar_digito(numero, digito)} veces.")

mostrar_factoriales_hasta_n()
mostrar_fibonacci_hasta_n()
probar_potencia()
probar_binario()
probar_palindromo()
probar_suma_digitos()
probar_contar_bloques()
probar_contar_digito()