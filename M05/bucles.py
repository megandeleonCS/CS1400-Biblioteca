# ==========================================
#  M5 Tarea 2
#  Christian Mendoza  
#  Fecha: 2026-09-29
# ==========================================

"""
# Sección 1: ¿Por qué usar un Bucle? (Repetición Manual vs. Iteración)
# Analiza el siguiente código para comprender la necesidad de los bucles.
# ==========================================

#Código 1:
# Impresión manual repetitiva
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")

Análisis:
# 1. Si quisieras saludar a 100 estudiantes, ¿qué problema presenta el enfoque mostrado en el Código 1?
Que se tendrian que escribir 100 veces esa linea de codigo, haciendo el programa mas ineficiente y propenso a errores.
Y si quisieras cambiar el mensaje lo tendrias que hacer en las 100 lineas.

# 2. ¿Crees que este enfoque manual permite adaptar el número de saludos dinámicamente si el usuario lo solicita en tiempo de ejecución? 
# Explica por qué.
No por que el codigo es estatico (hardcoded) y no permite cambios dinámicos en tiempo de ejecución.

"""
"""
# Sección 2: Bucle while (Iteración Indefinida)
# Analiza cómo la estructura condicional if difiere del bucle while.
# ==========================================

#Código 2:
# Intento de repetición con if
respuesta = input("¿Deseas repetir el proceso? (si/no): ")

while respuesta == "si":
    print("Ejecutando el bloque...")
    #respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")


Análisis:
# 3. Ejecuta el programa e introduce "si" en la primera pregunta y "si" en la segunda. ¿El programa preguntó una tercera vez o finalizó? 
# Explica por qué sucede esto usando un if.
El programa finalizo, por que el if evalua la condicion (si/no) solo una vez aunque se ponga otro input y cambie el valor de la variable respuesta.

Modificación 1A (Cambio a while):
Sustituye la palabra if por la palabra while en el código anterior y ejecútalo de nuevo.

# 4. Ejecuta el programa e ingresa "si" varias veces consecutivas. ¿Cómo cambia el comportamiento respecto al if?
El programa sigue repitiendo el bloque mientas la condicion sea verdadera ("si"), a diferencia del if, el while si vuelve a evaluar la condicion
principalmente porque el while permite la repetición indefinida mientras la condición sea verdadera.

# 5. ¿Es posible saber con exactitud de antemano cuántas veces el usuario escribirá "si" antes de ejecutar el programa?
No, eso depende del usuario, por eso se usa un while cuando no sabes exactamente cuantas veces se cumplirá la condición.

Modificación 1B (Bucle Infinito):
Comenta la línea respuesta = input(...) que está dentro del bloque while. Ejecuta el programa e introduce "si".

# 6. ¿Qué le sucede al programa cuando no se actualiza la variable de control dentro del while?
Entra en un bucle infinito por que la variable "respuesta" siempre sigue siendo "si" y nunca se actualiza dentro del while.

# 7. Investiga qué combinación de teclas se utiliza en la terminal para detener un bucle infinito en ejecución (Ctrl+C u otra). Escríbela.
Ctrl + C (en Windows/Linux/macOS) envía una señal de interrupción de teclado (KeyboardInterrupt) a la terminal para forzar la detención
inmediata del script.
"""
"""
# Sección 3: Bucle for y la Función range() (Iteración Definida)
# Usamos for cuando queremos iterar sobre un número conocido de repeticiones o sobre una secuencia.
# ==========================================

#Código 3:
# Ejemplo de range() simple
num = int(input("Introduce un número límite: "))

for i in range(2, 11, 2):
    print("Iteración:", i)


Análisis:
# 8. Ejecuta el programa e ingresa el valor 10. ¿Cuántas veces se imprimió la palabra "Iteración"? ¿Influyó en algo el número ingresado
# por teclado en este primer intento?
Se imprimio 10 veces y no, no influyo el numero ingresado (10) por que nunca se utilizo la variable num dentro del bucle.

# 9. Observa la salida numéricas de i. ¿Cuál es el valor inicial y cuál es el valor final impreso?

Valor inicial: 0

Valor final: 9

# 10. ¿Se llegó a imprimir el número 10 en la consola? Explica por qué Python excluye el límite superior en range().
No se imprimio el numero 10 porque la secuencia comienza en 0 y los 10 elementos se cuentan desde 0 hasta 9.
(El limite superior en range() es exclusivo.)

# 11. Cambia range(10) por range(0, 10). ¿Existe alguna diferencia en el resultado obtenido?
No, por que solo escribir 10 es equivalente a range(0, 10).

Modificación 2A (Rango con Variable Límite):
Cambia la línea del rango para usar la variable num: range(1, num).
# 12. Ejecuta e ingresa 20. ¿El conteo se detuvo en 20 o en 19?
Se detuvo en 19 porque el rango va de 1 hasta 20, pero como se comento arriba el límite superior en range() es exclusivo.

# 13. ¿Qué ajuste matemático debes hacer dentro de range() para que la cuenta incluya exactamente el número ingresado por el usuario?

Respuesta: range(1, num + 1)

Modificación 2B (Uso del Argumento Step / Paso):
Modifica la línea a: range(2, 11, 2).

# 14. Ejecuta el programa. ¿Qué valores se imprimieron y qué función cumple el tercer argumento dentro de range(inicio, fin, paso)?
Los valores que se imprimieron fueron: 2, 4, 6, 8, 10.
El tercer argumento especifica el incremento o tamaño del paso entre cada iteración.
"""
"""
# Sección 4: Iteración sobre Secuencias (Cadenas y Listas)
# Un bucle for permite iterar directamente sobre los elementos de una colección sin necesidad de usar contadores manualmente.
# ==========================================

#Código 4:
# Iteración sobre una cadena de texto
palabra = "Python"

print("--- Letras de la palabra ---")
for letra in palabra:
    print(letra)

# Iteración sobre una lista
frutas = ["manzana", "banana", "cereza"]

print("--- Lista de frutas ---")
for fruta in frutas:
    print(fruta)


Análisis:
# 15. En el primer bucle for letra in palabra:, ¿qué representa la variable letra en cada paso del bucle?
Representa un caracter individual de la cadena de texto leyendolo de izquierda a derecha.

# 16. En el segundo bucle for fruta in frutas:, contrasta la iteración directa (for fruta in frutas:) con el acceso por índices
# (for i in range(len(frutas)):). ¿Cuál de las dos opciones resulta más legible para un principiante y por qué?
La mejor opcion es usar la iteracion directa (for fruta in frutas:), por que el programa toma el primer elemento de la lista
lo guarda y lo usa, en la siguiente iteración toma el segundo y asi sucesivamente. Mientras que con el acceso por índices
primero cuenta cuantos elementos hay en la lista y luego accede a cada uno mediante su índice, que tu le tienes que proporcionar manualmente.
"""
"""
# Sección 5: Sentencias de Control de Bucles (break y continue)
# Podemos alterar el flujo normal de un bucle mediante instrucciones de control.
# ==========================================

#Código 5:
# Uso de break y continue
print("Demostración de continue:")
for num in range(1, 6):
    if num == 3:
        continue
    print("Número:", num)

print("\nDemostración de break:")
for num in range(1, 6):
    if num == 3:
        break
    print("Número:", num)


Análisis:
# 17. Observa la salida de la Demostración de continue. ¿Qué número falta en la secuencia impresa y por qué ocurrió esto?
Falto el numero 3 por que cuando la variable "num" es igual a 3, se ejecuta el continue que hace que se salte la iteracion actual
y pasa al siguiente ciclo del bucle.

# 18. Observa la salida de la Demostración de break. ¿Qué números se imprimieron y qué hace la instrucción break al ejecutarse?
Se imprimieron el 1 y el 2, el break interrumpe y finaliza la ejecucion del buicle actual, cuando la variable "num" es igual a 3
el bucle finaliza sin imprimir el número 3 ni los siguientes.

# 19. Supón que construyes un bucle while True: para solicitar claves de acceso. ¿Qué sentencia te permitiría salir del bucle una vez
# que el usuario ingrese la clave correcta?
Usaria la sentencia break para salir del bucle una vez que la condicion de acceso sea correcta.
"""
"""
# Sección 6: Patrones de Acumulación y Conteo
# Un patrón común en programación consiste en acumular valores o contar ocurrencias a medida que iteramos
# ==========================================

#Código 6:
# Acumulador de suma y contador de coincidencias
numeros = [4, 7, 2, 9, 10, 5]
suma_total = 0
mayores_a_cinco = 0

for num in numeros:
    suma_total += num  # Acumula la suma
    if num > 5:
        mayores_a_cinco += 1  # Incrementa el contador

print("Suma total:", suma_total)
print("Cantidad de números mayores a 5:", mayores_a_cinco)


Análisis:
# 20. ¿Con qué valor deben inicializarse las variables suma_total y mayores_a_cinco antes de comenzar el bucle? 
# ¿Qué pasaría si las inicializas dentro del bucle?
Se deben inicializar con 0 antes de comenzar el bucle.
Si se inicializaran dentro del bucle, se reiniciarían en 0 en cada iteración y y se perderian los valores acumulados previamente.

# 21. Explica con tus palabras la diferencia entre un acumulador (suma_total += num) y un contador (mayores_a_cinco += 1).
Un contador suma la cantidad fija contantemente cada vez que se cumple la condicion especificada.
Mientras que el acumulador suma una cantidad variable en cada iteracion. 
Su objetivo es como responder a la pregunta: Cuanto suman en total estos valores? (esta parte me la explico a profundidad gemini
y me gusto ponerlo para recordarlo facilmente)
"""

