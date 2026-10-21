""" 
M7 Laboratorio presencial:
Elije una pareja para entrevistar.
La concatenación de cadenas para aprender a usar + y unir cadenas de texto.
Incluir espacios manualmente (" "), y combinar entrada del usuario con otros textos.
"""

# TODO Tarea 1: Escribe una linea de bienvenida a este programa 
print("Bienvenido")

# TODO Tarea 2: Solicitar datos del usuario. 
# Usar tres variables: nombre, apellido, y cancion.
# ## Entrevista algun companero(a) para averiguar su cancion preferida y su nombrecompleto.
nombre = input("ingresa tu nombre\n")
apellido = input("ingresa tu apellido\n")
cancion = input("Escribe el nombre de tu canción favorita.\n")
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
nombre_completo = nombre+" "+apellido
# TODO Tarea 4: Mostrar el resultado con alguna frase como por ejemplo, "Tu nombre completo es  ___ "
print (f"holla {nombre_completo} Es estupendo tenerte aquí de nuevo.")

# TODO Tarea 5: Crear un ultimo variable, y agruegale más texto concatenado.
# Puede ser un saludo, o un piropo que incluya el variable para la cancion.
# Por ejemplo, "Hola ___, me encanta que tu cancion favorita sea ___! "

frase_final = nombre_completo + " Me pareció que la elección de la canción " + cancion + " fue simplemente perfecta."
print(frase_final)
# Imprimir a la terminal
print (f"¡Qué buen gusto musical tienes! Elegir {cancion} como tu canción favorita es realmente magnífico.")

