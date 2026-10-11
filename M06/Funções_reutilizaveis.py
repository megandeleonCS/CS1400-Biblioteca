# =============================================================
# Parte 1: Funciones sin retorno (Acciones directas)
# =============================================================

def mostrar_bienvenida(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a clase hoy.")

# PREGUNTAS:
# 1. En la función mostrar_bienvenida(nombre), ¿cómo se llama la variable "nombre" dentro de los paréntesis?
#La variable `nome` es un parámetro.
# 2. ¿Qué le falta al código para ser completamente reutilizable?
#Para que sea reutilizable, falta llamar a la función y pasarle un argumento para que se utilice.


# =============================================================
# Parte 2: Funciones con retorno (Procesamiento de datos)
# =============================================================

def calcular_descuento(precio, porcentaje=10):
    """calcula el precio final despues de aplicar un descuento"""
    precio = float(precio)
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

def es_par(numero):
    """Verifica si el número es par o impar."""
    return numero % 2 == 0

# PREGUNTAS:
# 3. ¿Qué palabra clave (keyword) de Python se utiliza para indicar que estamos definiendo una función?
#def
# 4. Escribe los nombres de las dos funciones definidas arriba.
#calcular_descuento  # es_par
# 5. ¿Qué sucede cuando llamas a la función pasando solo un argumento, como calcular_descuento(100)?
#Cuando utilizamos un solo argumento, la función emplea el valor establecido del descuento.
# 6. ¿Qué ocurre si pasas dos argumentos, como calcular_descuento(200, 20)?
#Cuando utilizamos dos argumentos, la función sustituye el valor fijo.

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
#1 recibir el precio del producto.
#2 recibir el porcentaje de descuento.
#3 calcular el importe del descuento.
#4 restar el descuento del precio original.
#5 devolver el precio final.
# recibir un numero
#dividir el numero entre 2 
#verificar se el resto es igual a zero 
#si es iqual a zero retorna verdadeiro 
#si es diferente retorna falso 
# 8. Explícale una de las dos a tu compañera(o) de al lado e incluye el propósito 
# del programa. Tu compañera(o) te debe explicar lo siguiente. 
# Lleguen a un acuerdo para agregar lo esencial como comentarios.
#def es_par(numero): esta funcion verifica se un numero es par o impa.
#retun numero % 2 == 0 divide entre 2 y comprueba si el resto es ceero.

# 9. Cambia las funciones para que acepten decimales en el precio.


# =============================================================
# Parte 4: Alcance (Scope) y Retorno
# =============================================================

# La función mostrar_bienvenida() usa print(), mientras que calcular_descuento() usa return.
# Si asignas la llamada de la bienvenida a una variable:

resultado = mostrar_bienvenida("Julio")
print(resultado)

# PREGUNTAS:
# 10. ¿Qué valor se guarda en la variable 'resultado' y por qué?
#La variable `resultado` no almacena nada porque la función utiliza `print(resultado)` y no devuelve ningún valor. 
# 11. ¿Por qué es necesario usar return en calcular_descuento() para poder guardar el precio final en compra_1 y compra_2?
#para devolver el precio final y poder guardarlo en las variables compra_1 y compra_2
# 12. Intenta ejecutar la siguiente línea al final del documento: print(descuento) ¿Qué error muestra Python?
#NameError: name 'descuento' is not defined
# 13. ¿Por qué la variable 'descuento' no es accesible fuera de la función?
# porque la variable es local, fue creada dentro de la función y no se puede acceder a ella desde fuera.
# 14. ¿Qué ocurre si dentro de calcular_descuento cambias 'return precio_final' por 'print(precio_final)' e intentas sumar 'compra_1 + 5'?
#Dará un error porque `print` solo muestra el valor de la variable, no le devuelve ningún valor.
# 15. Investiga: ¿Cómo podrías llamar a la función 'calcular_descuento' 
# asignando el porcentaje mediante su nombre de parámetro (keyword argument)?
#puedo llamar a la funcion usando el nombre del parametro :calcular_descuento(100,porcentaje=15)
# 16. Añade un "docstring" (comentario multilínea con """) dentro de cada función para explicar brevemente qué hace.
