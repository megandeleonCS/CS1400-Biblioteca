# ==========================================
#  M5 Tarea 1
#  Christian Mendoza  
#  Fecha: 2026-09-29
# ==========================================
"""
# Sección 1: Conteo Inverso con range()
# Analizaremos cómo usar pasos negativos para contar hacia atrás.
# ==========================================

#Código 1.1:

# Conteo descendente
num = int(input("Introduce el número inicial: "))

for i in range(num, -1, -2):
    print("Conteo:", i)

Análisis:
# 1. Ejecuta el programa e introduce 10. Al observar la consola, ¿en qué número comenzó la cuenta y en cuál terminó?

Inicio: en el 10 | Fin: en el 1

# 2. ¿Por qué es necesario que el parámetro step (paso) sea un número negativo al realizar un conteo descendente?
Por que se parametro determina cuanto se suma en cada iteracion, al ser un numero negativo, le dices que vaya restando esa cantidad.

# 3. ¿Por qué el valor final se configuró en 0 si queríamos que el conteo se detuviera en el número 1?
Por que se excluye el numero del valor final especificado en el range().

Práctica de Sección:
# 4. Modifica el código para que cuente hacia atrás de 2 en 2, comenzando desde el número elegido por el usuario y 
deteniéndose exactamente en el 0 (inclusive). Escribe la línea de tu range() modificada:

Respuesta: for i in range(num, -1, -2):
                print("Conteo:", i)

"""