# Sección 7: Normalización de Textos con .lower()
# Analiza cómo formatear cadenas dentro o fuera de un bucle para realizar comparaciones precisas.
# ==========================================

#Código 7:
sujeto1 = "Python"
sujeto2 = "python"

if sujeto1.lower() == sujeto2.lower():
    print("Iguales")
else:
    print("Diferentes")

"""
Análisis:
# 22. Observa las variables sujeto1 y sujeto2. ¿Cuál es la diferencia visual entre ambos textos y cuál es el resultado de la comparación inicial?
La diferencia es la P mayuscula y miniscula y el resultado de la comparación inicial es "Diferentes".
(Por que Python las cadenas son sensibles a las mayusculas y minusculas por su valor en Unicode/ASCII)

# 23. Modifica la condición a if sujeto1.lower() == sujeto2.lower():. Ejecuta el código nuevamente. 
# ¿Qué resultado obtienes y qué transformación realiza el método .lower()?
El resultado es "Iguales" por que usando .lower() se convierten ambas cadenas a minusculas.

# 24. ¿Por qué es útil aplicar .lower() a las respuestas del usuario cuando trabajamos con entradas dentro de un bucle while 
# (por ejemplo, al validar "SI", "Si" o "si")?
Para asegurarnos que la comparacion de las respuestas del usuario no dependa de si se escriben en mayúsculas o minúsculas.
El valor siempre se transforma a minusculas antes de la comparacion.
"""
