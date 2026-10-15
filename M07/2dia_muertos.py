# ==========================================
#  M7 Proyecto Dia De Los Muertos
#  Christian Mendoza  
#  Fecha: 2026-10-14
# ==========================================

# Tarea 2: El Registro de los Ancestros (Diccionarios y Conjuntos)

# Tarea 2: Registro de visitas y ofrendas asignadas

# Diccionario con el ancestro (llave) y su platillo favorito (valor)
altares_familiares = {
    "Abuela Coco": "Tamales de dulce",
    "Tío Héctor": "Mole poblano",
    "Bizabuelo Julio": "Atole de chocolate"
}

# Lista con flores traídas por los visitantes (contiene duplicados)
flores_recibidas = ["Cempasúchil", "Nube", "Cempasúchil", "Terciopelo",
 "Nube", "Cempasúchil"]

#4. Iteración en Diccionarios: Escribe un bucle for utilizando el método .items() para imprimir una frase por cada ancestro.
# (Ejemplo de salida esperada: "Para Abuela Coco preparamos: Tamales de dulce").
for ancestro, platillo in altares_familiares.items(): #Con items() puedo obtener tanto la llave como el valor del diccionario.
    print(f"Para {ancestro} preparamos: {platillo}")

#5. Usa los métodos .keys() y .values() por separado para mostrar en pantalla
#  únicamente los nombres de los ancestros y luego únicamente los platillos.
# Nombres de los ancestros
print("\nNombres de los ancestros:", list(altares_familiares.keys()))

# Platillos
print("\nPlatillos favoritos:", list(altares_familiares.values()))

#6. Uso de Sets (Conjuntos): Para evitar contar flores repetidas en el inventario,
# convierte la lista flores_recibidas en un set usando la función set().
flores = set(flores_recibidas)
print("\nFlores recibidas sin repetir:", flores)

#Con set, se guardan los elementos sin duplicados.(comentario para mi, para que no se me olvide su funcion)

#7. Reflexión: ¿Cuántos elementos tenía la lista original de flores y cuántos quedaron en el conjunto?
# ¿Por qué los conjuntos (sets) son ideales para la limpieza de datos?

"""
La lista original tenia 6 elementos y despues del "set" quedaron solo 3, son ideales para la limpieza de datos
por que no permiten o ignoran por asi decirlo los duplicados.
"""