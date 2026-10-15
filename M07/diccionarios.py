# ==========================================
#  M7 Tarea Diccionarios
#  Christian Mendoza  
#  Fecha: 2026-10-13
# ==========================================

"""
Parte 1 realizada por Hyrum Orozco

"""

# Diccionarios
# Agregar, reemplazar y eliminar elementos de un diccionario

# 1. ¿Qué signo de puntuación separa la clave del valor?
# Respuesta: Los dos puntos (:).

# 2. ¿Por qué no hay una coma después de "Cruz"?
# Respuesta: Porque es el último elemento del diccionario.

# 3. ¿Cuántos pares clave-valor hay inicialmente?
# Respuesta: 6 pares clave-valor.

num_salon = {
    "Murphy": 304,
    "Feiz": 336,
    "Mack": 207,
    "Ball": 227,
    "Bristow": 321,
    "Cruz": 101
}

print("La longitud es", len(num_salon))

# 4. ¿Qué reporta len() como longitud del diccionario?
# Respuesta: 6.

# Agregar un elemento adicional al diccionario
num_salon["Valle"] = 216

# 5. Agregar a DeLeon con el salón 147.
num_salon["DeLeon"] = 147

# 6. ¿Cambia la longitud al agregar a DeLeon?
# Respuesta: Sí, aumenta en 1.

# 7. Agregar a Hernandez con el salón 323 usando corchetes.
num_salon["Hernandez"] = 323

print("La longitud ahora es ", len(num_salon))

# 8. ¿Qué imprime .get() para Valle: la clave o el valor?
# Respuesta: El valor 216.

print( num_salon.get("Valle") )

# 9. ¿Qué se imprime usando los corchetes?
# Respuesta: 304, el número de salón de Murphy.

print( num_salon["Murphy"])

# 10. ¿Hay alguna diferencia entre [] y .get()?
# Respuesta: Sí. .get() devuelve None si la clave no existe;
# los corchetes producen un error KeyError.

# 11. Imprimir el número de salón de Murphy.
print(num_salon["Murphy"])



"""
Parte 2 realizada por Grecia Lopez Orozco
"""


# ¿Cuántos perros hay en el refugio al principio?
# 49 perros 

# ¿Cuántos perros se están agregando al refugio?
# 2 perros

# Escribe la línea de código para eliminar 3 gatos del refugio.
# animalesRefugiados["gato"] -= 3

# Observa el código para agregar los hurones. ¿Cuántos se agregaron?
# 2

# Escribe el código para agregar 4 serpientes al refugio.
# animalesRefugiados["serpiente"] = 4

# Escribe una sentencia if para imprimir "Lleno" si el número de perros es mayor a 50.
# if animalesRefugiados["perro"] > 50:
#    print("Lleno")

# Escribe una sentencia if para imprimir "No Ratones" si "raton" no es una clave en el diccionario animalesRefugiados.
# if "raton" not in animalesRefugiados:
#     print("No Ratones")

# Nota que la variable refugioOriginal es igual a la variable animalesRefugiados. ¿Es esta una copia superficial o profunda?
# No es ninguna de las dos. Las dos variables apuntan al mismo diccionario, asi que los cambios afectan a ambas
# print(refugioOriginal)

# Escribe el comando para mostrar los animales de refugioOriginal al final del segmento de código. ¿Muestra los animales originales?

# Cambia refugioOriginal para que sea una copia profunda (deep copy) de animalesRefugiados (recuerda importar la librería copy). ¿Muestra los animales originales ahora?

# ¿Qué diferencia notas entre una copia profunda y una copia superficial?

"""
Python
import copy

animalesRefugiados = {"perro": 49, "gato": 38, "conejo": 14}
refugioOriginal = animalesRefugiados
animalesRefugiados['perro'] += 2
animalesRefugiados["huron"] = 2
print(animalesRefugiados)
"""

import copy

animalesRefugiados = {"perro": 49, "gato": 38, "conejo": 14}

# Hacer una copia profunda antes de modificar los animales
refugioOriginal = copy.deepcopy(animalesRefugiados)

# Agregar perros
animalesRefugiados["perro"] += 2

# Agregar hurones
animalesRefugiados["huron"] = 2

# Eliminar 3 gatos
animalesRefugiados["gato"] -= 3

# Agregar 4 serpientes
animalesRefugiados["serpiente"] = 4

# Revisar si hay más de 50 perros
if animalesRefugiados["perro"] > 50:
    print("Lleno")

# Revisar si hay ratones
if "raton" not in animalesRefugiados:
    print("No Ratones")

# Mostrar los animales actuales y la copia original
print("Animales actuales:", animalesRefugiados)
print("Refugio original:", refugioOriginal)

# Verificación rápida: la copia profunda debe mantenerse intacta
print("Check: copia profunda intacta:", refugioOriginal == {"perro": 49, "gato": 38, "conejo": 14})

"""
Parte 3 realizada por Christian Mendoza
"""

# Ejemplo de conteo de palabras

text = "sana sana curita de rana sana sana pomada de sapo sana sana hoy y manana manana y hoy"

lst = text.split()
plbList = dict()

for x in lst:
    if x not in plbList:
        plbList[x] = 1
    else:
        plbList[x] += 1

for i in plbList:
    print (i, plbList[i])

# Ejemplo de conteo de calificaciones
notas = "A A A B B A C A B C C E A B A C C C A B B B A B A A A C D A B B C C A A A B A B A C A B B A"
listaNotas = notas.split()
notasDiccionario = dict()

for i in listaNotas:
  if i not in notasDiccionario:
    notasDiccionario[i] = 1
  else:
    notasDiccionario[i] += 1

for i in notasDiccionario:
  print(i, notasDiccionario[i])

"""
Uso de Diccionarios
El siguiente segmento de código contará cuántas veces aparece cada palabra en el texto dado.

Observa la variable listaNotas. ¿Es una lista o un diccionario? 
- Es una lista. 

¿Qué hace la función split()? (Puedes consultar lecciones anteriores).
-  Hace como una subcadena de la cadena original, separando los elementos por espacios.

Observa la variable notasDiccionario. ¿Está definida como una lista o un diccionario?
- Esta definida como diccionario, por que uso la palabra reservada dict().

¿Hay valores en el diccionario o está vacío?
- Empieza vacio y despues en el for se le van dando valores.

Observa el bucle for. ¿Está iterando a través de la lista o del diccionario?
- Esta iterando a traves de la lista.

Dado que la primera puntuación en listaNotas es "A", ¿el código ejecutaría la sentencia if o la sentencia else dentro del bucle?
-Ejecutaria el if por que al inicio el diccionario esta vacio.

El comando es notasDiccionario[i] = 1, cuando i es igual al texto "A", ¿cuál es el par clave-valor que se agrega al diccionario?
- El par clave-valor seria "A": 1.

La calificación "A" se agrega varias veces. La primera vez, pasa por el if. La segunda vez, pasará por el comando else. Hablando de esa segunda vez cuando i = "A", el par clave-valor es inicialmente "A": 1, 
¿a qué valor se actualiza cuando se ejecuta el comando notasDiccionario[i] += 1?
- Se actualiza a "A": 2.

Ejecuta el programa, ¿cuántas veces aparece la calificación "A" en los puntajes?
- Aparece 20 veces.

"""