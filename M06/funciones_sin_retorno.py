# ==========================================
#  M6 Tarea Funciones Reusables
#  Christian Mendoza  
#  Fecha: 2026-10-09
# ==========================================

# =============================================================
# Parte 1: Funciones sin retorno (Acciones directas)
# =============================================================

def mostrar_bienvenida(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a clase hoy.")
"""
Muestra un mensaje de bienvenida personalizado usando el parametro "nombre"
"""

# PREGUNTAS:
# 1. En la función mostrar_bienvenida(nombre), ¿cómo se llama la variable "nombre" dentro de los paréntesis?
#Es un parametro  
# 2. ¿Qué le falta al código para ser completamente reutilizable?
#Le hace falta el return para que la funcion se pueda reutilizar y devolver su valor.


# =============================================================
# Parte 2: Funciones con retorno (Procesamiento de datos)
# =============================================================

def calcular_descuento(precio: float, porcentaje: float = 10):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final
    #print(precio_final) PREGUNTA 14
"""
calcula el precio final de un producto aplicando un descuento, por defecto el porcentaje es 10, pero se pueden dar
otros valores llamando la funcion y modificando los parametros
"""

def es_par(numero):
    return numero % 2 == 0
"""
Determina si el numero es par. Si es par guarda el valor TRUE sino es FALSE
"""

# PREGUNTAS:
# 3. ¿Qué palabra clave (keyword) de Python se utiliza para indicar que estamos definiendo una función?
# La palabra clave es "def".

# 4. Escribe los nombres de las dos funciones definidas arriba.
# "calcular_descuento" y "es_par".

# 5. ¿Qué sucede cuando llamas a la función pasando solo un argumento, como calcular_descuento(100)?
# Se tomaria el valor de precio=100 y el porcentaje como no se lo diste, toma su valor por defecto 10 al definir la funcion.

# 6. ¿Qué ocurre si pasas dos argumentos, como calcular_descuento(200, 20)?
# Toma el valor de precio a 200 y el porcentaje a 20.


# =============================================================
# Parte 3: Pruebas de ejecución
# =============================================================

print("--- PRUEBA 1: Mostrar Bienvenida ---")
mostrar_bienvenida("Ana")
mostrar_bienvenida("Carlos")

print("\n--- PRUEBA 2: Cálculo de Descuentos ---")

compra_1 = calcular_descuento(100)
print(f"Precio con descuento por defecto: ${compra_1}")


compra_2 = calcular_descuento(200, 20)
print(f"Precio con 20% de descuento: ${compra_2}")

# PREGUNTAS:
# 7. Escribe el pseudocódigo de las funciones en la Parte 2.
"""
Funcion calcular_descuento:
    Declarar argumentos: precio variable y porcentaje por defecto 10 
    Calcular descuento = precio * (porcentaje / 100)
    Calcular precio_final = precio - descuento
    Devolver precio_final para poder reutilizar la funcion

Funcion es_par:
    Declarar argumento: numero
    Retornar True si numero es divisible entre 2, de lo contrario False
"""
# 8. Explícale una de las dos a tu compañera(o) de al lado e incluye el propósito del programa. Tu compañera(o) te debe explicar lo siguiente. Lleguen a un acuerdo para agregar lo esencial como comentarios.
# Este ejercicio sirve para practicar el uso de funciones que reciben datos y nos devuelven resultados listos para ser reutilizables.

# 9. Cambia las funciones para que acepten decimales en el precio.


# =============================================================
# Parte 4: Alcance (Scope) y Retorno
# =============================================================

# La función mostrar_bienvenida() usa print(), mientras que calcular_descuento() usa return.
# Si asignas la llamada de la bienvenida a una variable:

resultado = mostrar_bienvenida("Julio")
print(resultado)
#print(descuento)  PREGUNTA 12
#print(compra_1 + 5) PREGUNTA 14


# PREGUNTAS:
# 10. ¿Qué valor se guarda en la variable 'resultado' y por qué?
# No guarda un valor, porque no se le agrego el "return" para guardar su valor, solo imprime el mensaje.

# 11. ¿Por qué es necesario usar return en calcular_descuento() para poder guardar el precio final en compra_1 y compra_2?
# Para poder usar el valor dado cuando se declaro la funcion.

# 12. Intenta ejecutar la siguiente línea al final del documento: print(descuento) ¿Qué error muestra Python?
# NameError: name 'descuento' is not defined

# 13. ¿Por qué la variable 'descuento' no es accesible fuera de la función?
# Por que "descuento" es una variable local dentro de la funcion "calcular_descuento", cuando acaba la funcion "desaparece" por asi decirlo.

# 14. ¿Qué ocurre si dentro de calcular_descuento cambias 'return precio_final' por 'print(precio_final)' e intentas sumar 'compra_1 + 5'?
# Muestra TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

# 15. Investiga: ¿Cómo podrías llamar a la función 'calcular_descuento' asignando el porcentaje mediante su nombre de parámetro (keyword argument)?
# Se le agrega un = y le das el valor correspondiente, por ejemplo:
# compra_3 = calcular_descuento(100, porcentaje=50)

# 16. Añade un "docstring" (comentario multilínea con """) dentro de cada función para explicar brevemente qué hace.