"""
# Sección 2: Funciones Matemáticas de Python (math)
# Python incluye funciones matemáticas integradas (built-in) y un módulo especializado llamado math.
# ==========================================

#Código 2.1:

import math

decNum = -34.5678
intNum = 9

print( round(decNum, 2) )   # Línea A  #Redondea el número decimal -34.5678 a 2 posiciones decimales.
print( round(decNum, 0) )   # Línea B  #Redondea a 0 posiciones decimales, pero al pasar un valor flotante a round(), devuelve un tipo float (por eso conserva el .0).
print( int(decNum) )        # Línea C  #La función int() elimina todos los decimales sin redondear, dejando solo la parte entera.
print( abs(decNum) )        # Línea D  #Devuelve el valor absoluto del número, es decir, elimina el signo negativo haciéndolo positivo.
print( math.pow(intNum, 2) ) # Línea E #Eleva un número a una potencia, En este caso, eleva 9 a la potencia 2. La función math.pow() siempre devuelve un número flotante
print( math.sqrt(intNum) )   # Línea F #Calcula la raíz cuadrada (square root) del número. todas las funciones matemáticas del módulo math convierten internamente el resultado a tipo float.

Predicciones de Salida (Escribe el resultado exacto):
# 5. ¿Resultado de la Línea A round(decNum, 2)? 34.57 

# 6. ¿Resultado de la Línea B round(decNum, 0)? -35.0

# 7. ¿Resultado de la Línea C int(decNum)? -34 (Pista: ¿Redondea o trunca los decimales?) trunca los decimales.

# 8. ¿Resultado de la Línea D abs(decNum)? 34.5678

# 9. ¿Resultado de la Línea E math.pow(intNum, 2)? 81.0

# 10. ¿Resultado de la Línea F math.sqrt(intNum)? 3.0

"""
"""
# Sección 3: Comparación de Textos mediante ASCII / Unicode
# Las funciones max() y min() en Python no solo funcionan con números; en cadenas de texto comparan valores según la tabla 
# de caracteres ASCII/Unicode.
# ==========================================

#Código 3.1:

miMax = min("Banano", "manzana", "Zanahoria")
print("El máximo es:", miMax)


Análisis:
# 11. Antes de ejecutar: ¿Cuál crees que será el resultado devuelto por max()?

Predicción: Zanahoria
# 12. Ejecuta el código. ¿Cuál fue el resultado real devuelto?

Resultado: manzana

# 13. Sabiendo que en la tabla ASCII las mayúsculas tienen valores numéricos menores que las minúsculas, explica por qué "manzana" fue seleccionada como la mayor frente a "Zanahoria".
Porque Python compara las cadenas de texto caracter por caracter utilizando sus valores en la tabla ASCII / Unicode:
Las letras mayúsculas van antes que las minúsculas:
"Banano" empieza con 'B' (Unicode 66).
"Zanahoria" empieza con 'Z' (Unicode 90).
"manzana" empieza con 'm' (Unicode 109).
Como max() busca el valor más grande según la tabla Unicode, las letras minúsculas le ganan siempre a cualquier mayúscula.

# 14. Cambia la función de max() a min(). ¿Qué valor obtienes ahora y por qué?

Resultado: Banano

"""
"""
# Sección 4: Aplicación Práctica – Física y Matemáticas
# La policía de tránsito calcula la velocidad v de un auto a partir de la longitud d de la huella de frenado utilizando la fórmula: 
# v = \sqrt{20 \cdot d}.
# ==========================================

#Código 4.1:

import math

d = int(input("Ingresa la longitud de la huella de frenado (en metros): "))

# Completa la ecuación usando math.sqrt():
v = math.sqrt(20 * d)

print("Velocidad estimada del auto:", round(v, 2), "km/h")


Análisis:
# 15. Completa la asignación v = en el código superior utilizando la función math.sqrt() y la fórmula entregada. 
# Escribe la línea completa a continuación:

Respuesta: v = math.sqrt(20 * d)
"""
"""
# Sección 5: Segmentación de Cadenas (Slicing)
# El slicing o rebanado permite extraer subcadenas utilizando la sintaxis cadena[inicio:fin:paso].
# ==========================================

#Código 5.1:

nombre = "Building Puentes"

print("Índice 0:", nombre[0])
print("Segmento:", nombre[9:])


Análisis:
# 16. ¿Qué carácter imprime exactamente nombre[0]? La B

# 17. ¿En qué posición (índice) exacta se encuentra el espacio en blanco entre ambas palabras? En el 8 por que se cuenta desde 0.

# 18. Modifica los índices en nombre[X:Y] para extraer e imprimir exactamente la palabra "Puentes".

Opción con 2 valores: nombre[ 9 : 16 ]
#La 'P' está en el índice 9 y la 's' final en el 15. Dado que el límite superior es exclusivo,
# debemos indicar 16 para incluir la última letra.

Opción con límite implícito: nombre[ 9 : ]
#Al omitir el valor después de los dos puntos (:), Python toma automáticamente hasta el final de la cadena.
"""
"""
# Sección 6: Filtrado e Inspección de Caracteres en Cadenas
# Podemos usar bucles combinados con condicionales para inspeccionar y filtrar tipos específicos de caracteres dentro de un texto.
# ==========================================

#Código 6.1:

texto = input("Ingresa una frase con letras y números: ")
contador_numeros = 0

for caracter in texto:
    if caracter >= "0" and caracter <= "9":
        contador_numeros += 1

print("Total de dígitos numéricos encontrados:", contador_numeros)


Análisis:
# 19. Ejecuta el programa e ingresa el texto "3 tigres en 2 árboles". ¿Qué valor imprime contador_numeros? 2

# 20. Observa la condición del if. Explica cómo evalúa Python si un carácter individual es un dígito numérico usando los operadores >= y <=.
Por que Python compara los caracteres utilizando sus valores en la tabla ASCII / Unicode: los caracteres "0" a "9" tienen valores consecutivos, por lo que la condición if verifica si el carácter está dentro de ese rango.
(del 48 al 57), y las letras y los espacios están en otras posiciones de la fila, totalmente fuera de ese rango que le dimos.
"""

# Sección 7: Investigación de Métodos de Cadenas (String Methods)
# Investiga en la documentación oficial de Python o en W3Schools el funcionamiento de los siguientes métodos
#  y explica brevemente para qué sirven:
# ==========================================

"""
# 21. Método .rfind('a'):

Descripción: 
Busca la última posición (índice) donde aparece el carácter 'a' dentro del texto recorriéndolo de derecha a izquierda.
Devuelve -1 si no lo encuentra.


# 22. Método .isalpha():

Descripción:
Evalúa si la totalidad de los caracteres presentes en un string corresponden a letras.
Si la cadena contiene un solo carácter que no sea una letra (un espacio, un número, un guion, una coma), la función evaluará a False.

# 23. Método .isdigit():

Descripción:
Verifica si todos los caracteres de la cadena de texto son números enteros comprendidos entre el 0 y el 9. 
Si la cadena contiene letras, símbolos o caracteres de formato, devuelve False.
"""