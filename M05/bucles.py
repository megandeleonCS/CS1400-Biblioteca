# ==============================================================================
# M5 Laboratorio sobre Iteración
# bucles.py
# Grecia Lopez Orozco
# ==============================================================================


#¿Por qué usar un Bucle? 

# Código 1:
# print("Hola, estudiante")
# print("Hola, estudiante")
# print("Hola, estudiante")
# print("Hola, estudiante")
# print("Hola, estudiante")

# Analisis:
# 1. Si quisieras saludar a 100 estudiantes, ¿qué problema presenta el enfoque mostrado en el Código 1?
# Tendría que copiar y pegar la misma línea 100 veces, lo cual significa que el código sea muy largo, aburrido de escribir y fácil de equivocarme

# 2. ¿Crees que este enfoque manual permite adaptar el número de saludos dinámicamente si el usuario lo solicita en tiempo de ejecución? Explica por qué.
# No, porque el número de saludos ya está escrito fijo en el código y no cambia a menos que yo borre o agregue líneas a mano antes de ejecutarlo



# Sección 2 

# Código 2:
# respuesta = input("¿Deseas repetir el proceso? (si/no): ")
# if respuesta == "si":
#     print("Ejecutando el bloque...")
#     respuesta = input("¿Deseas repetir el proceso? (si/no): ")
# print("Programa finalizado.")

# Análisis:
# 3. Ejecuta el programa e introduce "si" en la primera pregunta y "si" en la segunda. ¿El programa preguntó una tercera vez o finalizó? Explica por qué sucede esto usando un if.
# El programa finalizó esto pasa porque el 'if' solo revisa la condición una sola vez y no vuelve a repetir el código.

# Modificación 1A (Cambio a while):
# 4. Ejecuta el programa e ingresa "si" varias veces consecutivas. ¿Cómo cambia el comportamiento respecto al if?
# Ahora con el 'while' el programa me vuelve a preguntar una y otra vez mientras siga escribiendo "si".

# 5. ¿Es posible saber con exactitud de antemano cuántas veces el usuario escribirá "si" antes de ejecutar el programa?
# No, porque depende de cuántas veces decida escribir "si" la persona que lo está usando.

# Modificación 1B (Bucle Infinito):
# 6. ¿Qué le sucede al programa cuando no se actualiza la variable de control dentro del while?
# El programa se queda atascado en un bucle infinito imprimiendo el mensaje sin parar, porque la respuesta nunca cambia.

# 7. Investiga qué combinación de teclas se utiliza en la terminal para detener un bucle infinito en ejecución (Ctrl+C u otra). Escríbela.
# Respuesta: Ctrl + C


# Sección 3

# Código 3:
# num = int(input("Introduce un número límite: "))
# for i in range(10):
#     print("Iteración:", i)

# Análisis:
# 8. Ejecuta el programa e ingresa el valor 10. ¿Cuántas veces se imprimió la palabra "Iteración"? ¿Influyó en algo el número ingresado por teclado en este primer intento?
# Se imprimió 10 veces. No influyó en nada el número que escribí porque el código tiene escrito range(10) fijo y no usa la variable 'num'.

# 9. Observa la salida numéricas de i. ¿Cuál es el valor inicial y cuál es el valor final impreso?
# Valor inicial: 0
# Valor final: 9

# 10. ¿Se llegó a imprimir el número 10 en la consola? Explica por qué Python excluye el límite superior en range().
# No llegó al 10. Python no incluye el número final porque siempre empieza a contar desde el 0 y se detiene un número antes.

# 11. Cambia range(10) por range(0, 10). ¿Existe alguna diferencia en el resultado obtenido?
# No hay ninguna diferencia, da exactamente el mismo resultado.

# Modificación 2A (Rango con Variable Límite):
# 12. Ejecuta e ingresa 20. ¿El conteo se detuvo en 20 o en 19?
# Se detuvo en 19.

# 13. ¿Qué ajuste matemático debes hacer dentro de range() para que la cuenta incluya exactamente el número ingresado por el usuario?
# Respuesta: range(1, num + 1)

# Modificación 2B (Uso del Argumento Step):
# 14. Ejecuta el programa con range(2, 11, 2). ¿Qué valores se imprimieron y qué función cumple el tercer argumento dentro de range(inicio, fin, paso)?
# Valores impresos: 2, 4, 6, 8, 10
# El tercer argumento sirve para decirle de cuánto en cuánto va a contar (en este caso de 2 en 2).



# Sección 4 

# Código 4:
# palabra = "Python"
# for letra in palabra:
#     print(letra)

# frutas = ["manzana", "banana", "cereza"]
# for fruta in frutas:
#     print(fruta)

# Análisis:
# 15. En el primer bucle for letra in palabra:, ¿qué representa la variable letra en cada paso del bucle?
# Representa cada una de las letras de la palabra "Python", una por una.

# 16. En el segundo bucle for fruta in frutas:, contrasta la iteración directa (for fruta in frutas:) con el acceso por índices (for i in range(len(frutas)):). ¿Cuál de las dos opciones resulta más legible para un principiante y por qué?
# La opción 'for fruta in frutas:' es mucho más fácil de entender porque se lee como español normal: "por cada fruta en la lista de frutas".



# Sección 5

# Análisis:
# 17. Observa la salida de la Demostración de continue. ¿Qué número falta en la secuencia impresa y por qué ocurrió esto?
# Falta el número 3. Ocurrió porque 'continue' le dice al programa que se salte esa vuelta y pase directamente al siguiente número.

# 18. Observa la salida de la Demostración de break. ¿Qué números se imprimieron y qué hace la instrucción break al ejecutarse?
# Números impresos: 1 y 2.
# La instrucción 'break' detiene el bucle por completo y lo cierra inmediatamente.

# 19. Supón que construyes un bucle while True: para solicitar claves de acceso. ¿Qué sentencia te permitiría salir del bucle una vez que el usuario ingrese la clave correcta?
# La sentencia 'break'.



# Sección 6 

# Análisis:
# 20. ¿Con qué valor deben inicializarse las variables suma_total y mayores_a_cinco antes de comenzar el bucle? ¿Qué pasaría si las inicializas dentro del bucle?
# Deben empezar en 0. Si las pongo dentro del bucle, cada vez que dé una vuelta se van a reiniciar a 0 y no van a sumar nada bien.

# 21. Explica con tus palabras la diferencia entre un acumulador (suma_total += num) y un contador (mayores_a_cinco += 1).
# El acumulador va sumando números diferentes (como 4, 7, 2...), mientras que el contador solo va sumando de 1 en 1 para contar cuántas veces pasa algo.



# Sección 7

# Análisis:
# 22. Observa las variables sujeto1 y sujeto2. ¿Cuál es la diferencia visual entre ambos textos y cuál es el resultado de la comparación inicial?
# Una tiene la 'P' mayúscula y la otra es toda en minúscula.
# Sale "Diferentes".

# 23. Modifica la condición a if sujeto1.lower() == sujeto2.lower():. Ejecuta el código nuevamente. ¿Qué resultado obtienes y qué transformación realiza el método .lower()?
# Ahora sale "Iguales".
# Convierte todo el texto a letras minúsculas.

# 24. ¿Por qué es útil aplicar .lower() a las respuestas del usuario cuando trabajamos con entradas dentro de un bucle while (por ejemplo, al validar "SI", "Si" o "si")?
# Porque así no importa si la persona escribe en mayúsculas o minúsculas, el programa lo convierte a minúsculas y lo entiende igual.