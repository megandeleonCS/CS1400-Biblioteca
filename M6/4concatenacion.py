""" 
M6 Laboratorio presencial:
Elije una pareja para entrevistar.
La concatenación de cadenas para aprender a usar + y unir cadenas de texto.
Incluir espacios manualmente (" "), y combinar entrada del usuario con otros textos.
"""

# TODO Tarea 1: Escribe una linea de bienvenida a este programa 
print("¡Bienvenido al programa de concatenación de cadenas! Hoy vamos a aprender cómo unir texto usando Python.")

# TODO Tarea 2: Solicitar datos del usuario. 
# Usar tres variables: nombre, apellido, y cancion.
# ## Entrevista algun companero(a) para averiguar su cancion preferida y su nombrecompleto.
nombre = input("Por favor, ingresa tu primer nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")
cancion = input("¿Cuál es tu canción favorita? ")

# Una manera de validar entradas vacías
# Toma en cuenta que cambios podrias realizar si tienen un segundo nombre, y/o un segundo apellido.
# La meta es obtener su nombre completo.
if not nombre.strip():
    print("Por favor, escribe tu primer nombre.")
    exit()

if not apellido.strip():
    print("Por favor, escribe tu apellido.")
    exit()

if not cancion.strip():
    print("Por favor, escribe el nombre de una canción que te guste.")
    exit()

# Formatear entrada: capitalizar nombres
# Agregar nuevos variables si es necesario.
nombre = nombre.strip().capitalize()
apellido = apellido.strip().capitalize()
cancion = cancion.strip().title()

# TODO Tarea 3: Crear un variable llamado nombre_completo para juntar
#  (concatenar) todos los nombres ingresados, usando los espacios adecuado.

nombre_completo = nombre + " " + apellido

# TODO Tarea 4: Mostrar el resultado con alguna frase como por ejemplo, "Tu nombre completo es  ___ "

print(f"Tu nombre completo es {nombre_completo}.")

# TODO Tarea 5: Crear un ultimo variable, y agruegale más texto concatenado.
# Puede ser un saludo, o un piropo que incluya el variable para la cancion.
# Por ejemplo, "Hola ___, me encanta que tu cancion favorita sea ___! "
    
mensaje_personalizado = f"Hola {nombre_completo}, me encanta que tu canción favorita sea {cancion}."

# Imprimir a la terminal

print(mensaje_personalizado)