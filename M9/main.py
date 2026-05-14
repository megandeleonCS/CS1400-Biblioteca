# Funciones Predefinidas
# Observa el segmento de código a continuación y luego responde las preguntas.

# Librería math en Python
import math

decNum = -34.5678
intNum = 9

print(round(decNum, 2))   # Pregunta 1
print(round(decNum, 0))   # Pregunta 2
print(int(decNum))        # Pregunta 3
print(abs(decNum))        # Pregunta 4

print(math.pow(intNum, 2))   # Pregunta 5
print(math.sqrt(intNum))     # Pregunta 6

# Predicciones de salida:
# 1. ¿Resultado del primer print?
# Respuesta: -34.57 porque la función round redondea a dos decimales.
#
# 2. ¿Resultado del segundo print?
# Respuesta: -35.0 porque la función round redondea a cero decimales.
#
# 3. ¿Resultado del tercer print?
# Respuesta: -34 porque int() no redondea, solo elimina los decimales.
#
# 4. ¿Resultado del cuarto print?
# Respuesta: 34.5678 porque abs() devuelve el valor absoluto.
#
# 5. ¿Resultado del quinto print?
# Respuesta: 81.0 porque math.pow(9, 2) calcula 9 al cuadrado.
#
# 6. ¿Resultado del sexto print?
# Respuesta: 3.0 porque la raíz cuadrada de 9 es 3.

# Máximo y Mínimo (Max and Min)
miMax = max("manzana", "Banano", "Zanahoria")
print(miMax)

# 7. ¿Cuál crees que será el resultado al comparar "manzana", "Banano" y "Zanahoria"?
# Respuesta: "manzana", porque Python compara las cadenas según su orden Unicode
# y distingue mayúsculas de minúsculas.

# 8. Ejecuta el código, ¿fue correcta tu suposición?
# Respuesta: Sí, al ejecutar el código se obtiene "manzana".

# 9. Si cambias "manzana" por "Manzana" (mayúscula), ¿crees que esto cambiará el resultado?
# Respuesta: Sí, cambiaría el resultado. Probablemente sería "Zanahoria".

# 10. Cambia la llamada de la función max por min. ¿Obtienes el valor más pequeño?
miMin = min("manzana", "Banano", "Zanahoria")
print(miMin)
# Respuesta: Sí, el valor más pequeño es "Banano".

# Funciones Matemáticas
# La policía necesita una aplicación para determinar la velocidad de los autos
# en un choque mediante la longitud de las huellas de frenado d.
# Ecuación:
# v = math.sqrt(30 * d)

# 11 y 12. Código para calcular la velocidad
d = float(input("Ingresa la longitud de la huella de frenado: "))

if d < 0:
    print("Error: la distancia no puede ser negativa.")
else:
    v = math.sqrt(30 * d)
    print("Velocidad del auto:", round(v, 2))

# 12. Escribe la ecuación aquí:
# v = math.sqrt(30 * d)

# Cadenas de Texto (Strings)

# 13. Observa las variables sujeto1 y sujeto2. ¿Cuál es la diferencia entre los textos?
# Respuesta: "Python" empieza con mayúscula y "python" con minúscula.

# 14. Ejecuta el código, ¿los valores se comparan como iguales o diferentes?
# Respuesta: Diferentes, porque Python distingue entre mayúsculas y minúsculas.

sujeto1 = "Python"
sujeto2 = "python"

if sujeto1 == sujeto2:
    print("Iguales")
else:
    print("Diferentes")

# 15. Agrega .lower() al final de sujeto1 y sujeto2 en la sentencia if.
# 16. Ejecuta el programa de nuevo, ¿los valores son iguales o diferentes?
# Respuesta: Iguales, porque ambos se convierten a minúscula.

if sujeto1.lower() == sujeto2.lower():
    print("Iguales")
else:
    print("Diferentes")

# Segmentación de Cadenas (Slicing)

nombre = "Building Puentes"
print(nombre[0])
print(nombre[8:10])

# 17. ¿Qué letra imprime exactamente nombre[0]?
# Respuesta: B

# 18. ¿En qué posición (índice) está el primer espacio en "Building Puentes"?
# Respuesta: 8

# 19. Corrige nombre[X:Y] para que imprima exactamente "Puentes".
print(nombre[9:16])
# Respuesta: nombre[9:16]

# Iteración de Cadenas

str_val = "hello"
for i in range(0, 5):
    print(str_val[i])

# 20. ¿Cuál es la longitud de la cadena str_val?
# Respuesta: 5

# 21. ¿Por qué usa el rango 0, 5?
# Respuesta: Porque los índices de "hello" van de 0 a 4.

# 22. ¿Qué valor de la cadena se está imprimiendo?
# Respuesta: Cada carácter de la cadena, uno por uno.

# 23. ¿Qué crees que se imprimirá al ejecutar el código?
# Respuesta:
# h
# e
# l
# l
# o

# 24. Modifica str_val para usar input y prueba con una palabra larga.
str_val = input("Ingresa una palabra: ")
for i in range(0, 5):
    if i < len(str_val):
        print(str_val[i])

# Respuesta 24:
# No necesariamente se imprime completa, porque el rango solo llega hasta 5.

# 25. Reemplaza el 5 con len(str_val).
str_val = input("Ingresa otra palabra: ")
for i in range(0, len(str_val)):
    print(str_val[i])

# Respuesta 25:
# Sí, ahora se imprime completa.

# 26. Mostrar la palabra en orden inverso.
# Respuesta: Hay que restar 1 a la longitud para comenzar en la última posición.

for i in range(len(str_val) - 1, -1, -1):
    print(str_val[i])

# Ahora mira este código y compáralo con el anterior:
str_val = "hello"
for i in str_val:
    print(i)

# 27. ¿Cuál es la diferencia entre cómo se comportan y cómo están programados?
# Respuesta: Uno recorre la cadena por índices y el otro recorre directamente
# cada carácter.

texto = input("Ingresa una frase que contenga texto y números: ")
for i in range(0, len(texto)):
    if texto[i] >= "0" and texto[i] <= "9":
        print("Hay un número en la posición:", i)

# 28. ¿El programa reporta las posiciones correctamente?
# Respuesta: Sí.

# 29. ¿Con qué se compara cada carácter para determinar si es un valor numérico?
# Respuesta: Con "0" y "9".

texto = input("Ingresa una frase que contenga texto y números: ")

# Inicializar el contador
numeros = 0

# Recorrer el texto carácter por carácter
for i in range(0, len(texto)):
    if texto[i] >= "0" and texto[i] <= "9":
        numeros += 1

# Mostrar el total de números encontrados
print("Total de números:", numeros)

# Explicación:
# En lugar de imprimir cada posición donde aparece un número, el contador
# "numeros" se incrementa cada vez que se encuentra un dígito.
