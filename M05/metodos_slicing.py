# ==============================================================================
# Guía de Trabajo 2: Métodos, Slicing y Matemáticas en Python
# Archivo: metodos_slicing.py
# Grecia Lopez Orozco
# ==============================================================================


# Sección 1 

# Código 1.1:
num = int(input("Introduce el número inicial: "))
for i in range(num, 0, -1):
    print("Conteo:", i)

# Sección 2

import math

decNum = -34.5678
intNum = 9

print( round(decNum, 2) )   # Línea A
print( round(decNum, 0) )   # Línea B
print( int(decNum) )        # Línea C
print( abs(decNum) )        # Línea D

print( math.pow(intNum, 2) ) # Línea E
print( math.sqrt(intNum) )   # Línea F

# Predicciones de Salida:
# 5. Línea A: -34.57
# 6. Línea B: -35.0
# 7. Línea C: -34  (decimales)
# 8. Línea D: 34.5678
# 9. Línea E: 81.0
# 10. Línea F: 3.0



# Sección 3 

miMax = max("Banano", "manzana", "Zanahoria")
print("El máximo es:", miMax)

# Sección 4

d = int(input("Ingresa la longitud de la huella de frenado (en metros): "))
v = math.sqrt(20 * d)
print("Velocidad estimada del auto:", round(v, 2), "km/h")


# Sección 5

nombre = "Building Puentes"

print("Índice 0:", nombre[0])
print("Segmento:", nombre[8:15])


texto = input("Ingresa una frase con letras y números: ")
contador_numeros = 0
for caracter in texto:
    if caracter >= "0" and caracter <= "9":
        contador_numeros += 1

print("Total de dígitos numéricos encontrados:", contador_numeros)

